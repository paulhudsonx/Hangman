from tkinter import *
import tkinter.messagebox
from Hangman import *

class MainScript():

    def main(self):
        self.root = Tk()
        self.root.geometry("320x200+200+100")
        app = HangmanUI(self.root)
        self.root.mainloop()


class HangmanUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        answer = tkinter.messagebox.askquestion("Are you sure?", "Do you really want to quit?")
        if answer == "yes":
            self.parent.destroy()

    def initUI(self):
        self.parent.title("Hangman")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        # ******* Menu *******

        new_game_button = Button(frame1, text="New Game", command=text_UI.play_game)
        new_game_button.pack(side=LEFT, padx=2, pady=2)
        exit_button = Button(frame1, text="Exit", command=self.on_closing)
        exit_button.pack(side=LEFT, padx=2, pady=2)


        frame2 = Frame(self)
        frame2.pack(fill=X)

        guesses_left = Label(frame2, text="You have 8 guesses left", bd=1, anchor=W)
        guesses_left.pack(side=LEFT, padx=5, pady=10)

        frame_masked_word = Frame(self)
        frame_masked_word.pack(fill=X)

        masked_word = Label(frame_masked_word, text="_ _ _ _ _ _ _ _", bd=1,anchor=W)
        masked_word.pack(side=LEFT, padx=5, pady=10)


        frame3 = Frame(self)
        frame3.pack(fill=X)

        frame3x = Frame(frame3)
        frame3x.pack(fill=X)

        lbl1 = Label(frame3x, text="Guess", width=6)
        lbl1.pack(side=LEFT)

        entry1 = Entry(frame3x)
        entry1.pack(side=LEFT, fill=X, expand=True)

        guess_button = Button(frame3x, text="Guess")
        guess_button.pack(side=LEFT)

        frame5 = Frame(self)
        frame5.pack(fill=X)

        notifications = Label(frame5, text="Letter X is incorrect", bd=1, anchor=W)
        notifications.pack(side=LEFT, padx=5, pady=20)



main = MainScript()

main.main()