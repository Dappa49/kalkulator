import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN, RAISED

# Variabel untuk menyimpan hasil sementara
current_result = 0
new_input = True  # Menandakan apakah input baru dimulai setelah hasil sebelumnya

# Function to toggle fullscreen
def toggle_fullscreen(event=None):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)

# Function to exit fullscreen
def end_fullscreen(event=None):
    window.attributes('-fullscreen', False)

# Function to insert numbers and operators
def myclick(value):
    global new_input
    if new_input:  # Jika input baru, bersihkan entry terlebih dahulu
        entry.delete(0, tk.END)
        new_input = False
    if value == ',':
        entry.insert(tk.END, ',')  # Insert comma directly
    else:
        entry.insert(tk.END, value)

# Function to evaluate expression
def equal():
    global current_result, new_input
    current = entry.get().replace('^', '**').replace(',', '.')
    try:
        result = eval(current)
        current_result = result
        entry.delete(0, tk.END)
        entry.insert(0, str(result).replace('.', ','))
        new_input = True
    except Exception:
        tkinter.messagebox.showinfo("Error", "SyntaxError")

# Function to calculate percentage
def percentage():
    current = entry.get().replace(',', '.')
    try:
        entry.delete(0, tk.END)
        entry.insert(0, str(eval(current) / 100).replace('.', ','))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear entry
def clear():
    global current_result, new_input
    entry.delete(0, tk.END)
    current_result = 0
    new_input = True

# Function to delete last character
def delete_last():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Main window setup
window = tk.Tk()
window.title('AIRA MUTIARAKAYLA')
window.attributes('-fullscreen', True)
window.configure(bg='#2D2D2D')  # Background color lebih solid dan gelap

frame = tk.Frame(master=window, bg="#2D2D2D", padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

entry = tk.Entry(master=frame, relief=SUNKEN, font=("Arial", 40, "bold"), 
                 borderwidth=10, width=15, bg="#F8F8F8", fg="black")
entry.grid(row=1, column=0, columnspan=4, ipady=20, pady=20, sticky="nsew")

# Button creation
buttons = [
    ('1', 1, 2, 0), ('2', 2, 2, 1), ('3', 3, 2, 2),
    ('4', 4, 3, 0), ('5', 5, 3, 1), ('6', 6, 3, 2),
    ('7', 7, 4, 0), ('8', 8, 4, 1), ('9', 9, 4, 2),
    ('0', 0, 5, 1), (',', None, 6, 1), ('%', None, 6, 0),
    ('+', None, 2, 3), ('-', None, 3, 3), 
    ('*', None, 4, 3), ('/', None, 5, 3),
    ('C', None, 5, 0), ('DEL', None, 5, 2), 
    ('^', None, 6, 2), ('=', None, 6, 3)
]

# Button colors
button_colors = {
    'numbers': '#4CAF50',       # Hijau solid untuk angka
    'operators': '#F44336',     # Merah solid untuk operator
    'functions': '#9E9E9E',     # Abu-abu untuk fungsi (C dan DEL)
    'equal': '#3F51B5',         # Biru solid untuk tombol "="
    'comma': '#FF9800'          # Oranye untuk tombol koma
}

# Create buttons
for (text, num, row, col) in buttons:
    if text in '0123456789':
        command = lambda n=num: myclick(n)
        bg_color = button_colors['numbers']
    elif text == ',':
        command = lambda: myclick(',')
        bg_color = button_colors['comma']
    elif text == '%':
        command = percentage
        bg_color = button_colors['operators']
    elif text == '=':
        command = equal
        bg_color = button_colors['equal']
    elif text == 'C':
        command = clear
        bg_color = button_colors['functions']
    elif text == 'DEL':
        command = delete_last
        bg_color = button_colors['functions']
    elif text == '^':
        command = lambda: myclick('^')
        bg_color = button_colors['operators']
    else:
        command = lambda op=text: myclick(op)
        bg_color = button_colors['operators']

    button = tk.Button(master=frame, text=text, bg=bg_color, font=('Arial', 25, 'bold'),
                       padx=15, pady=10, borderwidth=5, relief=RAISED, command=command, fg='white')
    button.grid(row=row, column=col, pady=5, sticky='nsew')

# Configuring row and column weights
for i in range(7):
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)

# Bind keys for fullscreen
window.bind('<F11>', toggle_fullscreen)
window.bind('<Escape>', end_fullscreen)

# Run the main loop
window.mainloop()