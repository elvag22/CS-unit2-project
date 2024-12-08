def learninformation():
        print("Sorting trash reduces waste in landfills, saves resources, and prevents pollution. It helps recycle materials and ensures hazardous items don’t harm the environment."
    "\nHow to Organize Trash:"
    "\n-Recycling Bin: Clean paper, cardboard, glass, metal, and certain plastics."
    "\n-Compost Bin: Food scraps, coffee grounds, and yard waste."
    "\n-Trash Bin: Non-recyclable items like dirty plastics or non-compostable food packaging."
    "\n-Hazardous Waste: Batteries, electronics, and chemicals")
        input("\n Enter 'yes' to continue to quiz").lower()
        #break
#For quiz
def quiz():
        questions = [
        "What is one benefit of sorting trash?",
        "Which item belongs in the recycling bin?",
        "What should be placed in a compost bin?",
        "What kind of waste should be disposed of in a hazardous waste bin?",
        "Which is a direct effect of not sorting hazardous waste properly?",
        "Why is it important to clean recyclable items before placing them in the recycling bin?",
        "Which item should not go in the trash bin?",
        "What material is generally suitable for composting?",
        "What is the purpose of having separate bins for trash, recycling, compost, and hazardous waste?",
        "Which of the following is not true about sorting trash?"
    ]
        choices = choices = [
        ["1) Increases landfill waste", "2) Saves resources", "3) Prevents recycling", "4) Slows pollution"],
        ["1) Dirty plastic packaging", "2) Food scraps", "3) Clean cardboard", "4) Batteries"],
        ["1) Metal cans", "2) Coffee grounds", "3) Broken electronics", "4) Dirty glass bottles"],
        ["1) Food wrappers", "2) Used batteries", "3) Cardboard boxes", "4) Plastic water bottles"],
        ["1) Reduction in pollution", "2) Resource conservation", "3) Environmental harm", "4) Cleaner compost"],
        ["1) To make them compostable", "2) To ensure they can be properly recycled",
         "3) To avoid placing them in hazardous waste", "4) To reduce their weight"],
        ["1) Non-compostable food packaging", "2) Broken electronics", "3) Dirty plastics", "4) Unrecyclable wrappers"],
        ["1) Glass", "2) Yard waste", "3) Metal", "4) Used batteries"],
        ["1) To save time when disposing of items", "2) To reduce the need for recycling",
         "3) To minimize waste and environmental impact", "4) To eliminate the need for landfills"],
        ["1) It reduces waste in landfills.", "2) It prevents pollution.",
         "3) It eliminates the need for hazardous waste disposal.", "4) It helps recycle materials."]
    ]
        answers = [2, 3, 2, 2, 3, 2, 2, 2, 3, 3]

        score = 0
        wronganswer = []
        for i in range(len(questions)):
            print(f"\nQuestion {i + 1}: {questions[i]}")
            for choice in choices[i]:
                print(choice)
            user_answer = input("Your answer (Enter the number): ")
            if int(user_answer) == answers[i]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {answers[i]}.")
        print(f"\nYour final score is: {score}/{len(questions)}")
        if score == len(questions):
            print("You mastered these skills, good job!")
#intro
while True:
        print("\nDo you want to (1) Learn information or (2) Take the quiz?")
        choice = input("Enter your choice: ").lower()
        if choice == "1":
            learninformation()
            quiz()
            break
        elif choice == "2":
            quiz()
            break
        else:
            print("Invalid input. Please try again.")



