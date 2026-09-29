class Search:
    def __init__(self, dnr, inv):
        self.dnr = dnr
        self.inv = inv

    def donor(self):
        x = input("Search by ID or name: ").strip()
        a = self.byid(x)

        if not a:
            a = self.byname(x)

        from utils.display import show
        show(a)

    def byid(self, did):
        return [x for x in self.dnr.all() if x["did"] == did]

    def byname(self, name):
        name = name.lower()
        return [x for x in self.dnr.all() if name in x["name"].lower()]

    def bgrp(self, b):
        b = b.upper()
        return [x for x in self.dnr.all() if x["bg"].upper() == b]

    def ibgrp(self, b):
        b = b.upper()
        return [x for x in self.inv.all() if x["bg"].upper() == b]
