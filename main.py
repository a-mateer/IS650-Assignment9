# My Virtual Pet

from typing import TypedDict

# Custom class to define a pet
class PetStats(TypedDict):
    name: str
    money: int
    hunger: int
    happiness: int
    energy: int


def gameStart() -> PetStats:
    print("MY VIRTUAL PET")
    print("---------------------")
    name = input("What is your pet's name?\n").strip() or "Pet"
    printPetArt()

    stats: PetStats = {
        "name": name,
        "money": 0,
        "hunger": 50,
        "happiness": 50,
        "energy": 50,
    }

    printStats(stats)
    return stats


def printPetArt() -> None:
    print(r"""
    /\_/\
   ( o.o )
    > ^ <
""")


def printActionArt(action: str) -> None:
    action_art = {
        "1": r"""
    /\_/\
   ( o.o )
    > ^ <

        o
 \    ooooo    /
  \ ooooooooo /
   \_________/
""",
        "2": r"""
    /\_/\
   ( o.o )  .-.
    > ^ <  (   )
            `-'
   .-.
  (   )
   `-'
""",
        "3": r"""
    /\_/\    $
   ( O.O )  $ 
    > ^ <  $   
""",
        "4": r"""
    /\_/\    Z
   ( -.- )  Z
    > ^ <  Z
""",
        "5": r"""
               /\
              /  \
    /\_/\    /    \
   ( ^.^ )  /______\
    > ^ <      ||
""",
    }
    print(action_art[action])


def printGameOverArt() -> None:
    print(r"""
  GGGG   A   M   M EEEEE   OOO  V   V EEEEE RRRR
 G      A A  MM MM E      O   O V   V E     R   R
 G GGG AAAAA M M M EEEE   O   O V   V EEEE  RRRR
 G   G A   A M   M E      O   O  V V  E     R R
  GGGG A   A M   M EEEEE   OOO    V   EEEEE R  RR
""")


# This function provides status updates
def printStats(stats: PetStats) -> None:
    print(f"{stats['name']}'s Stats:")
    print("Hunger:", stats["hunger"])
    print("Happiness:", stats["happiness"])
    print("Energy:", stats["energy"], "\n")

# This function caps the stats at 100 max
def _clampStats(stats: PetStats) -> None:
    for stat in ("hunger", "happiness", "energy"):
        stats[stat] = max(0, min(100, stats[stat]))


def feedPet(stats: PetStats) -> PetStats:
    if stats["money"] >= 25:
        stats["money"] -= 25
        stats["hunger"] -= 15
        _clampStats(stats)
        printStats(stats)
    else:
        print("Not enough money, go to work.")
    return stats


def playFetch(stats: PetStats) -> PetStats:
    stats["happiness"] += 10
    stats["energy"] -= 10
    _clampStats(stats)
    printStats(stats)
    return stats


def goToWork(stats: PetStats) -> PetStats:
    stats["money"] += 50
    stats["hunger"] += 20
    stats["happiness"] -= 20
    _clampStats(stats)
    printStats(stats)
    return stats


def goToSleep(stats: PetStats) -> PetStats:
    stats["hunger"] += 10
    stats["happiness"] += 10
    stats["energy"] += 10
    _clampStats(stats)
    printStats(stats)
    return stats


def takeWalk(stats: PetStats) -> PetStats:
    stats["hunger"] += 10
    stats["happiness"] += 15
    stats["energy"] -= 10
    _clampStats(stats)
    printStats(stats)
    return stats


if __name__ == "__main__":
    stats = gameStart()

    while True:
        # Game continues until the limit is reached on hunger, happiness, or energy
        if stats["hunger"] >= 100 or stats["happiness"] <= 0 or stats["energy"] <= 0:
            print("Game over. Your pet didn't make it.")
            printGameOverArt()
            break

        print("1 = Feed pet")
        print("2 = Play fetch")
        print("3 = Go to work")
        print("4 = Go to sleep")
        print("5 = Take a walk")
        print("Q = Quit\n")
        uInput = input("Select an action:\n").strip().lower()

        if uInput == "1":
            printActionArt(uInput)
            feedPet(stats)
        elif uInput == "2":
            printActionArt(uInput)
            playFetch(stats)
        elif uInput == "3":
            printActionArt(uInput)
            goToWork(stats)
        elif uInput == "4":
            printActionArt(uInput)
            goToSleep(stats)
        elif uInput == "5":
            printActionArt(uInput)
            takeWalk(stats)
        elif uInput == "q":
            # Game ends with a quit command
            print("Thanks for playing!")
            printGameOverArt()
            break
        else:
            # This redirects the user to provide valid input
            print("Invalid choice. Select 1-5 or Q to quit.\n")
