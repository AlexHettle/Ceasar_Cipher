from tkinter import *
letters="abcdefghijklmnopqrstuvwxyz"
#Takes in a phrase and a shift int and shifts every letter in the phrase
def begin_cipher(phrase_entry,shift_entry):
    try:
        shift=int(shift_entry.get())
        phrase=str(phrase_entry.get())
        shift_entry.delete(0,END)
        phrase_entry.delete(0,END)
        new_phrase=""
        for i in phrase:
            if i.lower() in letters:
                place=(shift+letters.find(i.lower()))%26
                if(i.isupper()):
                    new_phrase+=letters[place].upper()
                else:
                    new_phrase+=letters[place]
            else:
                new_phrase+=i
        Ciphered.configure(text=new_phrase)
    except:
        Ciphered.configure(text="invalid entry, please enter a valid phrase and a valid integer")
#This chunk of code sets up the GUI
window=Tk()
window.resizable(False, False)
window.title("Ceasar Cipher")
window.geometry("700x220")
window.configure(bg="#9de8f2")
title=Label(text="Ceasar Cipher",font=("Times new Roman",20),bg="#9de8f2")
title.pack(side=TOP)
Ciphered=Label(text="Please enter the phrase you want to cipher and the amount you want to shift it by",font=("Times new Roman",20),wraplength=300,justify=LEFT,bg="#9de8f2")
Ciphered.place(x=20,y=50)
phrase_entry=Entry(window,width=30,borderwidth=10)
phrase_entry.place(x=500,y=100)
phrase_label=Label(text="enter phrase:",font=("Times new Roman",20),bg="#9de8f2")
phrase_label.place(x=350,y=100)
shift_label=Label(text="enter shift:",font=("Times new Roman",20),bg="#9de8f2")
shift_label.place(x=350,y=130)
shift_entry=Entry(window,width=10,borderwidth=10)
shift_entry.place(x=500,y=130)
the_button=Button(text="ENCRYPT",font=("Times new Roman",10),padx=9,command=lambda: begin_cipher(phrase_entry,shift_entry))
the_button.place(x=500,y=167)
window.mainloop()
