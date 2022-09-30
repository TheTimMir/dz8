class Student:
    def __init__(self, name="Ivan", age=18, groupNum="10A"):
        self.name = name
        self.groupNum = groupNum
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNum(self):
        return self.groupNum

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNum(self, grN):
        self.groupNum = grN


Dan = Student("Dan", 16, "11B")
Ann = Student("Ann", 14, "9A")
Ben = Student("Ben", 10, "5C")
Sam = Student("Sam", 9, "4A")
Eve = Student("Eve", 12, "7B")
