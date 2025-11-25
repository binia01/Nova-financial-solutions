# Nova-financial-solutions

A project to analyze the correlation between financial news sentiment and stock price movements. It leverages NLP for sentiment analysis and statistical methods for correlation to surface actionable insights for investment strategies. This repository contains code, notebooks, and documentation for the analysis.

## Key Features

- **Modular & Reusable Code:** All logic is organized into a clean `src` package, promoting maintainability, testability, and reusability.
- **Data Ingestion & Preparation:** Loads and prepares historical stock price data and raw news data from source files.
- **Sentiment Analysis:** Implements sentiment scoring for over a million news headlines using `TextBlob`.
- **Technical Analysis:** Automatically calculates key technical indicators for multiple stocks, including Simple Moving Averages (SMA), Relative Strength Index (RSI), and MACD using `TA-Lib`.
- **Correlation Analysis:** Merges sentiment and stock data, calculates daily returns, and computes a full correlation matrix to uncover relationships.


## Task 1 — Environment setup & Exploratory Data Analysis (EDA)
The first phase focuses on:
- Environment setup: create a reproducible Python environment with version control.
- Exploratory Data Analysis (EDA): initial investigation of the financial news dataset to understand structure, characteristics, and preliminary insights.

## Task 2: Quantitative Analysis using PyNance and TA-Lib
The second phase focuses on: 
- Integrating external stock price data and calculating essential technical indicators. 
- Activities: Loading OHLCV data, calculating indicators like Moving Averages (MA), Relative Strength Index (RSI), and MACD using TA-Lib, and visualizing the data.

## Task 3: Correlation between News and Stock Movement
The third phase focuses on:
- The core correlation analysis required by the business objective. 
- Activities: Date alignment and normalization, conducting sentiment analysis on headlines using libraries like nltk and TextBlob, calculating daily stock returns, aggregating daily sentiment scores, and determining the Pearson correlation coefficient between sentiment and returns.

## Getting started

### Prerequisites
- Git
- Python 3.8+

### Clone the repository
```bash
git clone https://github.com/binia01/Nova-financial-solutions.git
cd nova-financial-solutions
```

### Create and activate a virtual environment

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

For macOS / Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Key findings from the EDA
1. Headline characteristics
    - Headlines are generally concise. Average length: TODO (e.g., ~65 characters).
    - Distribution is slightly right-skewed (most headlines are short; a few are long/descriptive).

2. Publisher activity
    - A small number of publishers dominate the dataset. Top publishers (examples):
      - Paul Quintaro
      - Lisa Levin
      - Benzinga Newsdesk
      - Charles Gross
      - Monica Gerson
    - This suggests most content originates from a few major newswires.

3. Temporal patterns
    - Publication volume follows a weekly cycle (peak on Tuesday, Wednesday and Friday, drop on Monday, Thursday and weekends).

4. Content Themes
   - A preliminary analysis of word frequency in headlines shows that the most common terms include "stock", "market", "company", "shares", "price", and "target", which is consistent with the financial nature of the dataset.

## Next steps
- Quantitative analysis using pynance and TaLib
- Integrate with stock price data for correlation and time-series analysis.
