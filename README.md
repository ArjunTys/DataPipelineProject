# News ETL Data Pipeline

An automated ETL pipeline that extracts real-time news articles from the News API, transforms the raw JSON into structured data, loads it into SQLite, and orchestrates the workflow using Apache Airflow.

## Project Structure
news-etl-pipeline/
├── dags/
│   └── news_pipeline_dag.py   # Airflow DAG
├── etl/
│   ├── extract.py             # Fetch from News API
│   ├── transform.py           # Clean and normalize
│   └── load.py                # Load into SQLite
├── utils/
│   └── config.py              # Environment variables
├── data/
│   └── news.db                # SQLite database (auto-created)
├── .env                       # API key (not committed)
└── requirements.txt

## Setup

**1. Clone and activate environment**
```bash
git clone https://github.com/your-username/news-etl-pipeline.git
cd news-etl-pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**2. Add your API key**

Get a free key at [newsapi.org](https://newsapi.org) and create a `.env` file:

**3. Run the pipeline**
```bash
python3 -c "
from etl.extract import fetch_news
from etl.transform import transform
from etl.load import load

raw_json = fetch_news('technology')
df = transform(raw_json)
load(df)
print(f'Done. Rows loaded: {len(df)}')
"
```

## Airflow Orchestration

The pipeline is defined as an Airflow DAG with daily scheduling and XCom-based task communication. See setup instructions for configuring Airflow with PostgreSQL as the metadata backend.

