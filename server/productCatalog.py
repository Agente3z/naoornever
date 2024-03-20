#!/usr/bin/env python3

# Product database importing script

# Imports
import copy

# Product class
class prodRecord :
    name="",
    weight="",
    cost="",
    dim="",
    photo="",
    link=""

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
