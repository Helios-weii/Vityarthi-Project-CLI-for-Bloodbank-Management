def head(title):
    print("\n" + "=" * 55)
    print(title.center(55))
    print("=" * 55)

def menu(opts):
    for i, x in enumerate(opts, 1):
        print(str(i) + ". " + x)

    while True:
        ch = input("Choose: ").strip()
        if ch.isdigit() and 1 <= int(ch) <= len(opts):
            return ch
        print("Invalid choice.")

def pause():
    input("\nPress Enter to continue...")

def show(rec):
    if not rec:
        print("No records found.")
        return

    for i, x in enumerate(rec, 1):
        print("\n--- Record " + str(i) + " ---")
        for k, v in x.items():
            print(k + ": " + str(v))
