# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
import requests
import re

with open('target.txt') as f:
    lines = f.readlines()
with open('results.txt', 'w', encoding="utf-8") as f:
    for x in lines:
        theURL="https://en.wikipedia.org/"+x.strip()
        page = requests.get(theURL)
        soup = BeautifulSoup(page.content, 'html.parser')
        list(soup.children)
        #description:
        if soup.find_all('p') == None:
            continue
        description = soup.find_all('p')[0].get_text()
        #name:
        if soup.find_all('b') == None:
            continue
        name = soup.find_all('b')[0].get_text()
        #coordinates:
        if soup.find_all('script') == None:
            continue
        script = soup.find_all('script')[0].get_text()
        
        result = re.search('lat\":(.*),\"lon\":', script)
        if result == None:
            continue
        lat = result.group(1)
        
        result2 = re.search('lon\":(.*)},\"wgEditSubmit', script)
        if result2==None:
            result2 = re.search('lon\":(.*)},\n\"wgEditSubmit', script)
            if result2==None:
                continue

        lon = result2.group(1)    
        
        newline = "  {  \"type\": \"Feature\",  \"properties\": {  \"_storage_options\": {  \"color\": \"Red\",  \"iconClass\": \"Circle\"  },  \"name\": \""+name+"\""+",\"description\": \"Montenegrin\",  \"_umap_options\": {  \"color\": \"DarkRed\",  \"iconClass\": \"Circle\"  }  },  \"geometry\": {  \"type\": \"Point\",  \"coordinates\": [  "+lon +"," +  lat+ "  ]  }  },"
        f.write(newline)
        f.write("\n")

print("done")