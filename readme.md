Web scraper for PDF files
---

A webscraper to download all files with a certain suffix found on a given website. 

Perfect to download lecture notes, excercise slides or whatever you need from the internet.

---
### Run

``python3 scra.py -url https://ocw.mit.edu/resources/res-ll-005-mathematics-of-big-data-and-machine-learning-january-iap-2020/lecture-notes/index.html -dir C:/home/course -suf pdf -inc exercise``

### Arguments

- `url`: Website url to download your files from
- `dir`: Directory to save files to. Default is current directory
- `suf`: File suffix to download. Default is pdf
- `inc`: Filename on the webpage needs to have this included to be downloaded.
