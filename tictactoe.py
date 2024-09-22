import random
import tkinter as tk
import tkinter.ttk as ttk

winning_conditions: list[set[int]] = [
    {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
players: dict[str, set[int]] = {'X': set(), 'O': set()}
turn: str = random.choice(('X', 'O'))


def reset() -> None:
    global turn, players
    pb['value'] = 0
    turn = random.choice(('X', 'O'))
    players = {'X': set(), 'O': set()}
    for button in buttons[1:]:
        button['text'] = ''  # type: ignore


def check(x: tk.Event) -> None:
    global turn
    btn: tk.Button = x.widget
    if btn['text'] == '':
        btn['fg'] = 'red' if turn == 'X' else 'orange'
        pb['value'] += 100/9
        for idx, button in enumerate(buttons):
            if btn is button:
                players[turn].add(idx)
        btn['text'] = 'X' if turn == 'X' else 'O'
        for condition in winning_conditions:
            if condition <= players[turn]:
                print(f'{turn} won the game')
                reset()
        turn = 'O' if turn == 'X' else 'X'


root = tk.Tk()
root.title('Tic-Tac-Toe.exe')  # type: ignore
root.config()
root.geometry('600x800')
buttons: list[tk.Button | None] = [None]*10
for i in range(1, 10):
    buttons[i] = tk.Button(root, font=('Ink Free', 80))
    buttons[i].bind('<Button-1>', check)  # type: ignore
    buttons[i].place(x=(i-1) % 3*200, y=((i-1)//3)*200,  # type: ignore
                     width=200, height=200)
pb = ttk.Progressbar(root)
pb.place(x=0, y=620, width=600, height=40)
reset_btn = tk.Button(root, text='Reset', font=(
    'JetBrains Mono', 40), command=reset)
reset_btn.place(x=200, y=680, width=200, height=75)
root.mainloop()
