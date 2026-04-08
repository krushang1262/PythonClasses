import json

time = [10, 11, 12, 2, 3]
file_path = 'D:/Python Practice/Assesment/HealthCare.json'

# 🔹 Load existing data
try:
    with open(file_path, "r") as f:
        db = json.load(f)
except:
    db = {}

ch = 'yes'

while ch != 'no':
    choice = int(input("""
1: Booking appointment
2: Cancel appointment
3: View appointment
"""))

    # ---------------- BOOK ----------------
    if choice == 1:
        print("*** Booking appointment ***")

        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        phone = input("Enter Your Phone: ")
        dr = input("Enter Doctor Name: ")
        slot = int(input(f"Enter Slot {time}: "))

        if slot not in time:
            print(" Invalid slot")
            continue

        # 🔹 Count same doctor + slot bookings
        count = 0
        for record in db.values():
            if record["dr"] == dr and record["slot"] == slot:
                count += 1

        if count >= 3:
            print("Slot Full for this doctor")
        else:
            db[phone] = {
                "name": name,
                "age": age,
                "dr": dr,
                "slot": slot
            }

            with open(file_path, "w") as f:
                json.dump(db, f, indent=4)

            print("✅ Appointment Booked")

    # ---------------- CANCEL ----------------
    elif choice == 2:
        print("*** Cancel appointment ***")
        phone = input("Enter Your Phone: ")

        if phone in db:
            db.pop(phone)

            with open(file_path, "w") as f:
                json.dump(db, f, indent=4)

            print("✅ Appointment Cancelled")
        else:
            print(" Appointment not found")

    # ---------------- VIEW ----------------
    elif choice == 3:
        print("*** View appointment ***")
        phone = input("Enter Your Phone: ")

        if phone in db:
            d = db[phone]
            print(f"""
Name  : {d['name']}
Age   : {d['age']}
Doctor: {d['dr']}
Slot  : {d['slot']}
""")
        else:
            print(" No appointment found")

    else:
        print("Invalid Choice")

    ch = input("Do you want to continue yes or no ? ").lower()