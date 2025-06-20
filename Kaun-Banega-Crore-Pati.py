n = input("Enter your name: ")
print("Hello " + n + " Welcome to Kaun banega Crorepati")
print("You have 5 questions with 4 options each")
print("You have 5 lifelines and you can call your friend for answer")
ready = input("Are you ready? (yes/no): ").strip()
if ready.lower() != 'yes':
    print("Okay, maybe next time!")
    exit()

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Saturn", "Mars"],
        "answer": "B"
    },
    {
        "question": "Tell me the best programming language?",
        "options": ["Python", "Java", "C++", "Javascript"],
        "answer": "A"
    },
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "CO2", "O2", "NaCl"],
        "answer": "A"
    }
]

levels = [10000, 5000000, 1000000, 2000, 8000,90000]
money = 0

for i in range(len(questions)):
    q = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(q["question"])
    print(f"a. {q['options'][0]}    b. {q['options'][1]}")
    print(f"c. {q['options'][2]}    d. {q['options'][3]}")
    reply = input("Enter your answer (A/B/C/D): ").strip().upper()
    if reply == q["answer"]:
        print("Correct!")
        money = levels[i]
    else:
        print("Sorry, that's incorrect.")
        print("The correct answer is:", q["options"][ord(q["answer"]) - ord('A')])
        break

print("Your total earnings are Rs.",money)
