class Student:
    def __init__(self, name: str, hair_color: bool, hair_length: bool, cut_nails: bool, uniform: bool):
        self.name = name
        self.hair_color = hair_color      
        self.hair_length = hair_length    
        self.cut_nails = cut_nails        
        self.__uniform = uniform          

    def count_violations(self) -> int:
        checks = [self.hair_color, self.hair_length, self.cut_nails, self.__uniform]
        return sum(1 for check in checks if not check)

    def evaluate_student(self) -> str:
        violations = self.count_violations()
        if violations > 2:
            return f"Offense: {violations} violations detected."
        elif violations >= 1:
            return f"Warn: {violations} violation(s) detected."
        else:
            return "Ignore: No violations found."

# New Related Class
class Inspection:
    def __init__(self, inspector_name: str, date: str):
        self.inspector_name = inspector_name
        self.date = date
        #  Store object references in a list for 1:Many multiplicity
        self.students: list[Student] = []

    # Method to manage association
    def add_student(self, student: Student) -> None:
        self.students.append(student)

    # Access data through the relationship using a loop
    def generate_report(self) -> None:
        for student in self.students:
            print(f"Student: {student.name:<8} | Status: {student.evaluate_student()}")


# Test
if __name__ == "__main__":
    # Instantiate the objects
    print("BEFORE RELATIONSHIP")
    session1 = Inspection("Jeavons Mesia, S.C.O.", "2026-09-14")
    student_a = Student("Angela", True, True, True, True)
    student_b = Student("Kirk", False, False, True, False)
    student_c = Student("Ivan", True, False, False, True)
    print(f"Inspection Session created. Enrolled students: {len(session1.students)}\n")

    # build the relationship
    print("BUILDING RELATIONSHIP")
    print("Assigning students to the inspection session...\n")
    session1.add_student(student_a)
    session1.add_student(student_b)
    session1.add_student(student_c)

    # Access Data (AFTR)
    print("AFTER RELATIONSHIP")
    print(f"Inspection Report by {session1.inspector_name} on {session1.date}:")
    session1.generate_report()