import tkinter as tk

def ftc():
    fah = entTempF.get()
    cel = (5/9)*(float(fah)-32)
    lblResult1["text"] = f"{round(cel,2)} \N{DEGREE CELSIUS}"

def ctf():
    cels = entTempC.get()
    fahr = ((float(cels)*(9/5))+32)
    lblResult2["text"] = f"{round(fahr,2)} \N{DEGREE FAHRENHEIT}"

window = tk.Tk()
window.title("Temperature Converter")

frm_entry1 = tk.Frame(master=window)
frm_entry2 = tk.Frame(master=window)

entTempF = tk.Entry(master=frm_entry1, width=25)
lblTempF = tk.Label(master=frm_entry1, text="\N{DEGREE FAHRENHEIT}")
entTempF.grid(row=0, column=0, sticky="e")
lblTempF.grid(row=0, column=1, sticky="w")

entTempC = tk.Entry(master=frm_entry2, width=25)
lblTempC = tk.Label(master=frm_entry2, text="\N{DEGREE CELSIUS}")
entTempC.grid(row=1, column=0, sticky="e")
lblTempC.grid(row=1, column=1, sticky="w")

btnConv1 = tk.Button(
master=window,
text="\N{RIGHTWARDS BLACK ARROW}",
command=ftc
)
btnConv2 = tk.Button(
master=window,
text="\N{RIGHTWARDS BLACK ARROW}",
command=ctf
)
lblResult1 = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
lblResult2 = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")
frm_entry1.grid(row=0, column=0, padx=10)
frm_entry2.grid(row=1, column=0, padx=10)
btnConv1.grid(row=0, column=1, pady=10)
btnConv2.grid(row=1, column=1, pady=10)
lblResult1.grid(row=0, column=2, padx=10)
lblResult2.grid(row=1, column=2, padx=10)

window.mainloop()
