# Student Registration System
import requests
import json


class Student:
    id = None

    def __init__(self, full_name, age, level, mobile_number):
        self.full_name = full_name
        self.age = age
        self.level = level
        self.mobile_number = mobile_number
        self.id = Student.id


while True:
    print("(1) New Students\n(2) Edit Student\n(3) Delete Student\n(4) Get Students\n(5) Get Student's Details\n(6)Exit")
    action = input("enter action")
    if action == "1":
        full_name = input("enter full name")
        age = input("enter age")
        level = input("level")
        if not level.capitalize() in ["A", "B", "C"]:
            print("PLease choose level from (A, B, C)")
            level = input("enter level")
        mobile_number = input("mobile number")
        data = {
            "full_name": full_name,
            "age": age,
            "level": level,
            "mobile_number": mobile_number
        }
        requests.post("http://staging.bldt.ca/api/method/build_it.test.register_student", data)

    elif action == "2":
        id = input("enter id")
        full_name = input("enter full name")
        age = input("enter age")
        level = input("level")
        if not level.capitalize() in ["A", "B", "C"]:
            print("PLease choose level from (A, B, C)")
            level = input("enter level")
        mobile_number = input("mobile number")

        data = {
            "id": id,
            "full_name": full_name,
            "age": age,
            "level": level,
            "mobile_number": mobile_number
        }
        requests.put("http://staging.bldt.ca/api/method/build_it.test.edit_student", data)

    elif action == "3":
        std_id = input("enter student id")
        response = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_student_details",
                                params={"id": std_id})
        response = response.text
        response = json.loads(response)
        if not response['status']:
            print("There is no student with given id")
            continue
        else:
            requests.delete("http://staging.bldt.ca/api/method/build_it.test.delete_student", params={"id": std_id})

    elif action == "4":
        response = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_students")
        data = response.text
        data = json.loads(data)

        for std in data['data']:
            f = open("students.txt", "a")
            f.write(str(std) + "\n")
            f.close()

    elif action == "5":
        std_id = input("enter std id")
        params = {
            "id": std_id
        }
        response = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_student_details", params)
        data = response.text
        data = json.loads(data)
        f = open("std_details.txt", "a")
        f.write(str(data['data']))
        f.close()

    elif action == "6":
        print("Have a Nice Day!")
        break

    else:
        print("please choose action from 1-6")