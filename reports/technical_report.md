# Technical Report: Volve Field Decline Curve Analysis

## 1. Project Overview

This project analyzes real well-production data from the Volve field and applies decline curve analysis to understand oil production behavior at the well level. The main purpose of the project is to demonstrate how petroleum production data can be cleaned, analyzed, visualized, and interpreted using Python and SQL.

The project focuses on practical petroleum engineering tasks such as production trend analysis, well performance comparison, decline rate estimation, and technical reporting.

## 2. Dataset Description

The dataset used in this project is the Volve production dataset. It contains monthly production records for multiple wellbores, including oil, gas, water, injection, and on-stream information.

The main columns used in the analysis are:

- Wellbore name
- Year
- Month
- On-stream hours
- Oil production
- Gas production
- Water production
- Gas injection
- Water injection

The raw Excel dataset was extracted from a compressed file, cleaned, and converted into a structured CSV format for further analysis.

## 3. Data Cleaning Process

The data cleaning stage was performed using Python and Pandas.

The main cleaning steps included:

1. Extracting the Excel file from the raw ZIP archive
2. Reading the monthly production sheet
3. Removing non-data rows and empty rows
4. Renaming long column names into clean and readable names
5. Converting numerical columns into proper numeric types
6. Creating a monthly date column from year and month
7. Sorting the dataset by wellbore and date
8. Saving the cleaned dataset as a CSV file

The cleaned dataset was saved in:

    data/processed/volve_monthly_production_clean.csv

This cleaned file was used for decline curve analysis, SQL aggregation, and visualization.

## 4. SQL Analysis

SQL was used to perform production aggregation and summarize well-level production behavior.

The project includes SQL queries for:

- Total oil, gas, and water production by wellbore
- Yearly production trends by wellbore
- Well-level production comparison

The SQL queries are stored in:

    sql/

The output tables are saved in:

    reports/sql_results/

Using SQL in this project helps demonstrate how production data can be queried and summarized in a structured way, similar to how engineering teams work with production databases.

## 5. Decline Curve Analysis Methodology

Decline curve analysis is a common petroleum engineering method used to study production decline over time and estimate production behavior after peak production.

This project uses the exponential decline model:

    q(t) = qi * exp(-D * t)

Where:

- q(t) is oil production at time t
- qi is the estimated initial production rate
- D is the decline rate
- t is time in months

For each selected wellbore, the analysis follows these steps:

1. Filter wellbores with positive oil production
2. Select the top oil-producing wells
3. Identify the peak oil production month
4. Use the post-peak production period for decline fitting
5. Apply logarithmic transformation to oil production
6. Fit a linear regression on log-transformed production
7. Estimate monthly decline rate
8. Convert monthly decline rate into annual decline percentage
9. Compare actual oil production with the fitted decline curve

The fitted curve is then visualized against actual oil production to evaluate how well the exponential model represents the decline behavior.

## 6. Outputs

The project produces the following outputs:

### Cleaned Dataset

    data/processed/volve_monthly_production_clean.csv

### Decline Curve Results

    reports/decline_curve_results.csv

This file includes:

- Wellbore name
- Estimated initial production rate
- Monthly decline rate
- Annual decline percentage
- R² value
- Number of months used in the analysis

### Visualizations

Decline curve plots are saved in:

    reports/figures/

Each plot shows:

- Actual oil production
- Exponential decline curve fit
- Production behavior over time

## 7. Interpretation

The decline curve results help compare production behavior across different wellbores. Wells with higher annual decline percentages show faster production decrease after peak output, while wells with lower decline percentages show more stable production behavior.

The R² value provides a simple measure of how well the exponential decline model fits the actual production data. A higher R² indicates that the exponential model explains the production decline more closely. However, a lower R² may indicate operational interruptions, changing production conditions, reservoir complexity, or limitations of the simple exponential decline model.

## 8. Engineering Relevance

This project is relevant to petroleum engineering because it connects production data analysis with practical reservoir and production engineering concepts.

It demonstrates:

- Well-level production performance analysis
- Oil production decline interpretation
- Basic forecasting logic
- Production data cleaning and structuring
- SQL-based production summaries
- Technical documentation of engineering results

Although the model is simple, the workflow reflects a realistic first step in petroleum production analytics.

## 9. Limitations

This project is a portfolio-level analysis and has several limitations:

- The decline model is simplified and uses only exponential decline
- Operational constraints are not fully considered
- Reservoir pressure data is not included in the model
- Well interventions, shut-ins, and production strategy changes may affect decline behavior
- The analysis does not replace full reservoir simulation or professional production forecasting

Future improvements could include:

- Comparing exponential, hyperbolic, and harmonic decline models
- Adding production rate normalization by on-stream hours
- Detecting shut-in periods and removing outliers
- Building well-level dashboards
- Adding cumulative production analysis
- Estimating EUR using decline curve assumptions

## 10. Conclusion

This project shows how real petroleum production data can be used to perform well-level decline curve analysis. The workflow includes data cleaning, SQL-based aggregation, decline model fitting, visualization, and technical reporting.

The project demonstrates practical skills in petroleum production analytics, Python programming, SQL querying, data visualization, and engineering interpretation.
