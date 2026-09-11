class Student:
    def __init__(self, hair_color: bool, hair_length: bool, cut_nails: bool, uniform: bool):
        # Public attributes (+ in UML)
        self.hair_color = hair_color      # True = Natural hair
        self.hair_length = hair_length    # True = Appropriate length (not long)
        self.cut_nails = cut_nails        # True = Cut nails (not uncut)
        
        # Private attribute (- in UML)
        self.__uniform = uniform          # True = Complete uniform


    def count_violations(self) -> int:
        """Counts total dress code and grooming violations (False values)."""
        checks = [self.hair_color, self.hair_length, self.cut_nails, self.__uniform]
        return sum(1 for check in checks if not check)

  
    def set_uniform_status(self, is_complete: bool) -> None:
        """Safely updates the private uniform attribute after verification."""
        self.__uniform = is_complete


    def evaluate_student(self) -> str:
        """Determines if the student receives an Offense, Warn, or Ignore."""
        violations = self.count_violations()

        if violations > 2:
            return f"Offense: {violations} violations detected (non-natural hair, long hair, uncut nails, or improper uniform)."
        elif violations >= 1:
            return f"Warn: {violations} violation(s) detected. Please rectify before the next check."
        else:
            return "Ignore: No violations found. Fully compliant."




if __name__ == "__main__":
    student1 = Student(hair_color=False, hair_length=False, cut_nails=False, uniform=False)
    student2 = Student(hair_color=True, hair_length=True, cut_nails=True, uniform=True)

    print("=== BEFORE ===")
    print(f"Object 1 (student1) Violations: {student1.count_violations()}")
    print(f"Object 1 (student1) Status: {student1.evaluate_student()}")
    print(f"Object 2 (student2) Violations: {student2.count_violations()}")
    print(f"Object 2 (student2) Status: {student2.evaluate_student()}\n")

    #Call state-changing method on Object 1 ONLY
    print("Performing action on Object 1 (Updating uniform status to True)...\n")
    student1.set_uniform_status(True)

    print("=== AFTER ===")
    print(f"Object 1 (student1) Violations: {student1.count_violations()} (UPDATED)")
    print(f"Object 1 (student1) Status: {student1.evaluate_student()}")
    print(f"Object 2 (student2) Violations: {student2.count_violations()} (UNCHANGED)")
    print(f"Object 2 (student2) Status: {student2.evaluate_student()}")