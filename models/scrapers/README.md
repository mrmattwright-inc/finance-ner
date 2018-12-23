Requirements:

```
pip install scrapy
```

Prerequisites:

Code currently missing. The scrape process requires an input file called 'items.json' (an array of objects). It is expecting each object to contain a populated entry called 'link' and the value is an individual investopedia page (eg `https://www.investopedia.com/terms/c/cdo2.asp`).

The missing code needs to start with the glossary root page of each letter of the alphabet:

```
https://www.investopedia.com/terms/1/
https://www.investopedia.com/terms/a/
https://www.investopedia.com/terms/b/
```

etc and scrape the page for all term links. It then needs to paginate through all available pages.

Once 'items.json' has been prepared, execute: 

```
scrapy crawl investopedia
```

to instigate the scrape.
