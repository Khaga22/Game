
#sneh acharya


import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("Number Guessing Game")

# Set the starting number to be guessed
number = random.randint(1, 100)

# Create a label to display the instructions
instructions = tk.Label(text="I'm thinking of a number between 1 and 100. Can you guess what it is?", font=("Helvetica", 16))
instructions.pack()

# Create an entry box for the user to enter their guess
guess_entry = tk.Entry()
guess_entry.pack()

# Create a function to check the user's guess
def check_guess():
  # Get the user's guess from the entry box
  guess = int(guess_entry.get())
  
  # Check if the guess is correct
  if guess == number:
    # If the guess is correct, display a "You Win!" message and exit the game
    result_label = tk.Label(text="You Win!", font=("Helvetica", 24))
    result_label.pack()
    window.destroy()
  elif guess < number:
    # If the guess is too low, display a "Too low" message and clear the entry box
    result_label = tk.Label(text="Too low. Try again.", font=("Helvetica", 16))
    result_label.pack()
    guess_entry.delete(0, "end")
  else:
    # If the guess is too high, display a "Too high" message and clear the entry box
    result_label = tk.Label(text="Too high. Try again.", font=("Helvetica", 16))
    result_label.pack()
    guess_entry.delete(0, "end")

# Create a button to submit the user's guess
guess_button = tk.Button(text="Guess", command=check_guess)
guess_button.pack()

# Run the main loop
window.mainloop()
staticmethod
