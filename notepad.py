from tkinter import Tk, Text, END, Menu
from tkinter.simpledialog import askstring
import tkinter.messagebox as tsmg


def save() -> None:
    global l1
    if l1 == '':
        saveas()
    else:
        with open(l1, 'a') as f:
            s = t1.get('1.0', 'end-1c')
            f.write(s)


def saveas() -> None:
    l1: str | None = askstring('Save As', 'Enter file name with extension')
    if l1:
        with open(l1, 'a') as f:
            s: str = t1.get('1.0', 'end-1c')
            f.write(s)


def openFile() -> None:
    l2: str | None = askstring(
        'Open File', 'Enter file name with extension to open')
    if l2:
        with open(l2) as f:
            s1 = f.read()
            t1.insert(END, s1)


def newFile() -> None:
    n: bool = tsmg.askyesno('Save', 'Do you want to save this file')
    if n:
        save()
    else:
        t1.delete('1.0', 'end')


root = Tk()
l1 = ''
root.geometry('1920x1080')
root.title('Notepad.exe')
t1 = Text(root, x=0, y=0, width=1000, height=800,  # type: ignore
          font=("Fira Code Retina", 18))
t1.pack()
m1 = Menu(root)
m1.add_command(label='Save', command=save)
m1.add_command(label='Save As', command=saveas)
m1.add_command(label='Open file', command=openFile)
m1.add_command(label='New file', command=newFile)
root.config(menu=m1)
root.mainloop()
