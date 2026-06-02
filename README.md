# Dubai Property Pulse

Dubai Property Pulse is a portfolio analytics project using Dubai Land Department / Dubai Pulse sales transaction data to compare residential apartment sales momentum across Dubai communities.

The V1 analysis focuses on transaction volume, median price per sqm, quarter-over-quarter movement, and off-plan versus ready/existing sales mix.

## Business Question

Which Dubai communities show the strongest residential apartment sales momentum based on transaction volume, median price per sqm, quarterly growth, and off-plan vs ready sales mix?

## Dataset Scope

- Source: Dubai Land Department / Dubai Pulse transaction data
- Segment: Residential apartment sales
- Period: 2023Q1 to 2026Q2
- Analysis level: Top 30 communities by total transaction volume
- Important caveat: 2026Q2 is partial in the current dataset, so latest-quarter volume changes should not be treated as full-quarter market declines.

V1 excludes villas, plots, rentals, mortgages, and gifts. Rental yield is intentionally out of scope for this version.

## Project Workflow

1. Inspect raw DLD transaction files.
2. Clean and filter the data to residential apartment sales.
3. Create a community-quarter analysis table.
4. Generate interactive chart previews.
5. Summarize findings in a short case study.

## Repository Structure

```text
.
├── README.md
├── case_study_v1.md
├── create_clean_v1.py
├── create_final_analysis_v1.py
├── create_chart_previews_v1.py
├── docs/
│   ├── index.html
│   ├── 01_top_communities_by_transactions.html
│   ├── 02_quarterly_transaction_trend.html
│   ├── 03_off_plan_vs_ready_share.html
│   └── 04_median_price_per_sqm_trend.html
├── data_clean/
├── data_raw/
└── requirements.txt
```

Large raw and cleaned CSV files are not intended to be committed to Git.

## Key Outputs

- [V1 case study](case_study_v1.md)
- [Chart preview index](docs/index.html)
- Final analysis dataset: `data_clean/final_area_quarter_analysis_v1.csv`

The final analysis dataset is generated locally and ignored by Git. It can be recreated by running the scripts below.

## V1 Findings

- Al Barsha South Fourth leads the V1 dataset by residential apartment sales volume.
- Business Bay and Marsa Dubai are also high-volume anchor communities, but their price bands and sales mix differ.
- Several high-activity areas, including Bukadra, Palm Deira, Wadi Al Safa 4, and Madinat Dubai Almelaheyah, are strongly off-plan driven.
- Ready/existing market activity is more visible in communities such as Al Warsan First, Palm Jumeirah, Burj Khalifa, and Marsa Dubai.
- Median price per sqm separates premium markets from lower-priced high-volume areas, so volume and price need to be read together.

## Tools Used

- Python
- pandas
- Plotly
- Jupyter Notebook for early inspection

PostgreSQL analysis is a possible next step, but V1 currently uses Python-generated analysis tables and chart previews.

## How To Run Locally

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the data pipeline:

```bash
python create_clean_v1.py
python create_final_analysis_v1.py
python create_chart_previews_v1.py
```

Open the chart previews:

```bash
open docs/index.html
```

## Limitations

- 2026Q2 is partial in the current data extract.
- Median price per sqm can still be affected by project mix, unit mix, and transaction composition.
- Off-plan vs ready share describes transaction type only; it does not prove buyer motivation or investor/end-user intent.
- The analysis is limited to residential apartment sales in V1.
