class Student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
    def calculate_average(self):
        if len(self.grades)==0:
            return 0
        return sum(self.grades)/len(self.grades)
    def check_pass_fail(self):
        avg=self.calculate_average()
        if avg>50:
            return "passed"
        else:
            return "fail"
        
    def print_details(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"grades: {self.grades}")
        print(f"Avarage: {self.calculate_average()}")
        print(f"results: {self.check_pass_fail()}")
        print("-"*30)

students=[
    Student("brian",20,[45,80,70]),
    Student("scola",20,[80,58,70]),
    Student("pee",18,[80,60,70])
]

for s in students:
    s.print_details()