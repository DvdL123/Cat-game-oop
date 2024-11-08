import time

def create_cat():
    cat = {
        "name": input("What's your cat's name: "),
        "color": input("What color is your cat: "),
        "intelligence": 10,
        "energy": 50,
        "weight": 10
    }
    return cat


def display_stats(cat):
    print(f"\n{cat['name']}'s Current Stats:")
    print(f"Color: {cat['color']}")
    print(f"Intelligence: {cat['intelligence']}")
    print(f"Energy: {cat['energy']}")
    print(f"Weight: {cat['weight']}")
    print()


def play(cat):
    if cat["energy"] > 5:
        time.sleep(1)
        print("Your cat is Happy!")
        cat["energy"] -= 5
        cat["weight"] -= 1
    else:
        time.sleep(1)
        print("Your cat is too tired to play.")


def train(cat):
    if cat["energy"] > 10:
        time.sleep(1)
        print("Your cat is getting smarter.")
        cat["intelligence"] += 5
        cat["energy"] -= 10
    else:
        time.sleep(1)
        print("Your cat is too tired to train.")


def feed(cat):
    time.sleep(1)
    print("Your cat is feeling fuller and content.")
    cat["energy"] += 10
    cat["weight"] += 1


def sleep(cat):
    time.sleep(1)
    print("Your cat takes a nap and wakes up refreshed.")
    cat["energy"] += 20


def main():
    print("Welcome to the Cat Designer")
    cat = create_cat()

    while True:
        time.sleep(0.5)
        print("\nWhat would you like to do with your cat?")
        print("\n1. Play with your cat")
        print("2. Train your cat")
        print("3. Feed your cat")
        print("4. Put your cat to sleep")
        print("5. Print latest stats")
        print("6. Quit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            play(cat)
        elif choice == "2":
            train(cat)
        elif choice == "3":
            feed(cat)
        elif choice == "4":
            sleep(cat)
        elif choice == "5":
            display_stats(cat)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")



main()