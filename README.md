# Report tool for media company using python3, PostgreSQL and DB-API


## Getting Started

This  tool is dependent on a specific database that is basically comprised of
three tables. A log table, an articles table and an authors table.

To make things easier, I did create a view  that combined the authors,
articles and pageviews for easier reporting. That view is defined here:

create view aut_art_pv as select path, count (path) as pageviews, articles.title,
authors.name  from log, articles, authors where substring(log.path,10) = articles.slug
and articles.author = authors.id group by path, articles.title, authors.name order by count(*)

## Bugs and Issues

None

## Creator

This code was created by Talha F Basit. Contact below:

* https://twitter.com/talhafbasit
* https://github.com/talhafbasit

## Copyright and License

Code released under the [MIT](http://choosealicense.com/licenses/mit/#) license.
