class Report:
    def __init__(self, dnr, inv, hos):
        self.dnr = dnr
        self.inv = inv
        self.hos = hos

    def summary(self):
        ds = self.dnr.all()
        ins = self.inv.all()
        hs = self.hos.allhos()
        rs = self.hos.allreq()

        total = sum(x["units"] for x in ins)
        pend = sum(1 for x in rs if x["status"] == "Pending")

        cnt = {}
        for x in ds:
            b = x["bg"]
            cnt[b] = cnt.get(b, 0) + 1

        s = [
            "BLOOD BANK SUMMARY",
            "-" * 35,
            "Total donors: " + str(len(ds)),
            "Total hospitals: " + str(len(hs)),
            "Total blood units: " + str(total),
            "Total requests: " + str(len(rs)),
            "Pending requests: " + str(pend),
            "",
            "Donors by blood group:"
        ]

        for b in sorted(cnt):
            s.append(b + ": " + str(cnt[b]))

        return "\n".join(s)
