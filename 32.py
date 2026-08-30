import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x500")
root.resizable(False, False)

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Score variables
player_score = 0
computer_score = 0
draw_score = 0


# Function to play the game
def play_game(player_choice):
    global player_score, computer_score, draw_score

    # Computer randomly selects a choice
    computer_choice = random.choice(choices)

    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a Draw!"
        draw_score += 1

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or
        (player_choice == "Paper" and computer_choice == "Rock")
        or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    # Display the choices
    player_label.config(text=f"You chose: {player_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    # Display the result
    result_label.config(text=result)

    # Update scores
    score_label.config(
        text=f"Your Score: {player_score}    "
             f"Computer: {computer_score}    "
             f"Draws: {draw_score}"
    )


# Function to reset the game
def reset_game():
    global player_score, computer_score, draw_score

    player_score = 0
    computer_score = 0
    draw_score = 0

    player_label.config(text="You chose: ")
    computer_label.config(text="Computer chose: ")
    result_label.config(text="Choose Rock, Paper or Scissors")
    score_label.config(
        text="Your Score: 0    Computer: 0    Draws: 0"
    )


# Title
title_label = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=20)

# Instructions
instruction_label = tk.Label(
    root,
    text="Choose one:",
    font=("Arial", 14)
)
instruction_label.pack(pady=5)

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

# Rock button
rock_button = tk.Button(
    button_frame,
    text="Rock",
    font=("Arial", 14),
    width=10,
    command=lambda: play_game("Rock")
)
rock_button.grid(row=0, column=0, padx=5)

# Paper button
paper_button = tk.Button(
    button_frame,
    text="Paper",
    font=("Arial", 14),
    width=10,
    command=lambda: play_game("Paper")
)
paper_button.grid(row=0, column=1, padx=5)

# Scissors button
scissors_button = tk.Button(
    button_frame,
    text="Scissors",
    font=("Arial", 14),
    width=10,
    command=lambda: play_game("Scissors")
)
scissors_button.grid(row=0, column=2, padx=5)

# Player choice
player_label = tk.Label(
    root,
    text="You chose: ",
    font=("Arial", 13)
)
player_label.pack(pady=10)

# Computer choice
computer_label = tk.Label(
    root,
    text="Computer chose: ",
    font=("Arial", 13)
)
computer_label.pack(pady=10)

# Result
result_label = tk.Label(
    root,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 18, "bold")
)
result_label.pack(pady=15)

# Score
score_label = tk.Label(
    root,
    text="Your Score: 0    Computer: 0    Draws: 0",
    font=("Arial", 12)
)
score_label.pack(pady=10)

# Reset button
reset_button = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 12),
    width=15,
    command=reset_game
)
reset_button.pack(pady=20)

# Start the GUI
root.mainloop()