Damn Small SQLi Scanner 
```
$ python3 dsss.py -h
Damn Small SQLi Scanner (DSSS) < 100 LoC (Lines of Code)

Usage: dsss.py [options]

Options:
  --version          show program's version number and exit
  -h, --help         show this help message and exit
  -u URL, --url=URL  Target URL (e.g. "http://www.target.com/page.php?id=1")
  --data=DATA        POST data (e.g. "query=test")
  --cookie=COOKIE    HTTP Cookie header value
  --user-agent=UA    HTTP User-Agent header value
  --referer=REFERER  HTTP Referer header value
  --proxy=PROXY      HTTP proxy address (e.g. "http://127.0.0.1:8080")
```

```
$ python3 dsss.py -u "http://testphp.vulnweb.com/artists.php?artist=1"
