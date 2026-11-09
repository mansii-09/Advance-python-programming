
import tkinter as tk


# Five questions about Indian geography
questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "2. Which is the longest river in India?",
        "options": ["Yamuna", "Godavari", "Ganga", "Narmada"],
        "answer": "Ganga"
    },
    {
        "question": "3. Which is the largest Indian state by area?",
        "options": ["Madhya Pradesh", "Maharashtra", "Rajasthan", "Uttar Pradesh"],
        "answer": "Rajasthan"
    },
    {
        "question": "4. Which ocean is south of India?",
        "options": ["Pacific Ocean", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean"],
        "answer": "Indian Ocean"
    },
    {
        "question": "5. Which is the highest mountain peak in India?",
        "options": ["Nanda Devi", "Kanchenjunga", "Anamudi", "Mount Abu"],
        "answer": "Kanchenjunga"
    }
]


# Store question index and score
state = {"index": 0, "score": 0, "answered": False}


# Check selected answer
def check(option):
    if state["answered"]:
        return

    correct_answer = questions[state["index"]]["answer"]

    if option == correct_answer:
        result_label.config(text="Correct!", fg="green")
        state["score"] += 1
        score_label.config(text=f"Score: {state['score']}/5")
    else:
        result_label.config(text="Wrong!", fg="red")

    state["answered"] = True

    for button in option_buttons:
        button.config(state="disabled")


# Load current question
def load_question():
    question_data = questions[state["index"]]

    question_label.config(text=question_data["question"])
    result_label.config(text="")
    score_label.config(text=f"Score: {state['score']}/5")

    state["answered"] = False

    for button, option in zip(option_buttons, question_data["options"]):
        button.config(
            text=option,
            state="normal",
            command=lambda option=option: check(option)
        )


# Move to next question
def next_question():
    if not state["answered"]:
        result_label.config(
            text="Please select an answer first.",
            fg="orange"
        )
        return

    state["index"] += 1

    if state["index"] < len(questions):
        load_question()
    else:
        show_result()


# Show final score
def show_result():
    question_label.config(text="Quiz Completed!")
    result_label.config(text="")
    score_label.config(text=f"Your score: {state['score']}/5")

    for button in option_buttons:
        button.grid_remove()

    next_button.grid_remove()
    restart_button.grid(row=6, column=0, columnspan=2, pady=10)


# Restart quiz
def restart_quiz():
    state["index"] = 0
    state["score"] = 0
    state["answered"] = False

    restart_button.grid_remove()

    for button in option_buttons:
        button.grid()

    next_button.grid(row=6, column=0, columnspan=2, pady=10)

    load_question()


# Create main window
root = tk.Tk()
root.title("Indian Geography Quiz")
root.geometry("450x350")
root.resizable(False, False)


# Heading Label
heading_label = tk.Label(
    root,
    text="Indian Geography Quiz",
    font=("Arial", 18, "bold")
)
heading_label.grid(row=0, column=0, columnspan=2, pady=12)


# Question Label
question_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    wraplength=410
)
question_label.grid(row=1, column=0, columnspan=2, pady=10)


# Four option buttons in 2x2 grid
option_buttons = []

for row in range(2):
    for column in range(2):
        button = tk.Button(root, text="", width=20, height=2)
        button.grid(row=row+2, column=column, padx=8, pady=5)
        option_buttons.append(button)


# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 11, "bold")
)
result_label.grid(row=4, column=0, columnspan=2, pady=4)


# Score Label
score_label = tk.Label(
    root,
    text="Score: 0/5",
    font=("Arial", 10)
)
score_label.grid(row=5, column=0, columnspan=2)


# Next Button
next_button = tk.Button(
    root,
    text="Next",
    width=12,
    command=next_question
)
next_button.grid(row=6, column=0, columnspan=2, pady=10)


# Restart Button
restart_button = tk.Button(
    root,
    text="Restart",
    width=12,
    command=restart_quiz
)


# Start first question
load_question()

root.mainloop()
