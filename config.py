TOKEN = ''


import psycopg2

con = psycopg2.connect(
  database="moreauth", 
  user="postgres", 
  password="12345678",
  host="localhost", 
  port="5432"
)

