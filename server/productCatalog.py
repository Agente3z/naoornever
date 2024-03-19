import copy

class prodRecord :
    name="",
    weight="",
    cost="",
    dim="",
    photo="",
    link=""

    def to_dict(self):
        return {
            "name": self.name,
            "weight": self.weight,
            "cost": self.cost,
            "dim": self.dim,
            "photo": self.photo,
            "link": self.link
        }

allrecords = []

lampCatalogString = ""
sofaCatalogString = ""
tableCatalogString = ""
chairCatalogString = ""

with open("database.csv") as csvfile:
    for row in csvfile:
        s = row.split(";")

        r = prodRecord()
        r.name = s[1]
        r.weight = s[3]
        r.cost = s[4]
        r.dim = s[5]
        r.photo = s[8]
        r.link = s[9]

        allrecords.append(copy.deepcopy(r))

        if s[18] == "illuminazione":
            lampCatalogString += s[0]+";"+s[1]+";"+s[2]+";"+s[11]+";\n"
        elif s[18] == "poltrone" or s[18] == "pouf":
            sofaCatalogString += s[0]+";"+s[1]+";"+s[2]+";"+s[11]+";\n"
        elif s[18] == "tavoli" or s[18] == "tavolini":
            sofaCatalogString += s[0]+";"+s[1]+";"+s[2]+";"+s[11]+";\n"
        elif s[18] == "sedute":
            chairCatalogString += s[0]+";"+s[1]+";"+s[2]+";"+s[11]+";\n"
