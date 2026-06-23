import grading_system

class ExamResultSystem:
    def __init__(self):
        
        self.student_records = [] 

    def add_student_from_input(self):
        print("\n--- Enter Student Details ---")
        roll_no = input("Enter Roll Number: ").strip()
        name = input("Enter Student Name: ").strip()
        
   
        student_details = (roll_no, name)
        
      
        marks = {}
        print("Enter marks for subjects (Enter an empty subject name to stop):")
        while True:
            subject = input("  Subject Name: ").strip()
            if not subject:
                break
            try:
                score = float(input(f"  Enter marks for {subject}: "))
                if 0 <= score <= 100:
                    marks[subject] = score
                else:
                    print("   Marks must be between 0 and 100.")
            except ValueError:
                print("   Invalid input. Please enter numbers for marks.")
        
        if not marks:
            print(" No marks were entered. Student registration cancelled.")
            return

        total, percentage, grade = grading_system.process_student_marks(marks)
        
     
        record = {
            "details": student_details, 
            "marks": marks,             
            "total": total,
            "percentage": percentage,
            "grade": grade
        }
        self.student_records.append(record)
        print(f"Successfully added records for {name}!")

    def generate_rankings(self):
        """Sorts student records in descending order based on total marks."""
        
        self.student_records.sort(key=lambda x: x['total'], reverse=True)

    def print_grade_reports(self):

        if not self.student_records:
            print("\n No student records found.")
            return
            
        print("\n GRADES REPORT")
  
        for rank, record in enumerate(self.student_records, 1):
            roll_no, name = record["details"]
            print(f"Rank: {rank} | Roll No: {roll_no} | Name: {name}")
            print(f"  Marks: {record['marks']}")
            print(f"  Total: {record['total']} | Percentage: {record['percentage']}% | Grade: {record['grade']}")
            print("-" * 45)

    def save_results_to_file(self, filename="exam_results.txt"):
        """Stores structured report analytics inside an external text file."""
        if not self.student_records:
            print("\n⚠ No records to save.")
            return
            
        with open(filename, "w") as file:
            file.write("OFFICIAL EXAM RANK RESULT\n")
          
            file.write(f"{'Rank':<6}{'Roll No':<10}{'Name':<15}{'Total':<8}{'Percentage':<12}{'Grade':<6}\n")
            file.write("-" * 57 + "\n")
            
            for rank, record in enumerate(self.student_records, 1):
                roll_no, name = record["details"]
                file.write(f"{rank:<6}{roll_no:<10}{name:<15}{record['total']:<8}{record['percentage']:<12}%{record['grade']:<6}\n")
                
        print(f"\nResults successfully saved to file: '{filename}'")



def main():
    system = ExamResultSystem()
    
    while True:
        print("\n=== EXAM RESULT PROCESSING SYSTEM ===")
        print("1. Add Student & Marks")
        print("2. Process Rankings & View Grade Reports")
        print("3. Export Results to File")
        print("4. Exit")
        
        choice = input("Select option (1-4): ").strip()
        
        if choice == "1":
            system.add_student_from_input()
        elif choice == "2":
            system.generate_rankings()
            system.print_grade_reports()
        elif choice == "3":
            system.generate_rankings()
            system.save_results_to_file()
        elif choice == "4":
            print("Exiting Exam Processing System. Goodbye!")
            break
        else:
            print(" Invalid entry. Choose options 1 to 4.")

if __name__ == "__main__":
    main()
