# Dubai Property Pulse - V1 Case Study

## Project Question

Which Dubai communities show the strongest residential apartment sales momentum based on transaction volume, median price per sqm, quarterly growth, and off-plan vs ready sales mix?

## Dataset Scope

- Source: Dubai Land Department / Dubai Pulse transaction data
- Segment: Residential apartment sales
- Period: 2023Q1 to 2026Q2
- Note: 2026Q2 is partial in the current dataset, so quarter-end movement should be treated carefully.
- Analysis level: Top 30 communities by total transaction volume

## Methodology

The transaction data was cleaned and filtered to residential apartment sales only. The analysis then summarized transactions at a community-quarter level to compare sales volume, median price per sqm, and off-plan versus ready/existing sales mix. Median price per sqm was used instead of average price to reduce distortion from unusually high-value transactions.

## Finding 1: Al Barsha South Fourth Leads by Sales Activity

Al Barsha South Fourth is the highest-volume residential apartment market in this V1 dataset, with 51,119 transactions. Business Bay follows with 32,645 transactions, and Marsa Dubai is third with 24,442 transactions.

This matters because transaction volume gives the first view of market activity before looking at price movement. High volume also gives more confidence when comparing trends, because the analysis is based on a larger number of transactions.

## Finding 2: High-Volume Communities Have Different Market Profiles

The top communities are not all behaving the same way. Some are high-volume and heavily off-plan, while others have stronger ready/existing market activity.

For example, Al Barsha South Fourth has the highest transaction count and an off-plan share above 70%. Marsa Dubai has lower transaction volume than Al Barsha South Fourth, but a stronger ready/existing share. This suggests the dashboard should not treat all high-volume communities as one market type.

## Finding 3: Several High-Activity Areas Are Strongly Off-Plan Driven

Some communities are almost entirely off-plan in the current dataset:

- Bukadra: 100.0% off-plan
- Palm Deira: 100.0% off-plan
- Wadi Al Safa 4: 99.5% off-plan
- Madinat Dubai Almelaheyah: 98.6% off-plan
- Al Barshaa South Second: 91.4% off-plan

The careful interpretation is that these areas show developer/new-project-led transaction activity. The dataset does not show buyer motivation, but the sales mix clearly separates these communities from more ready-market-driven areas.

## Finding 4: Ready-Market Anchors Are More Concentrated in Established Areas

The strongest ready/existing shares appear in:

- Al Warsan First: 89.0% ready
- Palm Jumeirah: 68.1% ready
- Burj Khalifa: 59.3% ready
- Marsa Dubai: 54.7% ready
- Al Hebiah Fourth: 50.5% ready

These communities provide a useful contrast to the off-plan-heavy areas. This split helps compare communities with more established ready-market activity against communities where sales activity is more off-plan-led.

## Finding 5: Price Bands Separate Premium Markets from Emerging High-Volume Areas

Median price per sqm shows clear differences across high-volume communities. Marsa Dubai and Business Bay sit in a higher price band, with median price per sqm around 26,494 and 25,315 respectively across the period. Al Barsha South Fourth and Wadi Al Safa 5 are lower-priced but show visible upward movement from 2023 to the latest available quarter.

This is why median price per sqm is useful alongside transaction count. Volume shows where activity is concentrated; price per sqm shows how those markets differ in value positioning.

## Data Caveats

- 2026Q2 is partial, so drops in the latest quarter should not be interpreted as full-quarter market declines.
- Median price per sqm reduces distortion from unusually high-value transactions, but it can still be affected by project mix, unit mix, and transaction composition.
- Off-plan vs ready share describes transaction type only. It does not prove buyer motivation or investor/end-user intent.
- The analysis focuses on residential apartment sales only. Villas, plots, rentals, mortgages, and gifts are outside V1 scope.
