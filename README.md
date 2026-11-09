# IS650-Assignment9

DUAL-APPROACH FEATURE DEVELOPMENT

# My Virtual Pet
This program creates a virtual pet for the user. The user grants the pet a name, and then must select actions to keep their pet alive and thriving.

# Feature Development Comparison
Manual Branch: The feature on this branch was created to assist the user to keep track of when one of the stats for their pet was getting too high (Hunger) or too low (Happiness, Energy).

AI Branch: The feature on this branch was created to enhance the user experience with ASCII illustrations that printed each time the user selected an action.

The AI model did not nail the brief on the first attempt. It took a couple of follow up prompts and some manual changes to get the update to an acceptable point.

The AI placed the ASCII drawings in the right places, and coded the game to print the art at the right moments in the logic. However, the drawings themselves were not very good/applicable. For example, instead of "GAME OVER" the AI drew the word "GOME".

I had much greater confidence in the feature I had updated manually. The feature I implemented was much simpler, and less prone to interpretation. 

If I was doing the assignment again in the future, I would focus the AI on the simple, logic updates, and would manually tackle the ASCII element.

## Manual Branch
Feature name: Pet Status Warnings

Purpose: Add some guidance to the user to flag when any of the conditions are getting too high or too low.

Expected behavior:
- When Hunger gets to 80, a message is printed instructing the user to feed the pet soon.
- When Happiness gets to 20, a message is printed instructing the user to play with the pet soon.
- When Energy get to 20, a message is printed instructing the user to sleep soon.

Case #1: Only going to work and feeding the pet will lower the happiness, and the Happiness level warning should print.

Case #2: Only going to work and playing with the pet will raise the hunger, and the Hunger level warning should print.

## AI Branch
Feature name: ASCII Art

Purpose: Add some visuals to the game to improve the user experience.

Expected behavior:
- At the start of the game ASCII art is printed of the pet.
- Each time the user chooses an action ASCII art is printed to the console.
- At the end of the game an ASCII art GAME OVER message is printed.

Case #1: Starting the game, checking the ASCII art prints.

Case #2: Ending the game, checking the ASCII GAME OVER prints.

## Initial Version
In the initial version, users chose from four actions that influence the pet's hunger, happiness, and energy.

1. Feed your pet (costs $25)
2. Play fetch
3. Go to work (earns $50)
4. Go to sleep

## Current Actions
In the latest version, users choose from five actions to manage your pet's hunger, happiness, and energy:

1. Feed your pet (costs $25)
2. Play fetch
3. Go to work (earns $50)
4. Go to sleep
5. Take a walk

Enter `Q` to quit. Pet needs stay between 0 and 100, and the game ends when hunger reaches 100 or happiness or energy reaches 0.

## How to Run the Program
The program may be run from the command line interface from the repository by entering: python main.py


