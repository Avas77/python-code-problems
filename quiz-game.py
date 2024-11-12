# multiple choice questions
# evaluate player's answers
# provide score

questions = [
    {"id": 1, "question": "What is the capital of Nepal", "options": {
        "a": "Kathmandu",
        "b": "Delhi",
        "c": "Karachi"
    }, "correct": "Kathmandu"},
    {"id": 1, "question": "What is the currency of Nepal", "options": {"a":"Rupees", "b":"Dollar", "c":"Riyal"}, "correct": "Rupees"},
]

correct_ans = 0
for item in questions:
    print(item["question"])
    options = item["options"]
    for key, option in options.items():
        print(f"{key}. {option}")
    ans = input("Your Answer:").lower();
    if ans in options.keys() and options[ans] == item["correct"]:
        print("Correct")
        correct_ans += 1
    else: 
        print("Incorrect")
    print("-------------------------------------------")

print(f"Your final score is: {correct_ans}")