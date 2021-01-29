import random
import argparse

def intro():
    title = "Math Quiz"
    print(title)
    print("*" * len(title))
    operationMenu = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Exit"]
    print(operationMenu[0])
    print(operationMenu[1])
    print(operationMenu[2])
    print(operationMenu[3])
    print(operationMenu[4])

def separator():
    print("-" * 24)

def userInput():
    userChoice = int(input("Enter your operation of choice: "))
    while userChoice > 5 or userChoice <= 0:
        print("Invalid menu option.")
        userChoice = int(input("Please enter a valid option: " ))
    else:
        return userChoice


def userAnswer(problem):
    for i in range(10):
        print("Enter your answer to the question")
        print(problem)
        result = int(input(" = "))
        return result

def checkAnswer(userSolution, solution, count):
    if userSolution == solution:
        count = count + 1
        print("Correct!")
        return count
    else:
        print("Incorrect : (")
        return count




def askquestion(index, count):
    firstNumber = random.randrange(1, 21)
    secondNumber = random.randrange(1, 21)
    if index is 1:
        problem = str(firstNumber) + " + " + str(secondNumber)
        solution = firstNumber + secondNumber
        userSolution = userAnswer(problem)
        count = checkAnswer(userSolution, solution, count)
        return count
    elif index is 2:
        problem = str(firstNumber) + " - " + str(secondNumber)
        solution = firstNumber - secondNumber
        userSolution = userAnswer(problem)
        count = checkAnswer(userSolution, solution, count)
        return count
    elif index is 3:
        problem = str(firstNumber) + " * " + str(secondNumber)
        solution = firstNumber * secondNumber
        userSolution = userAnswer(problem)
        count = checkAnswer(userSolution, solution, count)
        return count
    else:
        problem = str(firstNumber) + " // " + str(secondNumber)
        solution = firstNumber // secondNumber
        userSolution = userAnswer(problem)
        count = checkAnswer(userSolution, solution, count)
        return count


def display_result(total, correct):
    if total > 0:
        result = correct / total

    print("You answered", correct, "questions correctly out of", total, "questions.")

def main():
    parser = argparse.ArgumentParser(description="Math Quiz")
    args = parser.parse_args()
    print(args.accumulate(args.integers))

    intro()
    separator()

    option = userInput()
    totalscore = 0
    correct = 0
    while totalscore != 10:
        totalscore = totalscore + 1
        correct = askquestion(option, correct)
    separator()
    display_result(totalscore, correct)
    print("Do you want to play again? Press 1 for yes or 0 to exit")
    userinput = int(input("Enter your choice: "))
    if userinput == 1:
        main()
    else:
        print("Exit the quiz.")
main()