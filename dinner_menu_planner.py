def get_preferences(number_of_guests):
    dish_counts = {}

    for i in range(number_of_guests):
        print("What is guest #" + str(i + 1) + "'s name?")
        name = input()
        print("What are " + name + "'s three favorite dishes?")
        guest_dishes = []

        # Use lowercase so different capitalization still matches.
        for j in range(3):
            dish = input().strip().lower()

            # Count each dish only once for the current guest.
            if dish not in guest_dishes:
                guest_dishes.append(dish)
                if dish in dish_counts:
                    dish_counts[dish] += 1
                else:
                    dish_counts[dish] = 1

    return dish_counts


# Find dishes chosen by every guest and sort them alphabetically.
def find_common_dishes(dish_counts, number_of_guests):
    common_dishes = []

    for dish in dish_counts:
        if dish_counts[dish] == number_of_guests:
            common_dishes.append(dish)

    common_dishes.sort()
    return common_dishes


# Display the menu with each word capitalized.
def print_menu(common_dishes):
    print("For dinner, we will have:")
    for dish in common_dishes:
        print(dish.title())


# Get the guest count and call the functions to build the menu.
def main():
    print("How many guests are coming for dinner?")
    number_of_guests = int(input())

    dish_counts = get_preferences(number_of_guests)
    common_dishes = find_common_dishes(dish_counts, number_of_guests)
    print_menu(common_dishes)


if __name__ == "__main__":
    main()
