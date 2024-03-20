#!/usr/bin/env python3

# Product database importing script

# Imports
import copy
import json
import requests

# Product class
class prodRecord :
    name="",
    weight="",
    cost="",
    dim="",
    photo="",
    link=""

    def __init__(self, name, weight, cost, dim, photo, link) -> None:
        self.name=name
        self.weight=weight
        self.cost=cost
        self.dim=dim
        self.photo=photo
        self.link=link

    # Dict conversion for json packaging
    def to_dict(self):
        return {
            "name": self.name,
            "weight": self.weight,
            "cost": self.cost,
            "dim": self.dim,
            "photo": self.photo,
            "link": self.link
        }

# Product list
allrecords = []

# Strings for context creation
lampCatalogString = ""
sofaCatalogString = ""
tableCatalogString = ""
chairCatalogString = ""
fornitureCatalogString = ""

# Database retrival from API
with requests.get("http://127.0.0.1:5000/get") as response:
    for c in json.loads(response.content):

        if "illuminazione" in c["categoria"].lower():
            lampCatalogString += c["sottocategoria"] +"/"+ c["nome"] +"/"+ c["materiali"] +"/\n"
        elif "sedute comode" in c["categoria"].lower():
            sofaCatalogString += c["sottocategoria"] +"/"+ c["nome"] +"/"+ c["materiali"] +"/\n"
        elif "tavoli & tavolini" in c["categoria"].lower():
            tableCatalogString += c["sottocategoria"] +"/"+ c["nome"] +"/"+ c["materiali"] +"/\n"
        elif "sedute" in c["categoria"].lower():
            chairCatalogString += c["sottocategoria"] +"/"+ c["nome"] +"/"+ c["materiali"] +"/\n"
        elif "mobilio" in c["categoria"].lower():
            fornitureCatalogString += c["sottocategoria"] +"/"+ c["nome"] +"/"+ c["materiali"] +"/\n"
        else:
            continue

        r = prodRecord(c["nome"], c["peso"], c["prezzo"], c["dimensioni"], c["foto"], c["link"])
        allrecords.append(r)

"""
# DB File parsing 
with open("database.csv") as csvfile:
    for row in csvfile:
        s = row.split(";")

        # Record creation
        r = prodRecord()
        r.name = s[1]
        r.weight = s[3]
        r.cost = s[4]
        r.dim = s[5]
        r.photo = s[8]
        r.link = s[9]
        allrecords.append(copy.deepcopy(r))

        # Context strings
        if "illuminazione" in s[18].lower():
            lampCatalogString += s[0]+"/"+s[1]+"/"+s[2]+"/"+"\n"
        elif "comode" in s[18].lower() or "poltrone" in s[18] or "pouf" in s[18]:
            sofaCatalogString += s[0]+"/"+s[1]+"/"+s[2]+"/"+"\n"
        elif "tavoli" in s[18].lower() or "tavolini" in s[18]:
            tableCatalogString += s[0]+"/"+s[1]+"/"+s[2]+"/"+"\n"
        elif "sedute" in s[18].lower():
            chairCatalogString += s[0]+"/"+s[1]+"/"+s[2]+"/"+"\n"
"""