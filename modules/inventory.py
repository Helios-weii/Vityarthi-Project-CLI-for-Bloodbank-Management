from modules.filemanager import load, save
from utils.valid import bg, pos

fn = "inventory.dat"
groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

class Inv:
    def __init__(self):
        self.rec = load(fn)
        if not self.rec:
            self.rec = [{"bg": x, "units": 0} for x in groups]
            self.save()

    def save(self):
        save(fn, self.rec)

    def all(self):
        return self.rec

    def add(self):
        b = bg()
        n = pos("Units to add: ")
        x = next(x for x in self.rec if x["bg"] == b)
        x["units"] += n
        self.save()
        print(n, "units added to", b)

    def issue(self):
        b = bg()
        n = pos("Units to issue: ")
        x = next(x for x in self.rec if x["bg"] == b)

        if x["units"] < n:
            print("Not enough blood available.")
            return

        x["units"] -= n
        self.save()
        print(n, "units issued from", b)

    def check(self):
        b = bg()
        x = next(x for x in self.rec if x["bg"] == b)
        print(b, "available:", x["units"], "units")
