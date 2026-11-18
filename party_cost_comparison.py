def main():
    local_price = float(input(
        "What is the price of the local watch party?\n"
    ))
    number_of_people = int(input(
        "How many people are going (including you)?\n"
    ))

    attending_cost = local_price * number_of_people
    hosting_cost = 0.0
    another_dish = "yes"

    while another_dish == "yes":
        dish_name = input(
            "What dish are you making for the party?\n"
        )
        number_of_ingredients = int(input(
            "How many ingredients does it have?\n"
        ))

        dish_cost = 0.0
        ingredient_number = 1

        while ingredient_number <= number_of_ingredients:
            ingredient_cost = float(input(
                "How much is ingredient #"
                + str(ingredient_number)
                + "?\n"
            ))
            dish_cost = dish_cost + ingredient_cost
            ingredient_number = ingredient_number + 1

        print(
            "This dish will cost $"
            + format(dish_cost, ".2f")
            + "."
        )
        hosting_cost = hosting_cost + dish_cost
        another_dish = input("Is there another dish?\n")

    rounded_hosting_cost = round(hosting_cost, 2)
    rounded_attending_cost = round(attending_cost, 2)

    if rounded_hosting_cost == rounded_attending_cost:
        print("Hosting your own party will cost the same as attending one.")
    elif rounded_hosting_cost > rounded_attending_cost:
        print("Hosting your own party will cost more than attending one.")
    else:
        print("Hosting your own party will be cheaper than attending one!")


if __name__ == "__main__":
    main()
