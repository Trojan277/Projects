from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = Tk()
root.title("English Dictionary")
root.iconbitmap('C:/Users/kaan_/Desktop/PyProjects/Python Projects/englishDictionary/icon.ico')

root.geometry('800x600')
root.configure(bg='blue')

def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))


Label(root, text = "Welcome to Trojan's English Dictionary Program", font=('Helvetica 20 bold'), fg = "purple3").pack(pady = 10)

frame = Frame(root)
Label(frame, text = "Enter Word: ", font=('Helvetica 20 bold')).pack(side = LEFT)
word = Entry(frame, font=('Helvatica 20 bold'))
word.pack()
frame.pack(pady=10)



frame1 = Frame(root)
Label(frame1, text="meaning:- ", font=('Helvetica 10 bold')).pack(side = LEFT)
meaning = Label(frame1, text = "", font=('Helvetica 10 bold'))
meaning.pack()
frame1.pack(pady=10)



frame2 = Frame(root)
Label(frame2, text="Synonym:- ", font=('Helvetica 10 bold')).pack(side = LEFT)
synonym = Label(frame2, text = "   ", font=('Helvetica 10 bold'))
synonym.pack()
frame2.pack(pady=10)


frame3 = Frame(root)
Label(frame3, text = 'antonym:- ', font=('Helvetica 10 bold')).pack(side = LEFT)
antonym = Label(frame3, text ="", font=('Helvetica 10 bold'))
antonym.pack(side = LEFT)
frame3.pack(pady=10)

Button(root, text='Submit', font=('Helvetica 15 bold'), command = dict, fg = 'green').pack()
Button(root, text = 'Exit', font=('Helvetica 15 bold'), command= quit, fg = 'red').pack()

root.mainloop()