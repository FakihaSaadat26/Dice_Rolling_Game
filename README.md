# Dice_Rolling_Game

Key Features:

1) Random dice rolling: Uses the modern python for proper random number generation
2) Variable number of dice: Users can specify how many dice to roll (1-10)
3) Roll tracking: Keeps count of total rolls during the session
4) User-friendly interface: Clear prompts and formatted output
5) Input validation: Handles invalid input gracefully
6) Continuous play: Asks if the user wants to roll again after each round

How it works:

The DiceSimulator class encapsulates all the dice rolling logic
It uses std::mt19937 (Mersenne Twister) for high-quality random number generation
The rollDice() method generates the specified number of dice results
Results are displayed with individual dice values and their sum
The program tracks and displays the total number of rolls
Input validation ensures users enter valid numbers and responses
