import tkinter as tk


class StopWatch:
    def __init__(self, root: tk.Tk) -> None:
        self.root: tk.Tk = root
        self.elapsed_time = 0
        self.running = False

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()

        self.start_button = tk.Button(
            root, text="Start", command=self.start_stopwatch)
        self.start_button.pack()

        self.reset_button = tk.Button(
            root, text="Reset", command=self.reset_stopwatch)
        self.reset_button.pack()

        self.update_time()

    def update_time(self) -> None:
        hours = int(self.elapsed_time / 3600)
        minutes = int((self.elapsed_time % 3600) / 60)
        seconds = int(self.elapsed_time % 60)
        time_string: str = f"{hours:02}:{minutes:02}:{seconds:02}"
        self.label.config(text=time_string)
        if self.running:
            self.elapsed_time += 1
        self.root.after(1000, self.update_time)

    def start_stopwatch(self) -> None:
        self.running: bool = not self.running
        if self.running:
            self.start_button.config(text="Stop")
        else:
            self.start_button.config(text="Start")

    def reset_stopwatch(self) -> None:
        self.elapsed_time = 0
        self.running = False
        self.start_button.config(text="Start")
        self.update_time()


root = tk.Tk()
stopwatch = StopWatch(root)
root.mainloop()


# Creating stopwatch using GUI
# import tkinter as tk
# from time import sleep


# def start():
#     global m, s, ms
#     while True:
#         sleep(0.1)
#         ms += 1
#         if ms == 10:
#             s += 1
#             ms = 0
#         if s == 60:
#             m += 1
#             s = 0
#         timelabel.config(text= f'{m:02d}:{s:02d}.{ms}')


# root = tk.Tk()
# m, s, ms = 0, 0, 0
# root.geometry('400x400')
# root.maxsize(400, 400)
# root.minsize(400, 400)
# root.title('Stopwatch')
# l = tk.StringVar()
# timelabel = tk.Label(root,
#                      font='times 50 bold', bg='black', fg='green', text=f'{m:02d}:{s:02d}.{ms}')
# start_button = tk.Button(root, text='start', command=start)
# start_button.place(x=50, y=300, width=50, height=50)
# timelabel.place(x=20, y=20, width=360, height=100)
# root.mainloop()
