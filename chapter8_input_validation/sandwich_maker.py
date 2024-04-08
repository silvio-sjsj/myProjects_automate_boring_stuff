import pyinputplus as pyip

# Prices for different sandwich options
PRICE_BREAD = {"wheat": 1.0, "white": 1.0, "sourdough": 1.5}
PRICE_PROTEIN = {"chicken": 2.0, "turkey": 2.5, "ham": 2.0, "tofu": 2.0}
PRICE_CHEESE = {"cheddar": 1.0, "Swiss": 1.5, "mozzarella": 1.5}
PRICE_EXTRA = {"mayo": 0.5, "mustard": 0.4, "lettuce": 0.2, "tomato": 0.45}

def get_sandwich_preferences(num_sandwiches):
    """Get sandwich preferences from the user"""
    print(f"\nSandwich {num_sandwiches}:")
    print("Selection of the bread type")
    bread = pyip.inputMenu(["wheat: $1", "white: $1", "sourdough: $1.5"],
                            numbered=True)
    bread = bread.split(":")[0].strip()
    print("Selection of the protein")
    protein = pyip.inputMenu(["chicken: $2.0", "turkey: $2.5",
                              "ham: $2.0", "tofu: $2.0"], numbered=True)
    protein = protein.split(":")[0].strip()
    cheese_choice = pyip.inputYesNo("Do you want cheese? (yes/no): \n")
    cheese = None
    if cheese_choice == "yes":
        print("Selection of the cheese type")
        cheese = pyip.inputMenu(["cheddar: $1.0", "Swiss: $1.5", "mozzarella: $1.5"],
                                 numbered=True)
        cheese = cheese.split(":")[0].strip()
    extras = []
    extra_choices = pyip.inputYesNo("Do you want mayo, mustard, lettuce, or tomato? (yes/no): \n", allowRegexes=[r'yes', r'no'])
    if extra_choices == "yes":
        print("Select extras (choose option 'done' when finished):")
        while True:
            extra_choices = pyip.inputMenu(["mayo: $0.5", "mustard: $0.4", "lettuce: $0.2",
                                            "tomato: $0.45", "done"],
                                           numbered=True, blank=True)
            extra_choices = extra_choices.split(":")[0].strip()
            if extra_choices.lower() == 'done':
                break
            extras.append(extra_choices)
        print("Selected extras:", extras)
    return bread, protein, cheese, extras

def calculate_total_cost(bread, protein, cheese, extras):
    total_cost = 0
    # Calculate cost of each item
    total_cost += PRICE_BREAD[bread]
    total_cost += PRICE_PROTEIN[protein]
    if cheese:
        total_cost += PRICE_CHEESE[cheese]
    for extra in extras:
        total_cost += PRICE_EXTRA[extra]
    return total_cost

def main():
    print("Welcome to the Sandwich Maker!")
    num_sandwiches = 0
    total_cost_all = 0
    while True:
        num_sandwiches += 1
        bread, protein, cheese, extras = get_sandwich_preferences(num_sandwiches)
        total_cost = calculate_total_cost(bread, protein, cheese, extras)
        num_copies = pyip.inputInt(prompt="How many copies of the sandwich would you like? ",
                                   min=1)
        total_cost *= num_copies
        print(f"\nTotal cost for Sandwich {num_sandwiches}: ${total_cost:.2f}")
        total_cost_all += total_cost
        another_sandwiche = pyip.inputYesNo("Do you want a different sandwich? \n", allowRegexes=[r'yes', r'no'])
        if another_sandwiche == 'no':
            break
    print(f"\nTotal cost for {num_sandwiches} sandwich(es) is: ${total_cost_all:.2f}")

if __name__ == "__main__":
    main()