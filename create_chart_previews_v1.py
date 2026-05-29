from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


INPUT_FILE = Path("data_clean/final_area_quarter_analysis_v1.csv")
OUTPUT_DIR = Path("chart_previews")


def format_axis(fig):
    fig.update_layout(
        template="plotly_white",
        title_font_size=20,
        font=dict(size=13),
        margin=dict(l=60, r=40, t=80, b=60),
        legend_title_text="",
    )
    return fig


def write_chart(fig, filename):
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / filename
    fig.write_html(path, include_plotlyjs="cdn")
    print(f"Created {path}")


def load_data():
    df = pd.read_csv(INPUT_FILE)
    df["quarter"] = pd.Categorical(
        df["quarter"],
        categories=sorted(df["quarter"].unique()),
        ordered=True,
    )
    return df


def create_top_transactions_chart(df):
    area_totals = (
        df.groupby("area_name_en", as_index=False)["transaction_count"]
        .sum()
        .sort_values("transaction_count", ascending=False)
        .head(15)
        .sort_values("transaction_count")
    )

    fig = px.bar(
        area_totals,
        x="transaction_count",
        y="area_name_en",
        orientation="h",
        title="Top 15 Communities by Residential Apartment Sales Volume",
        labels={
            "transaction_count": "Total transactions",
            "area_name_en": "Community",
        },
        text="transaction_count",
        color="transaction_count",
        color_continuous_scale="Teal",
    )
    fig.update_traces(texttemplate="%{text:,}", textposition="outside")
    fig.update_layout(coloraxis_showscale=False)
    write_chart(format_axis(fig), "01_top_communities_by_transactions.html")


def create_transaction_trend_chart(df):
    top_areas = (
        df.groupby("area_name_en")["transaction_count"]
        .sum()
        .sort_values(ascending=False)
        .head(6)
        .index
    )
    trend = df[df["area_name_en"].isin(top_areas)].copy()

    fig = px.line(
        trend,
        x="quarter",
        y="transaction_count",
        color="area_name_en",
        markers=True,
        title="Quarterly Sales Volume Trend for High-Volume Communities",
        labels={
            "quarter": "Quarter",
            "transaction_count": "Transactions",
            "area_name_en": "Community",
        },
    )
    fig.add_annotation(
        text="Note: 2026Q2 is partial in the current dataset.",
        xref="paper",
        yref="paper",
        x=1,
        y=1.12,
        showarrow=False,
        font=dict(size=12, color="#666"),
    )
    write_chart(format_axis(fig), "02_quarterly_transaction_trend.html")


def create_off_plan_ready_chart(df):
    share = (
        df.groupby("area_name_en", as_index=False)
        .agg(
            total_transactions=("transaction_count", "sum"),
            off_plan_count=("off_plan_count", "sum"),
            ready_count=("ready_count", "sum"),
        )
        .sort_values("total_transactions", ascending=False)
        .head(15)
    )
    share["off_plan_share"] = share["off_plan_count"] / share["total_transactions"]
    share["ready_share"] = share["ready_count"] / share["total_transactions"]
    share = share.sort_values("off_plan_share", ascending=True)

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            y=share["area_name_en"],
            x=share["ready_share"],
            name="Ready / existing",
            orientation="h",
            marker_color="#4C78A8",
            hovertemplate="%{y}<br>Ready share: %{x:.1%}<extra></extra>",
        )
    )
    fig.add_trace(
        go.Bar(
            y=share["area_name_en"],
            x=share["off_plan_share"],
            name="Off-plan",
            orientation="h",
            marker_color="#F58518",
            hovertemplate="%{y}<br>Off-plan share: %{x:.1%}<extra></extra>",
        )
    )
    fig.update_layout(
        title="Off-Plan vs Ready Sales Mix for Top 15 High-Volume Communities",
        barmode="stack",
        xaxis_tickformat=".0%",
        xaxis_title="Share of transactions",
        yaxis_title="Community",
    )
    write_chart(format_axis(fig), "03_off_plan_vs_ready_share.html")


def create_price_trend_chart(df):
    top_areas = (
        df.groupby("area_name_en")["transaction_count"]
        .sum()
        .sort_values(ascending=False)
        .head(6)
        .index
    )
    trend = df[df["area_name_en"].isin(top_areas)].copy()

    fig = px.line(
        trend,
        x="quarter",
        y="median_price_per_sqm",
        color="area_name_en",
        markers=True,
        title="Median Price per Sqm Trend for High-Volume Communities",
        labels={
            "quarter": "Quarter",
            "median_price_per_sqm": "Median price per sqm",
            "area_name_en": "Community",
        },
    )
    fig.update_yaxes(tickformat=",.0f")
    fig.add_annotation(
        text="Median is used to reduce distortion from unusually high-value transactions.",
        xref="paper",
        yref="paper",
        x=1,
        y=1.12,
        showarrow=False,
        font=dict(size=12, color="#666"),
    )
    write_chart(format_axis(fig), "04_median_price_per_sqm_trend.html")


def create_index_page():
    index = OUTPUT_DIR / "index.html"
    index.write_text(
        """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Dubai Property Pulse - Chart Previews</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 40px; line-height: 1.5; color: #1f2933; }
    h1 { margin-bottom: 4px; }
    p { max-width: 760px; }
    li { margin: 10px 0; }
    a { color: #0f766e; font-weight: 600; }
  </style>
</head>
<body>
  <h1>Dubai Property Pulse - Chart Previews</h1>
  <p>V1 chart previews based on DLD residential apartment sales data. The current dataset runs from 2023Q1 to 2026Q2; 2026Q2 is partial. Charts using "Top 15" are filtered by total transaction volume.</p>
  <ol>
    <li><a href="01_top_communities_by_transactions.html">Top communities by sales volume</a></li>
    <li><a href="02_quarterly_transaction_trend.html">Quarterly transaction trend</a></li>
    <li><a href="03_off_plan_vs_ready_share.html">Off-plan vs ready share</a></li>
    <li><a href="04_median_price_per_sqm_trend.html">Median price per sqm trend</a></li>
  </ol>
</body>
</html>
""",
        encoding="utf-8",
    )
    print(f"Created {index}")


def main():
    df = load_data()
    create_top_transactions_chart(df)
    create_transaction_trend_chart(df)
    create_off_plan_ready_chart(df)
    create_price_trend_chart(df)
    create_index_page()


if __name__ == "__main__":
    main()
