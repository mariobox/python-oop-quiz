# Quiz App using Python OPP
import os

clear = lambda : os.system('clear')

questionList = [
    ['In what year was Python created?', ['1973', '2002', '1968', '1991'], '1991'],
    ['What is the only programming language that runs in the browser?', ['Pearl', 'SQL', 'JavaScript', 'Python'], 'JavaScript'],
    ['What data type will input from the user give you in Python?', ['int', 'string', 'float', 'array'], 'string'],
    ['Which of the following is not considered a programming language?', ['Python', 'Java', 'C', 'HTML'], 'HTML'],
    ['What does the M in MVC stand for?', ['Model', 'Module', 'Modern', 'Multiple'], 'Model'],
    ['Which of these is NOT a text editor?', ['VIm', 'MS Word', 'Notepad', 'Atom'], 'MS Word'],
    ['How do you define a dictionary in Python?', ['array', 'dict()', 'dictionary()', 'DictReader'], 'dict()'],
    ['What tag do you use to create a hyperlink in HTML?', ['<p>', '<div>', '<a>', '<span>'], '<a>'],
    ['What is the attribute for font color in CSS?', ['color', 'font-color', 'fontColor', 'hue'], 'color'],
    ['Inheritance is a property of which of these?', ['integers', 'strings', 'classes', 'structs'], 'classes']
    ]

# This class doesn't need instances, so no __init__ needed, and cls is used instead of self	
class Quiz:
    score = 0
    questionIndex = 0

    @classmethod
    def displayNextQuestion(cls, questionList):
        clear()
        print("--- CODING QUIZ ---\n")
        print(questionList[cls.questionIndex][0])
        print(f"a) {questionList[cls.questionIndex][1][0]}")
        print(f"b) {questionList[cls.questionIndex][1][1]}")
        print(f"c) {questionList[cls.questionIndex][1][2]}")
        print(f"d) {questionList[cls.questionIndex][1][3]}")

    @classmethod    
    def captureGuess(cls):
        while True:
            guess = input("Choose an answer: ")
            if guess == 'a':
                return 0
            elif guess == 'b':
                return 1
            elif guess == 'c':
                return 2
            elif guess == 'd':
                return 3
            else:
                print("You must return a, b, c or d. Try again")


    @classmethod
    def validateGuess(cls, guess):
        if questionList[cls.questionIndex][1][guess] == questionList[cls.questionIndex][2]:
            cls.score += 1
            print("Correct")
        else:
            print("Incorrect")
        cls.questionIndex += 1
    
    @classmethod
    def printProgress(cls):
        if cls.questionIndex == len(questionList):
            print("Quiz over!")
            print(f"Your final score is: {cls.score}/{cls.questionIndex}")
        else:
            print(f"Your score so far: {cls.score}/{cls.questionIndex}")
            input("Press Enter to continue")
    
    
def main():
    for _ in range(0, len(questionList)):
        Quiz.displayNextQuestion(questionList)
        Quiz.validateGuess(Quiz.captureGuess())
        Quiz.printProgress()



if __name__ == "__main__":
    main()
    

    
        
