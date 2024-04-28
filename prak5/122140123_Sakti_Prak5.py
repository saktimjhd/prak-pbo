#Nama   :   Sakti Mujahid Imani
#NIM    :   122140123

import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self):
        self._current_player = "X"
        self._board = [[' ' for _ in range(3)] for _ in range(3)]

    @staticmethod
    def _check_winner(board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return True
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                return True
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return True
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return True
        return False

    @staticmethod
    def _check_draw(board):
        for row in board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def switch_player(self):
        self._current_player = 'O' if self._current_player == 'X' else 'X'

    def check_winner(self):
        return self._check_winner(self._board)

    def check_draw(self):
        return self._check_draw(self._board)

    def reset_game(self):
        self._current_player = "X"
        self._board = [[' ' for _ in range(3)] for _ in range(3)]

class GameBoardGUI(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Tic Tac Toe")
        self._game = game
        self._create_widgets()
        self.bind("<Configure>", self._update_font_size)

    def _create_widgets(self):
        self._main_frame = tk.Frame(self)
        self._main_frame.pack(expand=True, padx=10, pady=10)
        
        self._buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self._buttons[i][j] = tk.Button(self._main_frame, text=" ", font=("TkDefaultFont", 20), width=10, height=4,
                                               command=lambda i=i, j=j: self._on_click(i, j))
                self._buttons[i][j].grid(row=i, column=j, padx=2, pady=2, sticky="nsew")

    def _on_click(self, row, col):
        if self._game._board[row][col] == ' ':
            self._game._board[row][col] = self._game._current_player
            self._buttons[row][col].configure(text=self._game._current_player)
            if self._game.check_winner():
                messagebox.showinfo("--PERMAINAN SELESAI--", f"Selamat pemenangnya adalah {self._game._current_player} !")
                self.quit()
            elif self._game.check_draw():
                messagebox.showinfo("--PERMAINAN SELESAI--", "Pertandingan berakhir seri !")
                self.quit() 
            else:
                self._game.switch_player()

    def _update_font_size(self, event):
        for i in range(3):
            for j in range(3):
                self._buttons[i][j].configure(font=("TkDefaultFont", 20))

if __name__ == "__main__":
    game = TicTacToeGame()
    app = GameBoardGUI(game)
    app.mainloop()