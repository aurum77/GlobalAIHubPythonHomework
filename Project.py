import random as rnd

class Student():

    name = list()
    courses = list()
    grades = dict()    
    chosenCourse = int()
    finalGrade = float()

    def inputName(self):

        for i in range(3):
            inputName = input("\nInput your Name and Surname\n")
    
            # Compare the input with the object's name variable
            if self.checkName(inputName.split()):
                print("Welcome")
                break
            else:
                print("Wrong name or surname")
    
            if i == 2:
                # Print message if 3rd try fails
                print("\nPlease try again later")
                quit()

    def checkName(self, name):

        if self.name == name:
            return True
        else:
            return False

    def inputCourses(self):

        print("Please input the names of the courses you want to take")
        print("and input \"done\" when you are done inputting them")
        print("You have to take 3 courses at least and 5 at most\n")

        # Take 5 courses at most,
        # stop input when input is equal to "done"
        for i in range(5):
            inputToAppend = input()
            if inputToAppend == 'done':
                break
            
            # Append the courses to the courses list in the object
            self.courses.append(inputToAppend)
            if i == 4:
                print("You have inputted 5 courses")

    def chooseRandomCourse(self):

        # Choose a random course
        self.chosenCourse = rnd.randint(0,len(self.courses) - 1)
        print("You chose course " + self.courses[self.chosenCourse])

    def getCourses(self):

        return self.courses

    def checkCourseCount(self):

        if len(self.courses) < 3:
            return "You have failed in class"

    def generateGrades(self):

        self.grades["midterm"] = rnd.randint(0,100)
        self.grades["final"] = rnd.randint(0,100)
        self.grades["project"] = rnd.randint(0,100)

    def printGrades(self):

        print("\nTook an exam from course \"" + s.courses[s.chosenCourse] + "\"")
        print("and you got " + str(s.grades["midterm"]) + " points from midterm ")
        print(str(s.grades["final"]) + " points from final ")
        print("and " + str(s.grades["project"]) + " points from project ")

        self.finalGrade = (self.grades["midterm"] * 0.3) + (self.grades["final"] * 0.5) + (self.grades["project"] * 0.2)

        if self.finalGrade > 90:
            print("You have the letter grade of AA")
            print("Your final grade is: " + str(int(self.finalGrade)))
        elif self.finalGrade <= 90 and self.finalGrade > 70:
            print("You have the letter grade of BB")
            print("Your final grade is: " + str(int(self.finalGrade)))
        elif self.finalGrade <= 70 and self.finalGrade > 50 :
            print("You have the letter grade of CC")
            print("Your final grade is: " + str(int(self.finalGrade)))
        elif self.finalGrade <= 50 and self.finalGrade > 30:
            print("You have the letter grade of DD")
            print("Your final grade is: " + str(int(self.finalGrade)))
        elif self.finalGrade <= 30 and self.finalGrade > 0:
            print("You have the letter grade of FF")
            print("Your final grade is: " + str(int(self.finalGrade)))
            print("You have failed")
            


# Instantiate the Student object
s = Student()

# Set the name and surname for the student object 
s.name = ['Bora', 'Baykar']

# Get the name as input and quit if 3 tries fail
s.inputName()

# Get the course names as input and append the to a list
s.inputCourses()

# Use the return statement to print a message and
# enter the if block when a message is returned
if s.checkCourseCount():
    print(s.checkCourseCount())
    quit()

# Choose a random course to get graded on
s.chooseRandomCourse()

# Assign random grades to the "grades" dictionary
s.generateGrades()

# Print the student's grades along with the letter grade
s.printGrades()