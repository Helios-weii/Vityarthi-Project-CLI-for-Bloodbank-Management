from modules.donor import Donor
from modules.inventory import Inv
from modules.hospital import Hos
from modules.search import Search
from modules.report import Report
from utils.display import head, menu, pause, show

dnr = Donor()
inv = Inv()
hos = Hos()
sea = Search(dnr, inv)
rep = Report(dnr, inv, hos)

def dmenu():
    while True:
        head("DONOR MANAGEMENT")
        ch = menu([
            "Add donor", "Show donors", "Search donor",
            "Update donor", "Delete donor", "Back"
        ])
        if ch == "1":
            dnr.add()
        elif ch == "2":
            show(dnr.all())
        elif ch == "3":
            sea.donor()
        elif ch == "4":
            dnr.update()
        elif ch == "5":
            dnr.delete()
        else:
            return
        pause()

def imenu():
    while True:
        head("BLOOD INVENTORY")
        ch = menu([
            "Add blood", "Issue blood", "Check stock",
            "Show inventory", "Back"
        ])
        if ch == "1":
            inv.add()
        elif ch == "2":
            inv.issue()
        elif ch == "3":
            inv.check()
        elif ch == "4":
            show(inv.all())
        else:
            return
        pause()

def hmenu():
    while True:
        head("HOSPITAL AND REQUESTS")
        ch = menu([
            "Register hospital", "Show hospitals",
            "Create request", "Show requests",
            "Update request", "Back"
        ])
        if ch == "1":
            hos.add()
        elif ch == "2":
            show(hos.allhos())
        elif ch == "3":
            hos.req(inv)
        elif ch == "4":
            show(hos.allreq())
        elif ch == "5":
            hos.upreq()
        else:
            return
        pause()

def smenu():
    while True:
        head("SEARCH")
        ch = menu([
            "Search by donor ID", "Search by name",
            "Search by blood group", "Search inventory", "Back"
        ])
        if ch == "1":
            show(sea.byid(input("Donor ID: ").strip()))
        elif ch == "2":
            show(sea.byname(input("Name: ").strip()))
        elif ch == "3":
            show(sea.bgrp(input("Blood group: ").strip()))
        elif ch == "4":
            show(sea.ibgrp(input("Blood group: ").strip()))
        else:
            return
        pause()

def main():
    while True:
        head("BLOOD BANK MANAGEMENT SYSTEM")
        ch = menu([
            "Donor Management",
            "Blood Inventory",
            "Hospital and Requests",
            "Search",
            "Reports",
            "Exit"
        ])
        if ch == "1":
            dmenu()
        elif ch == "2":
            imenu()
        elif ch == "3":
            hmenu()
        elif ch == "4":
            smenu()
        elif ch == "5":
            head("REPORT")
            print(rep.summary())
            pause()
        else:
            print("\nThank you for using the system.")
            break

if __name__ == "__main__":
    main()
