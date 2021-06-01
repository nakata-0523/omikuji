#cording: utf-8

import tkinter as tk
import random

def dispLabel():
    i = random.randint(1, 10)
    
    if i == 1 :
        res = "大吉"
        restex = "おめでとうございます"
    elif i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
        res = "吉"
        restex = "頑張りましょう。"
    else :
        res = "凶"
        restex = "残念でした。"
        
    tex.configure(text=res)
    restext.configure(text=restex)
root = tk.Tk()
root.geometry("300x100")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command = dispLabel)
tex = tk.Label(text="")
restext = tk.Label(text="")

lbl.pack()
btn.pack()
tex.pack()
restext.pack()
tk.mainloop()