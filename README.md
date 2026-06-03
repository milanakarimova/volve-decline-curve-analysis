# Volve Field Decline Curve Analysis

Petroleum engineering project analyzing real Volve field well-production data using Python, SQL, Pandas, NumPy, Matplotlib, and decline curve analysis.

## Dataset

Dataset: Volve production data.

The project uses monthly well-production data, including oil, gas, water, injection, and on-stream information.

## Project Goals

- Clean real well-production data
- Analyze oil production behavior by wellbore
- Perform decline curve analysis
- Estimate monthly and annual decline rates
- Visualize actual vs fitted oil production
- Create SQL-based well production summaries
- Summarize findings in a technical report

## Methodology

This project applies exponential decline curve analysis:

    q(t) = qi * exp(-D * t)

Where:

- q(t): oil production at time t
- qi: estimated initial production rate
- D: decline rate
- t: time in months

## Tech Stack

Python, SQL, SQLite, Pandas, NumPy, Matplotlib, scikit-learn, Excel, Git, GitHub

## How to Run

Install dependencies:

    pip install -r requirements.txt

Clean the data:

    python src/clean_data.py

Run SQL analysis:

    python src/run_sql_analysis.py

Run decline curve analysis:

    python src/decline_curve.py

## Outputs

- Cleaned monthly production dataset
- SQL-based well production summaries
- Decline curve results table
- Actual vs fitted oil production plots
- Detailed technical report

## Project Structure

    data/
      raw/
      processed/
    src/
      clean_data.py
      run_sql_analysis.py
      decline_curve.py
    sql/
      well_production_summary.sql
      yearly_well_production.sql
    reports/
      figures/
      sql_results/
      decline_curve_results.csv
      technical_report.md
    requirements.txt
    README.md

## Technical Report

The detailed technical report is available here:

    reports/technical_report.md

## Portfolio Value

This project demonstrates petroleum production analytics, decline curve fitting, SQL-based production aggregation, visualization, and technical reporting using real well-production data.
