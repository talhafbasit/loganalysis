# simple python tool to extract some log and article data
# from a media companies db

import psycopg2

DBNAME = "news"


def connect():
    # Connect to the PostgreSQL database.  Returns a database connection.
    # print("connected to postgres datbase: ", DBNAME)
    return psycopg2.connect(dbname=DBNAME)


def articleCount():
    sql = "select count (path) as pageviews, articles.title  from \
    log, articles where substring(log.path,10) = articles.slug  \
    group by path, articles.title order by count(*) desc limit 3;"
    db = connect()
    cursor = db.cursor()
    cursor.execute(sql)

    print("The top 3 articles based on pageviews are as follows:\n")
    for row in cursor.fetchall():
        articles = row
        print("There were {} views of the article - {}".format(articles[0],
                                                               articles[1]))

    print("\n")
    cursor.close()
    db.close()


def authors():
    sql = "select name as author, SUM(pageviews) as total_pageview from \
            aut_art_pv group by name order by total_pageview desc;"
    db = connect()
    cursor = db.cursor()
    cursor.execute(sql)

    print("The most popular authors of all time are as follows:\n")
    for row in cursor.fetchall():
        author = row
        print("{} had {} total pageviews.".format(author[0], author[1]))

    print("\n")

    cursor.close()
    db.close()


def logResults():
        sql = "select date, \
        (100.00 * cast(good_status as decimal)/cast(all_status as decimal)) \
        as percent_good from  (select time::date as date,  count(status) \
        as all_status, sum((status='200 OK')::int) as good_status \
        from log group by date) as foo;"
        db = connect()
        cursor = db.cursor()
        cursor.execute(sql)

        print("On the following days, there were more than 1% errors\n")
        for row in cursor.fetchall():
            logs = row
            if logs[1] < 99.0:
                percentErrors = 100-logs[1]
                percentErrors = str(round(percentErrors, 2))
                print("Date: {} had {}% errors.".format(logs[0],
                                                        percentErrors))

        print("\n")

        cursor.close()
        db.close()


articleCount()
authors()
logResults()
