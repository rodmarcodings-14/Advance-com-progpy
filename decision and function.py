situation = input("How is your exam situation today? (prepared, anxious, unprepared): ").lower()

if situation == "prepared":
    print("Awesome! Review lightly and stay confident.")
elif situation == "anxious":
    print("Take a deep breath, relax, and focus on key points.")
elif situation == "unprepared":
    print("Don't panic! Make a quick study plan and do your best.")
else:
    print("Hmm, I'm not sure about that situation. Reflect and try again!")
