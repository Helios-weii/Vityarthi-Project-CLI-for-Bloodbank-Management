groups = {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}

def req(msg):
    while True:
        x = input(msg).strip()
        if x:
            return x
        print("This cannot be empty.")

def pos(msg):
    while True:
        try:
            x = int(input(msg).strip())
            if x > 0:
                return x
        except ValueError:
            pass
        print("Enter a positive number.")

def bg(msg="Blood group: "):
    while True:
        x = input(msg).strip().upper()
        if x in groups:
            return x
        print("Invalid blood group.")

def phone(msg="Phone: "):
    while True:
        x = input(msg).strip()
        if x.isdigit() and len(x) == 10:
            return x
        print("Enter a 10 digit phone number.")
