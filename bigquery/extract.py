from google.cloud import bigquery
import os


def read_from_bigquery(sql_query):
    client = bigquery.Client()
    query = client.query(sql_query)
    return [row for row in query.result()]

project_id = 'project-428209'
sql_query = f'SELECT * FROM {project_id}.project_zola.my_table LIMIT 100'
data = read_from_bigquery(sql_query)
for row in data:
    print(row)