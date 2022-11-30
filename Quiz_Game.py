questions = ("What does DNA stand for?:",
             "What is the hardest natural substance on Earth?:",
             "Which is the main gas that makes up the Earth's atmosphere?:",
             "Roughly how long does it take for the sun's light to reach Earth?:",
             "What is the biggest planet in our solar system?:",
             "How many vertebrae does the average human possess?:")

options = (("A.Deoxy-Ribo Nucleic Acid","B.Dynamic Neural Acid ","C.Di-nucleic Acid","D.Double nucleic acid "),
            ("A.Graphite","B.Carbon","C.Daimond","D.Iron"),
            ("A.Oxygen","B.Nitrogen","C.Carbon-di-Oxide","D.argon Gas"),
            ("A.8 hours","B.8 seconds","C.8 minutes","D.8 milli seconds"),
            ("A.Mercury","B.Venus","C.Earth","D.Jupyte"),
            ("A.33", "B.34", "C.42", "D.242"))

answeres =("A","C","B","C","D","A")

question_num = 0
score = 0
for question in questions:
    print("---------------------------------------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter A , B , C , D:").upper()
    if guess == answeres[question_num]:
        print("CORRECT!!")
        score +=1
    else:
        print(f"INCORRECT!! the correct answere is {answeres[question_num]}")
    question_num += 1
print(f"your score is {score}")