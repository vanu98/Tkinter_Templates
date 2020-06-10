import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1) 

languages = [
    ("Bread",1),
    ("Butter",2),
    ("Cheese",3),
    ("Milk",4),
    ("Water",5)
]

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="""Grocery:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root, 
                  text=language,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


root.mainloop()