# Volve Field Decline Curve Analysis

Petroleum engineering project analyzing real Volve field well-production data using Python, Pandas, NumPy, Matplotlib, and decline curve analysis.

## Dataset

Dataset: Volve production data.

The project uses monthly well-production data, including oil, gas, water, injection, and on-stream information.

## Project Goals

- Clean real well-production data
- Analyze oil production behavior by wellbore
- Perform decline curve analysis
- Estimate monthly and annual decline rates
- Visualize actual vs fitted oil production
- Summarize petroleum engineering findings

## Methodology

The project applies exponential decline curve analysis:

    q(t) = qi * exp(-D * t)

Where:

- q(t): production rate at time t
- qi: initial production rate
- D: decline rate
- t: time in months

## Tech Stack

Python, Pandas, NumPy, Matplotlib, scikit-learn, Excel, Git, GitHub

## How to Run

Install dependencies:

    pip install -r requirements.txt

Clean the data:

    python src/clean_data.py

Run decline curve analysis:

    python src/decline_curve.py

## Outputs

- Cleaned production dataset
- Decline curve results table
- Actual vs fitted production plots
- Field/well-level decline rate estimates

## Project Structure

    data/
      raw/
      processed/
    src/
      clean_data.py
      decline_curve.py
    reports/
      figures/
      decline_curve_results.csv
    sql/
    requirements.txt
    README.md

## Portfolio Value

This project demonstrates petroleum production analysis, decline curve fitting, technical interpretation, and Python-based engineering data analysis.
