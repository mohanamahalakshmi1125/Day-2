class School:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.SSLC_marks = int(input("Enter your SSLC marks: "))
        self.HSC_marks = int(input("Enter your HSC marks: "))
        self.HSC = self.group()

    def group(self):
        if self.SSLC_marks >= 500:
            print("Bio-Maths")
            self.stream = "Bio-Maths"
            return "Bio-Maths"
        elif self.SSLC_marks >= 450:
            print("Computer Science")
            self.stream = "Computer Science"
            return "Computer Science"
        elif self.SSLC_marks >= 300:
            print("Commerce")
            self.stream = "Commerce"
            return "Commerce"
        else:
            print("Arts")
            self.stream = "Arts"
            return "Arts"


class College(School):
    def college(self):
        if (self.stream == "Bio-Maths" or self.stream == "Computer Science") and self.HSC_marks >= 500:
            return "Congratulations! You are eligible for Medical & Engineering colleges (VIT, SRM, Anna University, Madras University)"

        elif (self.stream == "Commerce" or self.stream == "Arts") and self.HSC_marks >= 450:
            return "Congratulations! You are eligible for Arts & Science colleges (Sathyabama, Stella Maris)"

        elif (self.stream == "Commerce" or self.stream == "Arts") and self.HSC_marks >= 300:
            return "Congratulations! You are eligible for Arts stream only (Thiyagarajar College, Loyola College)"

        else:
            return "Sorry! You are not eligible for any college based on your marks and group."

    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("SSLC Marks:", self.SSLC_marks)
        print("HSC Marks:", self.HSC_marks)
        print("Group:", self.HSC)
        print("College:", self.college())


# Create object
student = College()

# Show details
student.display()
