# Parent & Child Classes (IS-A)

class CommunityMember:
    """Parent Class representing general school community members."""
    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def get_details(self) -> str:
        return f"ID: {self.id} | Name: {self.name} | Email: {self.email}"


class Student(CommunityMember):
    """Child Class representing a Student (IS-A CommunityMember)."""
    def __init__(self, id: str, name: str, email: str, grade_level: int, section: str):
        # Call parent constructor using super()
        super().__init__(id, name, email)
        self.grade_level = grade_level
        self.section = section

    def get_details(self) -> str:
        base_info = super().get_details()
        return f"{base_info} | Grade: {self.grade_level} | Section: {self.section}"


class Staff(CommunityMember):
    """Child Class representing Staff/Faculty (IS-A CommunityMember)."""
    def __init__(self, id: str, name: str, email: str, unit: str, position: str):
        # cll parent constructor using super()
        super().__init__(id, name, email)
        self.unit = unit
        self.position = position

    def get_details(self) -> str:
        base_info = super().get_details()
        return f"{base_info} | Unit: {self.unit} | Position: {self.position}"


#Aggregation Class (HAS-A)

class SchoolCampus:
    """Class containing other objects via Aggregation (Weak HAS-A)."""
    def __init__(self, campus_name: str):
        self.campus_name = campus_name
        # Receives already existing objects (Aggregation)
        self.members = []

    def add_member(self, member: CommunityMember):
        self.members.append(member)

    def display_campus_directory(self):
        print(f"\n--- {self.campus_name} Directory ---")
        for member in self.members:
            print(member.get_details())


# Test Runs
if __name__ == "__main__":
    print("=== TEST 1: INHERITANCE ===")
    # Creating child instances with inherited parent features
    student1 = Student("2026-07-0012", "Angela D. Carza", "adpcarza@brc.pshs.edu.ph", 9, "Magnesium")
    staff1 = Staff("R4ND0M-ID-NUMB3R5", "Dr. Juan Dela Cruz", "jdelacruz@brc.pshs.edu.ph", "PEHM", "Special Science Teacher III")

    # Reusing inherited method behavior
    print(student1.get_details())
    print(staff1.get_details())

    print("\n=== TEST 2: AGGREGATION ===")
    # Creating campus object and passing independently existing objects
    pshs_brc = SchoolCampus("Philippine Science High School - Bicol Region Campus")
    pshs_brc.add_member(student1)
    pshs_brc.add_member(staff1)

    # Displaying connected objects
    pshs_brc.display_campus_directory()