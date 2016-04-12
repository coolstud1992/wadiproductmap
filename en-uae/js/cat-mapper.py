import os
import csv
import requests
from unidecode import unidecode
from bs4 import BeautifulSoup
import math
import demjson


with open('wadi_cat_Scrape.csv') as wadi_cat:
	reader=csv.DictReader(wadi_cat, delimiter=";")
	for row in reader:
		print(row['category'])
