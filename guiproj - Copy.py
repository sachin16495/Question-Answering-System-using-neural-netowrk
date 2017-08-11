import tkMessageBox

import tkinter
window = tkinter.Tk();

def on_click(*args):

          sentence = ent.get('0.0', tkinter.END) #knoweldge
          text2 = quest.get('0.0', tkinter.END)  #question



window.title("hello world")

lbl = tkinter.Label(window,text = "Enter the knowedge")  #this label
ent = tkinter.Text(window,height=20, width=60)           # this knowledge
text1 = ent.get('0.0', tkinter.END)
lbl2 = tkinter.Label(window,text = "Enter the Question")   # this is also label

quest = tkinter.Text(window,height=1, width=60)                              # this question


btn = tkinter.Button(window,text = "Get Answer",command=on_click)
answer = tkinter.Label(window,text = "dfgdfgd")        # this is answer whic is calculated

lbl.pack()
ent.pack()
lbl2.pack()
quest.pack()
btn.pack()
answer.pack()

window.geometry("600x600+600+600")
window.mainloop()
