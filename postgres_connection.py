import psycopg2
conn = psycopg2.connect(database="django_project", user="postgres", password="Datha@123", host="127.0.0.1", port="5432")
print(conn)