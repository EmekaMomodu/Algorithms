#!/bin/bash

# Check if figlet is installed
if ! command -v figlet &> /dev/null; then
    echo "Figlet is not installed. Installing..."
    # Install figlet on Ubuntu-based systems
    sudo apt-get update && sudo apt-get install figlet
    # For other systems, use the package manager to install figlet
fi

# Game loop
while true; do
    # Ask the user for an input word
    read -p "Enter a word (or 'quit' to exit): " word

    # Exit the game if the user types 'quit'
    if [ "$word" = "quit" ]; then
        break
    fi

    # Use figlet to create ASCII art text banner
    figlet "$word"
done