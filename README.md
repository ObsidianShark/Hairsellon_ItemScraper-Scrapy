# Hairsellon Item Scraper



## Description

Hairsellon is a website where people can put parts of hair for sale, as well with the item information and previous care. With this spider its possible 
to crawl over all listed ads and compile its data for further analysis.

## Requirements

Python 3.10+


## Installation

To clone the repository, type the code below in a shell :

```bash
  git clone https://github.com/ObsidianShark/Hairsellon_ItemScraper-Scrapy.git  
```

To install dependencies, run the command bellow :

```bash
  pip install -r requirements.txt
```
Add your MongoDB address to settings.py

```bash
  MONGODB_SERVER = "localhost"
  MONGODB_PORT = 27017
  MONGODB_DB = "YOUR_DB"
  MONGODB_COLLECTION = "YOUR_COLLECTION"
```


## Usage


To crawl over all ads, run the command bellow:

```bash
  scrapy crawl hairsellon 
```




