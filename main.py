import tkinter as tk



def add(symbol):
    display.insert(tk.END, symbol)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        expression = display.get()
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Ошибка")




root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(False, False)



display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=8
)

display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    [".", "(", ")", ""]
]

for row in range(len(buttons)):
    for col in range(len(buttons[row])):

        text = buttons[row][col]

        if text == "":
            continue

        if text == "=":
            command = calculate

        elif text == "C":
            command = clear

        else:
            command = lambda x=text: add(x)

        button = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            width=5,
            height=2,
            command=command
        )

        button.grid(row=row + 1, column=col, padx=5, pady=5, sticky="nsew")



for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)



root.mainloop()

