#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import time


DBNAME = "news"


def popular_articles():
    """Shows the three most popular articles!"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from popular_articles")
    articles = c.fetchall()

    text = "What are the most popular three articles of all time:\n"
    for i in articles:
        text += "%-35s -- %-10s views\n" % (i[0], i[1])
    text += "\n\n"
    return text


def authors_popular():
    """Shows the authors of most popular articles of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from authors_popular")
    autores = c.fetchall()

    text = "Who are the most popular article authors of all time:\n"
    for i in autores:
        text += "%-35s -- %-10s views\n" % (i[0], i[1])
    text += "\n\n"
    return text


def load_error_days():
    """Show which days did more than 1% of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select * from load_error_days")
    dias = c.fetchall()

    text = "On which days did more than 1% of requests lead to errors:\n"
    for i in dias:
        text += "%-35s -- %-10.4s%s erros\n" % (i[0], i[1], '%')
    text += "\n\n"
    return text


def main():
    """Write the text on the log file."""
    db = psycopg2.connect(database=DBNAME)

    print("Writing Log...\n")
    relatorio = open("Log.txt", "w")

    relatorio.write("Log Analysis Report - Written: " +
                    time.ctime() + "\n\n")
    relatorio.write(popular_articles())
    relatorio.write(authors_popular())
    relatorio.write(load_error_days())

    relatorio.close()
    print("Analysis is done! See the file log.txt")

    db.close()


if __name__ == "__main__":
    main()
