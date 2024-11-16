import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "Bin":
        try:
            num = int(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, bin(num)[2:])
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Input")
    elif text == "Hex":
        try:
            num = int(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, hex(num)[2:])
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Input")
    elif text == "Oct":
        try:
            num = int(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, oct(num)[2:])
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Input")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    'Bin', 'Hex', 'Oct'
]

row = 1
col = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=10)
    button.grid(row=row, column=col, padx=5, pady=5)

    button.bind("<Button-1>", on_click)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()