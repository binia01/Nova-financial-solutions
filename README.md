# Nova-financial-solutions

A project to analyze the correlation between financial news sentiment and stock price movements. It leverages NLP for sentiment analysis and statistical methods for correlation to surface actionable insights for investment strategies. This repository contains code, notebooks, and documentation for the analysis.

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