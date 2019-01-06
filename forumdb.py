import psycopg2

DBNAME = "news"

QUE1 = "1. What are the most popular three articles of all time?"
QUE2 = "2. Who are the most popular article authors of all time?"
QUE3 = "3. On which days did more than 1% of requests lead to errors?"

QUERY1 = "select articles.slug as atitle, count(*) as numb from log, articles where articles.slug = substr(log.path, 10) group by atitle order by numb desc limit 3;"
QUERY2 = "select authors.name as name , sum(numb) as articleViews from authors, articalOrder, articles where atitle = articles.slug and author=authors.id group by authors.name order by articleViews desc;"
QUERY3 = "select reqData.date, (errorcount*100.0/reqcount) as errorPercent from errorData, reqData where reqcount * 0.01 < errorcount and reqData.date = errorData.date order by errorPercent desc ;"

query1_result = dict()
query2_result = dict()
query3_result = dict()


def execute_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
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


query1_result['output'] = execute_query(QUERY1)
print_query12_results(query1_result, QUE1)

query2_result['output'] = execute_query(QUERY2)
print_query12_results(query2_result, QUE2)

query3_result['output'] = execute_query(QUERY3)
print_query3_results(query3_result, QUE3)
