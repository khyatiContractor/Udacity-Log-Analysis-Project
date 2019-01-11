#!/usr/bin/env python

import psycopg2

DBNAME = "news"

QUE1 = "1. What are the most popular three articles of all time?"
QUE2 = "2. Who are the most popular article authors of all time?"
QUE3 = "3. On which days did more than 1% of requests lead to errors?"

QUERY1 = """
SELECT articles.slug AS atitle,
       count(*) AS numb
FROM log,
     articles
WHERE articles.slug = substr(log.path, 10)
GROUP BY atitle
ORDER BY numb DESC
LIMIT 3;
"""

QUERY2 = """
SELECT authors.name AS name,
       count(*) AS numb
FROM log,
     articles,
     authors
WHERE articles.slug = substr(log.path, 10)
GROUP BY atitle
ORDER BY numb DESC
LIMIT 3;
"""

QUERY3 = """
SELECT reqData.date,
       (errorcount*100.0/reqcount) AS errorPercent
FROM errorData,
     errorData
WHERE reqcount * 0.01 < errorcount
AND reqData.date = errorData.date
ORDER BY errorPercent DESC;
"""

query1_result = dict()
query2_result = dict()
query3_result = dict()


def connect(database_name):
    """
     Connect to the PostgreSQL database.
     Return a database connection.
    """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
    except psycopg2.Error as err:
        print("Unable to connect!")
        print(err)
        sys.exit(1)       # Then perhaps exit the program -- The easier method
    else:
        print("Connected!")
    cursor = db.cursor()
    return db, cursor
    """
                db, cursor : is a tuple.
                The first element (db) is a connection to the database.
                The second element (cursor) is a cursor for the database.
    """


def execute_query(query):
    db, C = connect(database_name=DBNAME)
    c.execute(query)
    votes = c.fetchall()
    db.close()
    return votes


def print_query12_results(query_result, que):
    print (que)
    for result in query_result['output']:
        print ('\t' + str(result[0]) + ' -- ' + str(result[1]) + ' views')


def print_query3_results(query_result, que):
    print (que)
    for result in query_result['output']:
        print ('\t' + str(result[0]) + ' -- ' + str(result[1]) + ' %  errors')


if __name__ == '__main__':
    query1_result['output'] = execute_query(QUERY1)
    print_query12_results(query1_result, QUE1)

    query2_result['output'] = execute_query(QUERY2)
    print_query12_results(query2_result, QUE2)

    query3_result['output'] = execute_query(QUERY3)
    print_query3_results(query3_result, QUE3)
else:
    print ('Importing ...')