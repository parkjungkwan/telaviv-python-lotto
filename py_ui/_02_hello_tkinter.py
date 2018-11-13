import tkinter as tk
class Label:
    def __init__(self,text,padx,pady):
        root = tk.Tk()
        label = tk.Label(root, text=text, padx=padx, pady=pady)
        label.pack()
        root.mainloop()