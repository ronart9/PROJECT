import tkinter as tk
import random

class MiniGame(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("MiniGame")
        self.number = random.randint(1, 100)
        self.num_guesses = 0

        self.guess_label = tk.Label(self, text="Guess a number between 1 and 100:")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        # Bind the "Return" key to check_guess method
        self.guess_entry.bind('<Return>', lambda event: self.check_guess())

    def check_guess(self):
        guess = int(self.guess_entry.get())
        self.num_guesses += 1

        if guess == self.number:
            self.result_label.configure(
                text="Congratulations! You guessed the number in " + str(self.num_guesses) + " guesses.")
            #self.submit_button.configure(state="disabled")
            #self.guess_entry.configure(state="disabled")

        elif guess < self.number:
            self.result_label.configure(text="Too low! Guess again.")
        else:
            self.result_label.configure(text="Too high! Guess again.")

        self.guess_entry.delete(0, 'end')


