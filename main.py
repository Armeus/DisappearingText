import tkinter as tk
import re

FONT = ("Helvetica", 16)


class App(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        parent.bind('<KeyPress>', self.on_key_press)

        self.text = tk.Text(width=50, height=15, font=FONT, highlightthickness=0, borderwidth=0)
        self.text.pack()
        self.text.focus_set()

        self.label = tk.Label(text='0 words', background='white')
        self.label.pack()

        self.time_left = 6
        self.timer = None

    # When any character key is pressed
    # The countdown time is started and text color is reset to black
    # Word count label is updated with current word count
    def on_key_press(self, event):
        if event.char != '' and event.keysym != 'BackSpace':
            if self.time_left > 5:
                self.count_down()
            self.time_left = 5
            self.text.config(foreground='#000000')

            words = self.text.get('1.0', 'end-1c')
            wordcount = len(re.findall('\w+', words))
            self.label.config(text=f'Words: {wordcount}')

    # Timer Utility
    # When timer reach 0, text is deleted
    def count_down(self):
        if self.time_left > 0:
            self.timer = tk.Frame.after(self, 1000, self.count_down)
            self.time_left -= 1
            if self.time_left == 3:
                self.text.config(foreground='#800000')
            elif self.time_left == 2:
                self.text.config(foreground='#bf0000')
            elif self.time_left <= 1:
                self.text.config(foreground='#ff0000')
        else:
            self.text.delete('0.0', tk.END)
            tk.Frame.after_cancel(self, self.timer)


def main():
    root = tk.Tk()
    root.title("Disappearing Text")
    root.minsize(width=500, height=300)
    root.config(padx=20, pady=20, background='white')
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
