# IS650-Assignment9

DUAL-APPROACH FEATURE DEVELOPMENT

# My Virtual Pet
This program creates a virtual pet for the user. The user grants the pet a name, and then must select actions to keep their pet alive and thriving.

# Manual Branch
Feature name: Pet Status Warnings
Purpose: Add some guidance to the user to flag when any of the conditions are getting too high or too low.
Expected behavior:
- When Hunger gets to 80, a message is printed instructing the user to feed the pet soon.
- When Happiness gets to 20, a message is printed instructing the user to play with the pet soon.
- When Energy get to 20, a message is printed instructing the user to sleep soon.
Case #1: Only going to work and feeding the pet will lower the happiness, and the Happiness level warning should print.
Case #2: Only going to work and playing with the pet will raise the hunger, and the Hunger level warning should print.

# AI Branch
Feature name: ASCII Art
Purpose: Add some visuals to the game to improve the user experience.
Expected behavior:
- At the start of the game ASCII art is printed of the pet.
- Each time the user chooses an action ASCII art is printed to the console.
- At the end of the game an ASCII art GAME OVER message is printed.
Case #1: Starting the game, checking the ASCII art prints.
Case #2: Ending the game, checking the ASCII GAME OVER prints.

# Initial Version
In the initial version, users chose from four actions that influence the pet's hunger, happiness, and energy.

1. Feed your pet (costs $25)
2. Play fetch
3. Go to work (earns $50)
4. Go to sleep

# Current Actions
In the latest version, users choose from five actions to manage your pet's hunger, happiness, and energy:

1. Feed your pet (costs $25)
2. Play fetch
3. Go to work (earns $50)
4. Go to sleep
5. Take a walk

Enter `Q` to quit. Pet needs stay between 0 and 100, and the game ends when hunger reaches 100 or happiness or energy reaches 0.

# AI Tool Used
I used the built-in Chat option in Visual Studio Code:
> Copilot Fusion selected GPT-6 Luna

# AI Assistance
I gave the model the following prompt:
> Review the program in main.py, suggest improvements, and enhance the game experience for the user by suggesting at least one additional action.

# New or Modified Features
The model gave this summary response:
- Added takeWalk as a fifth action: it boosts happiness while using energy and increasing hunger.
- Added a quit option, feedback for invalid choices, and a default name if the user enters a blank one.
- Capped hunger, happiness, and energy at 0–100, and moved the game-over check so it appears immediately after a fatal action.
- Added a PetStats type and removed unused global stats. 
- Updated the action list in README.md.

# Evaluation of AI Output
I accepted the AI modifications because they made sense from a UI standpoint. Stopping the game when the game-ending decision is made makes a lot of sense for obvious reasons. The custom PetStats type was helpful - it opens the possibility in future versions for managing multiple pets. 

# How to Run the Program
The program may be run from the command line interface from the repository by entering: python main.py


