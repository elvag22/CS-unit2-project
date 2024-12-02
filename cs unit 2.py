#Base choice
while True:
    print("\nDo you want to take the quiz first (1), or read the information first (2)?")
    choice = input("Enter your choice: ").lower()
    if choice == "2":
        learninformation = ("Sorting trash reduces waste in landfills, saves resources, and prevents pollution. It helps recycle materials and ensures hazardous items don’t harm the environment."
"\nHow to Organize Trash:"
"\n-Recycling Bin: Clean paper, cardboard, glass, metal, and certain plastics."
"\n-Compost Bin: Food scraps, coffee grounds, and yard waste."
"\n-Trash Bin: Non-recyclable items like dirty plastics or non-compostable food packaging."
"\n-Hazardous Waste: Batteries, electronics, and chemicals")

        print(learninformation)
        print("If you want to continue to the quiz enter 1, if you want to exit, enter 0")

    break
#For quiz
def quiz():
    questions = [
    {
        "questions": "Why is sorting trash important for the environment?",
         "options": ["a) It reduces waste in landfills", "b) It saves resources", "c) It prevents pollution", "d) All of the above"],
         "answer": "d"

    },
    {
        "questions": "What are the benefits of recycling materials?",
        "options": ["a) Conserves resources and energy.","b) Increases landfill capacity"]0

        ("What types of waste should be placed in a recycling bin?")

        ("Which items are suitable for composting?")

        ("What kinds of waste should go in the trash bin?")

        ("Why is it essential to separate hazardous waste from regular trash?")

        ("Give three examples of items considered hazardous waste.")

        ("How does composting benefit the environment?")

        ("What steps can you take to ensure recyclable materials are properly sorted?")

        ("What are the consequences of not separating waste properly?")

        
