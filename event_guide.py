def welcome():
    print("Welcome to the Event Guide!")
    print("Find an event that matches your interests.")


# Display the five available menu choices.
def menu():
    print("1. Get ticket price for an event")
    print("2. Check if I can attend an event")
    print("3. See event details")
    print("4. Get an event recommendation")
    print("5. Quit")


# Return the ticket price based on the event and student status.
def get_ticket_price(event_type, is_student):
    if event_type == "music":
        if is_student:
            return 12.00
        else:
            return 25.00
    elif event_type == "sports":
        if is_student:
            return 0.00
        else:
            return 15.00
    elif event_type == "festival":
        if is_student:
            return 0.00
        else:
            return 10.00
    elif event_type == "fundraiser":
        if is_student:
            return 5.00
        else:
            return 20.00


# Return whether the user's age meets the event's age requirement.
def check_age_limit(event_type, age):
    if event_type == "music" or event_type == "fundraiser":
        return age >= 18
    else:
        return True


# Display the event and reuse the pricing function for its cost.
def print_event(event_type, is_student):
    price = get_ticket_price(event_type, is_student)
    print("Event:", event_type)
    print("Cost: $" + format(price, ".2f"))


# Return an event based on mood and willingness to spend money.
def recommend_event(mood, money):
    if mood == "energetic":
        if money:
            return "fundraiser"
        else:
            return "sports"
    else:
        if money:
            return "music"
        else:
            return "festival"


# Collect user information and process menu choices until the user quits.
def main():
    welcome()

    # Convert the student answer to a Boolean for the pricing functions.
    student_answer = input("Are you a student? (yes/no):\n")
    is_student = student_answer.strip().lower() == "yes"
    age = int(input("What is your age?\n"))

    # Keep choices as text so invalid entries can receive the error message.
    menu_choice = ""
    while menu_choice != "5":
        menu()
        menu_choice = input().strip()

        # The first three choices all need the same event information.
        if menu_choice == "1" or menu_choice == "2" or menu_choice == "3":
            event_type = input(
                "Which event? (music / sports / festival / fundraiser):\n"
            ).strip().lower()

            if event_type not in ("music", "sports", "festival", "fundraiser"):
                print("Please choose one of the listed event types.")
                continue

            if menu_choice == "1":
                price = get_ticket_price(event_type, is_student)
                print("Ticket price: $" + format(price, ".2f"))
            elif menu_choice == "2":
                if check_age_limit(event_type, age):
                    print("You can attend this event!")
                else:
                    print("You may not attend this event.")
            else:
                print_event(event_type, is_student)

        # Convert the money answer to a Boolean for the recommendation.
        elif menu_choice == "4":
            mood = input(
                "How are you feeling? (energetic / relaxed):\n"
            ).strip().lower()
            money_answer = input("Are you willing to spend money? (yes/no):\n")
            money = money_answer.strip().lower() == "yes"
            print("We recommend:", recommend_event(mood, money))
        elif menu_choice != "5":
            print("Sorry, that was not a valid option.")

    print("Thank you for using our Event Guide. Have fun!")


# Start the program when this file is run in IDLE or Python.
if __name__ == "__main__":
    main()
