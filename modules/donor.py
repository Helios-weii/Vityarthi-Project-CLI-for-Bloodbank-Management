from modules.filemanager import load, save
from utils.valid import req, pos, phone, bg

fn = "donors.dat"

class Donor:
    def __init__(self):
        self.rec = load(fn)

    def save(self):
        save(fn, self.rec)

    def all(self):
        return self.rec

    def add(self):
        did = str(pos("Donor ID: "))
        if any(x["did"] == did for x in self.rec):
            print("Donor ID already exists.")
            return

        d = {
            "did": did,
            "name": req("Name: "),
            "add": req("Address: "),
            "ph": phone(),
            "bg": bg(),
            "gen": req("Gender: "),
            "dob": req("Date of birth: "),
            "ld": req("Last donation date: "),
            "mh": req("Medical history: ")
        }

        self.rec.append(d)
        self.save()
        print("Donor added successfully.")

    def update(self):
        did = input("Donor ID to update: ").strip()
        d = next((x for x in self.rec if x["did"] == did), None)

        if not d:
            print("Donor not found.")
            return

        d["name"] = req("New name: ")
        d["add"] = req("New address: ")
        d["ph"] = phone("New phone: ")
        d["bg"] = bg("New blood group: ")
        d["gen"] = req("New gender: ")
        d["dob"] = req("New date of birth: ")
        d["ld"] = req("New last donation date: ")
        d["mh"] = req("New medical history: ")

        self.save()
        print("Donor updated successfully.")

    def delete(self):
        did = input("Donor ID to delete: ").strip()
        old = len(self.rec)
        self.rec = [x for x in self.rec if x["did"] != did]

        if len(self.rec) == old:
            print("Donor not found.")
            return

        self.save()
        print("Donor deleted successfully.")
