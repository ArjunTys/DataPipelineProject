import pandas as pd

def transform(raw_json):
    data = raw_json['articles']
    df = pd.DataFrame(data)
    source_flat = pd.json_normalize(df['source'])
    df = df.drop(columns=['source']).join(source_flat)
    df.drop('id', axis = 1, inplace=True)
    df['description'].fillna('N/A', inplace= True)
    df['author'].fillna('unknown', inplace=True)
    df.rename(columns={"urlToImage": "url_to_image", "publishedAt":"published_at", 'name':'source_name'}, inplace=True)
    df['published_at'] = pd.to_datetime(df['published_at'])
    df['url_to_image'].fillna("No Image Available", inplace=True)
    return df
