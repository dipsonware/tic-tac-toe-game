import tkinter as tk
from tkinter import messagebox

WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6)]              # diagonals


class TicTacToe:
    def __init__(self, root):
        self.root = root
        root.title("Tic Tac Toe")
        root.resizable(False, False)

        self.status = tk.Label(root, text="", font=("Arial", 16))
        self.status.grid(row=0, column=0, columnspan=3, pady=10)

        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                root, text="", font=("Arial", 32, "bold"),
                width=4, height=2,
                command=lambda i=i: self.on_click(i),
            )
            btn.grid(row=1 + i // 3, column=i % 3, padx=2, pady=2)
            self.buttons.append(btn)

        tk.Button(root, text="Restart", font=("Arial", 12),
                  command=self.reset).grid(row=4, column=0, columnspan=3, pady=10)

        self.reset()

    def reset(self):
        self.x_state = [0] * 9
        self.z_state = [0] * 9
        self.turn = 1  # 1 for X, 0 for O
        for btn in self.buttons:
            btn.config(text="", state="normal", fg="black")
        self.update_status()

    def update_status(self):
        name = "X" if self.turn == 1 else "O"
        self.status.config(text=f"{name}'s turn")

    @staticmethod
    def check_win(state):
        return any(all(state[i] for i in line) for line in WINS)

    def on_click(self, i):
        if self.x_state[i] or self.z_state[i]:
            return

        name = "X" if self.turn == 1 else "O"
        state = self.x_state if self.turn == 1 else self.z_state
        state[i] = 1
        self.buttons[i].config(
            text=name, fg="blue" if name == "X" else "red", state="disabled",
            disabledforeground="blue" if name == "X" else "red",
        )

        if self.check_win(state):
            self.end_game(f"{name} won the match!")
        elif all(x or z for x, z in zip(self.x_state, self.z_state)):
            self.end_game("It's a draw!")
        else:
            self.turn = 1 - self.turn
            self.update_status()

    def end_game(self, message):
        for btn in self.buttons:
            btn.config(state="disabled")
        self.status.config(text=message)
        messagebox.showinfo("Game Over", message)


if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()