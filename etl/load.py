import sqlite3

def load(df, db_path = 'data/news.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS news_articles (
    url TEXT PRIMARY KEY,
    title TEXT,
    author TEXT,
    description TEXT,
    url_to_image TEXT,
    published_at TEXT,
    content TEXT,
    source_name TEXT
)
""")
    df.to_sql('news_articles', conn, if_exists='append', index=False)
    conn.commit()
    conn.close()

