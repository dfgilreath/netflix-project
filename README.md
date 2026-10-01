Netflix Cultural Impact

An analytics project exploring the relationship between Netflix viewing popularity and broader public interest.

Research Question

When a title becomes popular on Netflix, does broader public interest move with it?

The project will use Netflix Top 10 viewing data as the primary signal of streaming popularity and eventually compare it with external indicators of public interest, such as Google Trends and other publicly available data.

Project Goals
Build a reproducible Python data pipeline for Netflix Top 10 data
Analyze title-level viewing patterns over time
Explore geographic differences in Netflix popularity
Identify titles and events that show notable changes in viewing popularity
Compare Netflix viewing signals with broader measures of public interest
Develop an interactive analytical experience around the findings
Data

The project uses Netflix's publicly available Top 10 datasets:

Global weekly Top 10 data
Country-level weekly Top 10 data

The raw source files are intentionally excluded from this repository because they are large and periodically updated.

Current Progress

Load Netflix Top 10 global data with Python

Load Netflix Top 10 country data with Python

Profile dataset structure

Check for duplicate records

Check for missing values

Clean and validate data

Develop title-level metrics

Analyze geographic patterns

Integrate external public-interest data

Develop visualizations

Create final interactive analysis

Project Structure
netflix_project/
├── data/
│   └── raw/
├── src/
│   └── inspect_data.py
├── .gitignore
└── README.md
Tools
Python
Pandas
Git / GitHub
Data visualization tools to be added as the project develops
Status

Early development. The current focus is building and validating the Netflix data pipeline before beginning the broader cultural-impact analysis.