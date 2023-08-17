urls = {
    "base": "https://codefirstgirls.com/",
    "courses": "https://codefirstgirls.com/courses",
    "opportunities": "https://codefirstgirls.com/opportunities",
    "cfgdegree": "https://codefirstgirls.com/courses/cfgdegree/",
    "ambassadors": "https://codefirstgirls.com/opportunities/ambassadors/"
}

current_url = urls["base"]

while True:
    print("You are currently on the URL:", current_url)

    if current_url == urls["base"]:
        print("Where are you clicking?")
        print("Options: Courses, Opportunities")
        choice = input("Enter your choice: ")

        if choice == "Courses":
            current_url = urls["courses"]
        elif choice == "Opportunities":
            current_url = urls["opportunities"]
        elif choice != "Courses" or "Opportunities":
            print("Invalid choice")
            pass
    elif current_url == urls["courses"]:
        print("Where are you clicking?")
        print("Options: CFGDegree, Back")
        choice = input("Enter your choice: ")

        if choice == "CFGDegree":
            current_url = urls["cfgdegree"]
        elif choice == "Back":
            current_url = urls["base"]
        elif choice != "CFGDegree" or "Back":
            print("Invalid Choice")
            pass
    elif current_url == urls["cfgdegree"]:
        print("Where are you clicking?")
        print("Options: Back")
        choice = input("Enter your choice: ")

        if choice == "Back":
            current_url = urls["courses"]
        elif choice != "Back":
            print("Invalid choice")
            pass
    elif current_url == urls["opportunities"]:
        print("Where are you clicking?")
        print("Options: Ambassadors, Back")
        choice = input("Enter your choice: ")

        if choice == "Ambassadors":
            current_url = urls["ambassadors"]
        elif choice == "Back":
            current_url = urls["base"]
        elif choice != "Ambassadors" or "Back":
            print("Invalid Choice")
            pass
    else:
        print("Invalid URL.")
        break


# Time Complexity:
# Since the time complexity is in line with how many iterations are passed through the
# while loop, the number of conditional statements and input operations do not change
# depending on the data. The loop will terminate when broken out of or closed.
# Therefore, the time complexity would be O(1).

# Space Complexity:
# Since there are a set number of urls in a dictionary and the number of choices a
# user can make, this would set the space complexity as O(1).
#
# Therefore, both time and space complexity are O(1).

# Assumptions:
# The user will input the prompts according to the options presented to them.
# There will be no connectivity issues/errors related to the URL.
# The user will eventually break out of the program or terminate it themsevles.
