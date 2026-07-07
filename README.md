# Career Stability Analyzer

A small data analysis project that looks at real employment data to figure out which college majors are actually stable career choices.

## What it does

Fetches employment data from FiveThirtyEight (the same people who do the polls), cleans it up, and calculates a "Stability Score" for each major based on median salary and unemployment rate. Then categorizes them as Volatile, Stable, or Highly Secure.

## How the score works

- 60% weight on median salary (higher is better)
- 40% weight on unemployment rate (lower is better)
- Scores range from 0 to 100

## Run it

```
pip install pandas numpy
python main.py
```

It fetches fresh data from the internet automatically, so you need an internet connection for the first run.

## Project structure

- main.py - runs everything
- generate_data.py - downloads the dataset from FiveThirtyEight
- analyzer.py - does the actual analysis (cleaning, scoring, categorizing)

## What I learned

- Working with real-world messy data (missing values, different formats)
- Grouping and aggregating data with Pandas
- Building a simple scoring system from scratch
- How to interpret unemployment and salary stats

## Stack

Pandas, NumPy, FiveThirtyEight dataset
