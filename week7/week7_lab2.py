class Student:
    # Class variable to keep track of unique membership IDs
    membership_counter = 1000

    def __init__(self, student_id, last_name, programme):
        self.student_id = student_id
        self.last_name = last_name
        self.programme = programme
        self.membership_id = Student.membership_counter  # Assign unique Membership ID
        Student.membership_counter += 1  # Increment the counter for next member

    def __str__(self):
        return f"Membership ID: {self.membership_id}, Student ID: {self.student_id}, Last Name: {self.last_name}, Programme: {self.programme}"

class MembershipSystem:
    def __init__(self):
        self.registered_members = []
        self.withdrawn_members = []
        self.diploma_count = 0
        self.bachelor_count = 0
        self.withdrawn_count = 0

    def register_student(self, student_id, last_name, programme):
        if programme.lower() not in ['diploma', 'bachelor']:
            print("Invalid programme! Please choose either 'Diploma' or 'Bachelor'.")
            return

        # Create a new student object and add it to the registered list
        new_student = Student(student_id, last_name, programme)
        self.registered_members.append(new_student)

        # Update counts based on the programme
        if programme.lower() == 'diploma':
            self.diploma_count += 1
        elif programme.lower() == 'bachelor':
            self.bachelor_count += 1

        print(f"Student {last_name} successfully registered with Membership ID {new_student.membership_id}.")

    def withdraw_student(self, membership_id, last_name):
        # Find the student with matching membership ID and last name
        for student in self.registered_members:
            if student.membership_id == membership_id and student.last_name.lower() == last_name.lower():
                # Remove student from registered list and add to withdrawn list
                self.registered_members.remove(student)
                self.withdrawn_members.append(student)

                # Update counts based on the programme
                if student.programme.lower() == 'diploma':
                    self.diploma_count -= 1
                elif student.programme.lower() == 'bachelor':
                    self.bachelor_count -= 1

                self.withdrawn_count += 1

                print(f"Student {last_name} with Membership ID {membership_id} has successfully withdrawn.")
                return
        print("Student not found or details incorrect.")

    def display_statistics(self):
        # Display the system's current statistics
        print("\nMembership Registration System Statistics:")
        print(f"Number of Registered Members: {len(self.registered_members)}")
        print(f"Number of Diploma Students: {self.diploma_count}")
        print(f"Number of Bachelor of IT Students: {self.bachelor_count}")
        print(f"Number of Withdrawn Students: {self.withdrawn_count}\n")

    def display_registered_members(self):
        print("\nList of Registered Members:")
        for student in self.registered_members:
            print(student)
        print()

# Example usage of the system
def main():
    system = MembershipSystem()

    # Register some students
    system.register_student("S001", "Smith", "Diploma")
    system.register_student("S002", "Johnson", "Bachelor")
    system.register_student("S003", "Williams", "Diploma")

    # Display registered members and statistics
    system.display_registered_members()
    system.display_statistics()

    # Withdraw a student
    system.withdraw_student(1001, "Johnson")

    # Display statistics after withdrawal
    system.display_statistics()

if __name__ == "__main__":
    main()