import sys

WinAmount = 0

LastCheckpoint = None

Introduction = """

Welcome to KBC Game !!!!

1. The game consists of 16 MCQ questions.
2. At any point you can quit the game by entering "q".
3. There will be 4 option. You have to choose 1 correct answer. 

"""

GameQus = [
    "In which year did India become a republic?",
    "Which Indian cricketer holds the record for the highest individual score in test cricket?",
    "Which Indian state has the highest literacy rate?",
    "Which planet in our solar system is known as the Red Planet?",
    "Which country is the largest producer of coffee in the world?",
    "Which Indian state is the largest producer of rice?",
    "Which river is known as the Sorrow of Bihar due to frequent flooding?",
    "Who is the current CEO of Microsoft?",
    "Which Indian state is known as the Land of Five Rivers?",
    "Which country is home to the tallest building in the world, the Burj Khalifa?",
    "Which Indian state has the largest forest cover?",
    "Which video game shattered the record for most sales in 24 hours, making over $800 million?",
    "In what year was the first video game invented?",
    "Pacman was designed to resemble which food?",
    "Which is the National game of our India?",
    "What is the old name of Ahmedabad"]

QOpt = [
    "A.1950 \n B.1947 \n C.1965 \n D.1971",
    "A.Sachin Tendulkar \n B.Virender Sehwag \n C.Rohit Sharma \n D.Rahul Dravid",
    "A.Tamil Nadu \n B.Punjab \n C.Maharashtra \n D.Kerala",
    "A.Jupiter \n B.Mars \n C.Venus \n D.Saturn",
    "A.Brazil \n B.Ethiopia \n C.Vietnam \n D.Colombia",
    "A.Punjab \n B.Uttar Pradesh \n C.West Bengal \n D.Tamil Nadu",
    "A.Brahmaputra \n B.Kaveri \n C.Ganga \n D.Yamuna",
    "A.Steve Ballmer \n B.Satya Nadella \n C.Bill Gates \n D.Tim Cook",
    "A.Madhya Pradesh \n B.Rajasthan \n C.Haryana \n D.Punjab",
    "A.United Arab Emirates \n B.Saudi Arabia \n C.Kuwait \n D.Qatar",
    "A.Arunachal Pradesh \n B.Madhya Pradesh \n C.Kerala \n D.Maharashtra",
    "A.Fifa 18 \n B.Grand Theft Grand Theft Auto V \n C.Call of Duty: Black Ops \n D.Cyberpunk 2077",
    "A.1958 \n B.1969 \n C.1943 \n D.1962",
    "A.Cookie \n B.Burger \n C.Pizza \n D.Sandwich",
    "A.Football \n B.Hockey \n C.Cricket \n D.Volleyball",
    "A.Amdavad \n B.Karnavati \n C.Both A & B \n D.None"]

QAns = ["a", "c", "d", "b", "a", "c", "c", "b","d", "a", "a", "b", "a", "c", "b", "c"]

am = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,320000, 640000, 1250000, 2500000, 5000000, 7500000, 10000000]

def prt_Que(string):
    for s in string:
        if s not in "\t\n":
            print(s, end="")
        else:
            print(s, end="")


def prt_Ans(string):
    lines = string.split("\n")
    for line in lines:
        if line:
            print(line, end="\n")
        else:
            print(line, end="\n")


def generator():
    for question, options, answer, amount in zip(GameQus, QOpt, QAns, am):
        yield (question, options, answer, amount)


everything = generator()

LengthOfGame = len(GameQus)

prt_Que(Introduction)

input("Press [Enter] to start the game.")

print()

prt_Que("Welcome to KBC Game\n\n")

for i in range(1, LengthOfGame+1):
    question, options, answer, amount = next(everything)
    prt_Que(f"Question Number {i}")
    print()
    prt_Que(question)
    print()
    prt_Ans(options)
    print()

    choice = str(input("Enter your option: "))

    choice = choice.strip().lower()

    while choice not in "abcdq" or choice == "":

        print("Not a valid option\nTry Again\n")

        choice = str(input("Enter your option: "))
        choice = choice.strip().lower()

    if choice == "q":
        if LastCheckpoint:
            WinAmount = am[LastCheckpoint-1]
        print()
        prt_Ans(f"Game Ending!!\n\nThe Correct Answer is option {answer.upper()}\n\nYou won ₹{WinAmount:,}")
        sys.exit()
    else:
        if choice == answer:
            WinAmount += amount
            prt_Ans(f"\nCorrect Answer!!\nYou won ₹{amount:,}")
            if i in [4, 8, 11, 13]:
                LastCheckpoint = i
        else:
            if LastCheckpoint:
                WinAmount = am[LastCheckpoint-1]
            print()
            prt_Ans(f"Sorry Incorrect Option \n Correct Answer is option {answer.upper()}!! \n\n Game Over \n\n You won ₹{WinAmount:,}")
            sys.exit()
    print()

else:
    prt_Que("Congratulations you completed the KBC game.")
