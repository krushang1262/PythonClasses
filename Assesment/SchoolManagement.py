import json
forrecords = {}
data = {}
ch = 'yes'

while ch != 'no':
    choice = int(input("""
                1: New Admission
                2: View Students Details
                3: Update Student Info
                4: Remove Student Record
                """))

    if choice == 1:
        print("*** Enter the Student Details ***")
        
        studentId = 1
        studentNm = input("Enter Student Name: ")
        print("*** Enter the age between 5 to 18 ***")
        studentAge = int(input("Enter Student Age: "))
        print("*** Enter the class 1 to 12 ***")
        studentclass = int(input("Enter Student Class: "))
        print("*** Enter the mobile 10 digit ***")
        Mobile = input("Enter Student guardian's mobile number: ")
         
        if len(Mobile) != 10 or len(Mobile) > 10:
            print("Enter the Proper 10 digit Mobile Number. ")
            break
        
        if studentAge not in range(5,19):
            print(f"Invalid Age {studentAge}")
            break
        
        if studentclass in range(1,13):
            if studentclass > 12:
                print("Invalid Standard")
                break
            else:
                print("Admission Successfully")
                
            forrecords.update({"Id":studentId, "name":studentNm, "age":studentAge, "class":studentclass, "mobile":Mobile})
            
            try:
                with open('D:/Python Practice/Assesment/School.json', "r") as sr:
                    data = json.load(sr)
            except:
                forrecords = {}

            studentId = str(len(data) + 1)

            data[studentId] = {
                "name": studentNm,
                "age": studentAge,
                "class": studentclass,
                "mobile": Mobile
            }

            with open('D:/Python Practice/Assesment/School.json', "w") as sc:
                json.dump(data, sc, indent=4)
        else:
            print("Invalid class enter")            
        
    elif choice == 2:
        with open('D:/Python Practice/Assesment/School.json', "r") as reader:
            print(reader.readlines())
            
    elif choice == 3:
        print("*** Update the Student Details ***")

        try:
            with open('D:/Python Practice/Assesment/School.json', "r") as f:
                data = json.load(f)
        except:
            data = {}

        sid = input("Enter Student ID: ")

        if sid in data:
            print("1. Update Mobile")
            print("2. Update Class")
            ch2 = input("Enter choice: ")

            if ch2 == "1":
                mobile = input("Enter new mobile: ")
                if mobile.isdigit() and len(mobile) == 10:
                    data[sid]["mobile"] = mobile
                    print("Mobile Updated")
                else:
                    print("Invalid mobile")

            elif ch2 == "2":
                
                studentclass = int(input("Enter new class: "))
                if  studentclass in range(1,13):
                    data[sid]["class"] = studentclass
                    print(" Class Updated")
                else:
                    print("Invalid class")
            else:
                print("Invalid choice")

            with open('D:/Python Practice/Assesment/School.json', "w") as f:
                json.dump(data, f)
        else:
            print("Student not found")
                
    elif choice == 4:
        
        print("*** Delete the Student Details ***")
        
        with open('D:/Python Practice/Assesment/School.json',"r")as r:
            data = json.load(r)
            
            sid = input("Enter the Student Id: ")
            
            if sid in data:
                data.pop(sid)
                print("Student Record Delete")
                
                with open('D:/Python Practice/Assesment/School.json',"w")as w:
                    json.dump(data,w)
            else:
                print("Student Id not Found")
    
    ch = input("are you continue yes or no ? ").lower()