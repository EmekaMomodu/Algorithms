#!/bin/bash

# Function to draw the word
draw_word() {
  local word=$1
  local font_size=${2:-10}
  local font_style=${3:-standard}

  # Use figlet to draw the word
  figlet -f $font_style -s -w 100 -c "$word"
}

# Main game loop
while true; do
  # Ask the user for an input word
  read -p "Enter a word to draw (or 'quit' to exit): " input_word

  # Check if the user wants to quit
  if [ "${input_word,,}" = "quit" ]; then
    break
  fi

  # Draw the word
  draw_word "$input_word"

  # Ask the user if they want to continue
  read -p "Do you want to draw another word? (y/n): " response
  if [ "${response,,}" != "y" ]; then
    break
  fi
done

echo "Thanks for playing!"