import tkinter as tk

def click(event):
    currect =display.get()
    text=event.widget.cget("text")
    if text == "=":
        result = eval(currect)
        display.delete(0,tk.END)
        display.insert(tk.END, result)
    elif text== "C":
        display.delete(0,tk.END)
    else:
        display.insert(tk.END,text)



window= tk.Tk()
window.title("calulator")

display=tk.Entry(window,font=("arial",25),justify="right")
display.pack(fill=tk.X,padx=20,pady=20)
btn_frame= tk.Frame(window)
btn_frame.pack()

button_label=[
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "C", "0", "/", "=",
    
]


i=0
for label in button_label:
    button= tk.Button(btn_frame,text=label,font=("arial",18),padx=20,pady=20)
    button.grid(row=i//4,column=i%4,padx=10,pady=10)
    button.bind("<Button-1>",click)
    i=i+1

window.mainloop()