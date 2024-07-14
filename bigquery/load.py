from google.cloud import bigquery
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/root/.config/gcloud/application_default_credentials.json'

def write_to_bigquery(table_id, rows_to_insert):
    client = bigquery.Client(project='project-428209')
    table = client.get_table(table_id)
    errors = client.insert_rows_json(table, rows_to_insert)
    if errors:
        print('Encountered errors while inserting rows: {}'.format(errors))
    else:
        print('Successfully inserted data')

table_id = 'project-428209.project_zola.my_table'
rows_to_insert = [
    {"id": 1, "name": 'Phred Phlyntstone', "created_at": '2023-11-10 08:00:00'},
    {"id": 2, "name": 'Wylma Phlyntstone', "created_at": '2023-11-10 08:00:00'},
    {"id": 3, "name": 'Wylma', "created_at": '2023-11-10 10:00:00'},
    {"id": 4, "name": 'Phlyntstone', "created_at": '2023-11-10 11:00:00'},
    {"id": 5, "name": 'maPhlyn', "created_at": '2023-11-10 12:00:00'}
]

write_to_bigquery(table_id, rows_to_insert)
