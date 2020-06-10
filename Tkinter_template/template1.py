import tkinter as tk

root = tk.Tk()

frame_a = tk.Frame(root)
frame_a.place(relx=0.5, rely=0.4, relwidth=0.7, relheight=0.1, anchor='n')

L1 = tk.Label(frame_a,text="User Name")
L1.pack(side="left")
E1 = tk.Entry(frame_a, bd =5)
E1.pack(side="right")


frame_b = tk.Frame(root)
frame_b.place(relx=0.5, rely=0.6, relwidth=0.7, relheight=0.1, anchor='n')


L1 = tk.Label(frame_b,text="Password")
L1.pack(side="left")
E1 = tk.Entry(frame_b, bd =5)
E1.pack(side="right")

frame_c = tk.Frame(root)
frame_c.place(relx=0.5, rely=0.8, relwidth=0.7, relheight=0.1, anchor='n')

B = tk.Button(frame_c, text ="Log In", command = "Command")
B.pack(side="bottom")
root.mainloop()