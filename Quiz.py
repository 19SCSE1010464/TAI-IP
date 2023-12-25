questions = ("How many bits make one byte ?: ",
             "Google is a browser or a search engine ?: ",
             "What is the full form of RAM ?: ")
options = (("A. 16","B. 32","C. 8"),
           ("A. Browser" ,"B. Search engine","C. Neither"),
           ("A. Random access memory" ,"B. None","C. Read and memory"))
answers = ("C","B","A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("***********************")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A,B,C): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT !")
        score+=1
    else:
        print("INCORRECT !")
        print(f"{answers[question_num]} is the correct answer")

    question_num+=1
print("*******************")
print("     RESULTS       ")
print("*******************")

print("Answers :",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("Guesses :",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score/len(questions)*100)
print(f"your score is : {score}%")



