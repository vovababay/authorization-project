TOKEN = '1459605967:AAGC7XKJJOGMrHjR-Yjl38Wm4T2N5PKpwLI'


import psycopg2

con = psycopg2.connect(
  database="moreauth", 
  user="postgres", 
  password="2932065", 
  host="localhost", 
  port="5432"
)

