# Week 2 Assignment 
# Solved by Hemant

import tkinter as tk
from tkinter import ttk

class hemant_calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Made By Hemant")
        self.geometry("400x600")
        self.configure(bg='#121212')

        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry = ttk.Entry(self, textvariable=self.result_var, font=('Arial', 24), state='readonly', justify='right')
        entry.pack(fill='both', padx=10, pady=10)
        button_frame = tk.Frame(self, bg='#121212')
        button_frame.pack(fill='both', expand=True)

        # buttons layout add karte hai 
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]
# Week 2 Assignment 
# Solved by Hemant
        # buttons add karte hai 
        for (text, row, col) in buttons:
            if text == '=':
                button = ttk.Button(button_frame, text=text, command=self.calculate)
            else:
                button = ttk.Button(button_frame, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
            button_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        self.expression += str(char)
        self.result_var.set(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.result_var.set(result)
            self.expression = str(result)
        except Exception as e:
            self.result_var.set('Error')
            self.expression = ''

if __name__ == "__main__":
    app = hemant_calculator()
    style = ttk.Style(app)
    style.configure('TButton', font=('Arial', 18), background='#1f1f1f', foreground='#00FF00', padding=10)
    app.mainloop()
# Week 2 Assignment 
# Solved by Hemant
# Date => 10-June-2024
