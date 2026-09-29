from modules.filemanager import load, save
from utils.valid import req, phone, bg, pos
from datetime import datetime

hf = "hospitals.dat"
rf = "requests.dat"

class Hos:
    def __init__(self):
        self.hos = load(hf)
        self.reqst = load(rf)

    def save(self):
        save(hf, self.hos)
        save(rf, self.reqst)

    def allhos(self):
        return self.hos

    def allreq(self):
        return self.reqst

    def add(self):
        hid = str(pos("Hospital ID: "))

        if any(x["hid"] == hid for x in self.hos):
            print("Hospital ID already exists.")
            return

        self.hos.append({
            "hid": hid,
            "name": req("Hospital name: "),
            "add": req("Address: "),
            "ph": phone()
        })

        self.save()
        print("Hospital added successfully.")

    def req(self, inv):
        hid = input("Hospital ID: ").strip()

        if not any(x["hid"] == hid for x in self.hos):
            print("Hospital not found.")
            return

        b = bg()
        n = pos("Units requested: ")

        rid = "R" + str(len(self.reqst) + 1).zfill(3)

        self.reqst.append({
            "rid": rid,
            "hid": hid,
            "bg": b,
            "units": n,
            "status": "Pending",
            "dt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        self.save()
        print("Request", rid, "created successfully.")

    def upreq(self):
        rid = input("Request ID: ").strip()
        r = next((x for x in self.reqst if x["rid"] == rid), None)

        if not r:
            print("Request not found.")
            return

        st = input(
            "Status (Pending/Approved/Rejected/Fulfilled): "
        ).strip().title()

        if st not in ["Pending", "Approved", "Rejected", "Fulfilled"]:
            print("Invalid status.")
            return

        r["status"] = st
        self.save()
        print("Request updated successfully.")
