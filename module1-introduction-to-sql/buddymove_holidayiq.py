''' py file to create a sql database from csv + explorations '''

import pandas as pd
import sqlite3
df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
conn
curs = conn.cursor()
curs 
df.to_sql('buddymove_holidayiq', con=conn)

df.info()
df.columns

# Count how many rows you have - it should be 249!
total_rows = '''
SELECT COUNT(*)
FROM buddymove_holidayiq
'''

# How many users who reviewed at least 100 Nature in the 
# category also reviewed at least 100 in the Shopping category?
user100 = '''
SELECT COUNT(*)
FROM buddymove_holidayiq
WHERE Nature > 100 and Shopping > 100
'''
# What are the average number of reviews for each category?
cat_average = '''
SELECT AVG(Sports)
FROM buddymove_holidayiq
'''