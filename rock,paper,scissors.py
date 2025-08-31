import tkinter as tk
import random

# Initialize scores and round number
player_score = 0
computer_score = 0
round_number = 1

# Function to determine winner
def play(player_choice):
    global player_score, computer_score, round_number

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    if player_choice == computer_choice:
        result_text = f"Round {round_number}: It's a Tie! Both chose {player_choice}"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        player_score += 1
        result_text = f"Round {round_number}: You Win! {player_choice} beats {computer_choice}"
    else:
        computer_score += 1
        result_text = f"Round {round_number}: You Lose! {computer_choice} beats {player_choice}"

    result_label.config(text=result_text)
    score_label.config(text=f"Score ➝ You: {player_score} | Computer: {computer_score}")
    round_number += 1

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors - Made by Shubh Kashyap")
root.geometry("500x400")
root.config(bg="#1e1e2e")  # Dark background

# Header
header_label = tk.Label(root, text="🎮 Rock Paper Scissors 🎮", 
                        font=("Arial", 20, "bold"), fg="#ffcc00", bg="#1e1e2e")
header_label.pack(pady=10)

# Subheader
credit_label = tk.Label(root, text="Made by Shubh Kashyap", 
                        font=("Arial", 12, "italic"), fg="#00ffcc", bg="#1e1e2e")
credit_label.pack()

# Instruction label
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", 
                             font=("Arial", 14), fg="white", bg="#1e1e2e")
instruction_label.pack(pady=15)


button_frame = tk.Frame(root, bg="#1e1e2e")
button_frame.pack()

rock_button = tk.Button(button_frame, text="🪨 Rock", width=12, font=("Arial", 12, "bold"),
                        bg="#4444ff", fg="white", command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="📄 Paper", width=12, font=("Arial", 12, "bold"),
                         bg="#44cc44", fg="white", command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="✂️ Scissors", width=12, font=("Arial", 12, "bold"),
                            bg="#ff4444", fg="white", command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="Round 1 begins!", font=("Arial", 14, "bold"), 
                        fg="#ffcc00", bg="#1e1e2e")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score ➝ You: 0 | Computer: 0", 
                       font=("Arial", 14), fg="white", bg="#1e1e2e")
score_label.pack()

root.mainloop()
