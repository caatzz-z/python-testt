print("welcome to the mini math quiz ! 📝")

score = 0

answer = input("1. What is 2 + 2? ")
if answer.strip() == "4":
    print("correctt ! 🎉")
    score += 1
else:
    print("wrong.., the answer is 4. how could you not know that? 😖")

answer = input("2. What is 5 * 3? ")
if answer.strip() == "15":
    print("correctt ! 🎉")
    score += 1
else:
    print("wrong.., the answer is 15. HOW?? its basic math😲")

print(f"\nur final score is {score}/2. this doesnt prove anything that youre good at math, but good job anyway!..")
