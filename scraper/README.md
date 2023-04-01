## About

A scraper used to scrape the prose section of the site valmiki-ramayana.net

## Scraper

1. `chapter-scraper.py`

For scraping only the chapters name and sarga for each kanda.
Example: For Ayodhya kanda, it will scrape all chapters available for this kanda
and store it as a json file inside `src/kanda/ayodhya/chapters.json`

2. `prose-scraper.py`

With #1 we get all the chapters for each kanda.
In #2 scraper, we loop through this chapters and hit the url for each chapter.
Inside it we scrape the prose for that chapter and store it as a json with the
chapter number as the file name.

`src/kanda/ayodhya/prose/chapter/<chapter_number>.json`
