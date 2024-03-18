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

aiCatalogString = ""

with open("db.csv") as csvfile:
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

        aiCatalogString += s[0]+";"+s[1]+";"+s[2]+";"+s[11]+";\n"