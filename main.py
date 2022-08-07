from calendar import c
import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk

width = 280
height= 350
x = 100                 # x position
y = 100                 # y position

# GUI Window
window = tk.Tk()                    #creates a GUI
window.title('Python Calculator')               # changes the title
window.configure(bg='#008080')
window.geometry(f'{width}x{height}+{x}+{y}')
window.iconbitmap('images/calculator.ico')                     #changes the icon
window.resizable(False, False)                # fixes the GUI window size

# Frames
screen_frame = tk.Frame(window, width=300)
screen_frame.pack(padx=5, pady=10)

button_frame = tk.Frame(window, width=300, height=120)
button_frame.pack()

# Font 
style = font.Font(family='Helvetica')

# Input
input = tk.StringVar()
input_screen = tk.Entry(screen_frame, textvariable=input, width=38)
input_screen.config(state='disable')                                    # disable access to the input screen
input_screen.pack()

# Functions
def insert_input(x):
    """
        Allows the user to insert a number, decimal point, and an operation (+,-,*,/)
    """
    input_screen.config(state='normal')
    input_screen.insert(len(input.get()), x)
    input_screen.config(state='disable')


    

# Buttons
one_btn = tk.Button(button_frame, text="1", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("1"))
one_btn.grid(column=0, row=0, padx=5, pady=5)

two_btn = tk.Button(button_frame, text="2", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("2"))
two_btn.grid(column=1, row=0, padx=5, pady=5)

three_btn = tk.Button(button_frame, text="3", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("3"))
three_btn.grid(column=2, row=0, padx=5, pady=5)

add_btn =tk.Button(button_frame, text="+", bg='#008080', fg='#fff', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("+"))
add_btn.grid(column=3, row=0, padx=5, pady=5)

four_btn = tk.Button(button_frame, text="4", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("4"))
four_btn.grid(column=0, row=1, padx=5, pady=5)

five_btn = tk.Button(button_frame, text="5", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("5"))
five_btn.grid(column=1, row=1, padx=5, pady=5)

six_btn = tk.Button(button_frame, text="6", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("6"))
six_btn.grid(column=2, row=1, padx=5, pady=5)

sub_btn =tk.Button(button_frame, text="-", bg='#008080', fg='#fff', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("-"))
sub_btn.grid(column=3, row=1, padx=5, pady=5)

seven_btn = tk.Button(button_frame, text="7", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("7"))
seven_btn.grid(column=0, row=2, padx=5, pady=5)

eight_btn = tk.Button(button_frame, text="8", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("8"))
eight_btn.grid(column=1, row=2, padx=5, pady=5)

nine_btn = tk.Button(button_frame, text="9", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("9"))
nine_btn.grid(column=2, row=2, padx=5, pady=5)

mult_btn = tk.Button(button_frame, text="x", bg='#008080', fg='#fff', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("*"))
mult_btn.grid(column=3, row=2, padx=5, pady=5)

decimal_btn = tk.Button(button_frame, text=".", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("."))
decimal_btn.grid(column=0, row=3, padx=5, pady=5)

zero_btn = tk.Button(button_frame, text="0", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("0"))
zero_btn.grid(column=1, row=3, padx=5, pady=5)

equal_btn = tk.Button(button_frame, text="=", bg='#FFF', fg='#008080', width=2, height=1, font=style, padx=8, pady=5)
equal_btn.grid(column=2, row=3, padx=5, pady=5)

div_btn = tk.Button(button_frame, text="/", bg='#008080', fg='#fff', width=2, height=1, font=style, padx=8, pady=5, command=lambda:insert_input("/"))
div_btn.grid(column=3, row=3, padx=5, pady=5)

clear_btn = tk.Button(button_frame, text="Clear", bg='#fff', fg='#008080', width=7, height=1, font=style, padx=8, pady=5, command=lambda:input.set(""))
clear_btn.grid(column=0, row=5, columnspan=2, padx=5, pady=5)

exit_btn = tk.Button(button_frame, text="Exit", bg='#fff', fg='#008080', width=7, height=1, font=style, padx=8, pady=5, command=lambda:window.quit())
exit_btn.grid(column=2, row=5, columnspan=2, padx=5, pady=5)

window.mainloop()           # makes window visible