# Log Analysis Report
Third project of FSND from Udacity.
This tool print Logs from Database

## To Run

### You will need:
- Python3
- Vagrant
- VirtualBox

### Setup
1. Install Vagrant And VirtualBox
2. Clone this repository

### To Run

Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

The database includes three tables:
- Authors table
- Articles table
- Log table

### How to Create the Views
This project uses views that were created in the database and are referenced in `news.py`. For the program to work correctly, these views must be created in the `news` database.
1) To create the view `popular_articles`:
```sql
create view popular_articles as
select articles.title, count(log.path) as views
from log, articles
where log.status = '200 OK' and log.path like concat('%', articles.slug)
group by log.path, articles.title
order by views desc limit 3;
```

2) To create the view `authors_popular`:
```sql
create view authors_popular as
select authors.name, count(articles.author) as views
from log, articles, authors
where log.status = '200 OK' and log.path like concat('%', articles.slug) and articles.author=authors.id
group by articles.author, authors.name
order by views desc;
```

3) To create the view `load_error_dayss`:
```sql
create view load_error_days as

select * from

(select to_char(ers.data, 'Mon DD, YYYY') as data, ers.erros::decimal / oks.validos * 100 as porcentagem from

(select date(log.time) as data, count(date(log.time)) as erros
from log
where log.status != '200 OK'
group by date(log.time)
order by erros desc ) as ers,

(select date(log.time) as data, count(date(log.time)) as validos
from log where log.status = '200 OK'
group by date(log.time)
order by validos desc ) as oks

where ers.data = oks.data

order by porcentagem desc) as consulta

where porcentagem > 1;
```
## Execute Program
To execute the program, run `python news.py` from the command line, Then it will generate a file `Log.txt` with the results.
