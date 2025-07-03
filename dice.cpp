#include <iostream>
#include <random>
#include <vector>
#include <iomanip>

class DiceSimulator {
private:
    std::random_device rd;
    std::mt19937 gen;
    std::uniform_int_distribution<> dis;
    int totalRolls;

public:
    DiceSimulator() : gen(rd()), dis(1, 6), totalRolls(0) {}

    std::vector<int> rollDice(int numDice) {
        std::vector<int> results;
        for (int i = 0; i < numDice; i++) {
            results.push_back(dis(gen));
        }
        totalRolls++;
        return results;
    }

    void displayResults(const std::vector<int>& results) {
        std::cout << "\n--- Roll Results ---\n";
        std::cout << "Dice rolled: ";
        
        int sum = 0;
        for (size_t i = 0; i < results.size(); i++) {
            std::cout << results[i];
            if (i < results.size() - 1) {
                std::cout << ", ";
            }
            sum += results[i];
        }
        
        std::cout << "\nSum: " << sum << std::endl;
        std::cout << "Total rolls this session: " << totalRolls << std::endl;
    }

    int getTotalRolls() const {
        return totalRolls;
    }
};

int getValidInput(const std::string& prompt, int min, int max) {
    int input;
    while (true) {
        std::cout << prompt;
        if (std::cin >> input && input >= min && input <= max) {
            return input;
        } else {
            std::cout << "Invalid input. Please enter a number between " 
                      << min << " and " << max << ".\n";
            std::cin.clear();
            std::cin.ignore(10000, '\n');
        }
    }
}

char getYesNo(const std::string& prompt) {
    char choice;
    while (true) {
        std::cout << prompt;
        std::cin >> choice;
        choice = std::tolower(choice);
        if (choice == 'y' || choice == 'n') {
            return choice;
        } else {
            std::cout << "Please enter 'y' for yes or 'n' for no.\n";
            std::cin.clear();
            std::cin.ignore(10000, '\n');
        }
    }
}

int main() {
    DiceSimulator simulator;
    
    std::cout << "=== Dice Rolling Simulator ===\n";
    std::cout << "Welcome to the dice rolling simulator!\n";
    
    bool continueRolling = true;
    
    while (continueRolling) {
        // Get number of dice from user
        int numDice = getValidInput("\nHow many dice would you like to roll? (1-10): ", 1, 10);
        
        // Roll the dice
        std::vector<int> results = simulator.rollDice(numDice);
        
        simulator.displayResults(results);
        
        char rollAgain = getYesNo("\nWould you like to roll again? (y/n): ");
        continueRolling = (rollAgain == 'y');
    }
    
    std::cout << "\nThanks for playing! You rolled the dice " 
              << simulator.getTotalRolls() << " times during this session.\n";
    std::cout << "Goodbye!\n";
    
    return 0;
}
