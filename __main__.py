import tkinter as tk
from tkinter import messagebox
import json
import random
def main(args=None) :
    app = Application()
    app.master.title('Quiz')
    app.mainloop()
class Application(tk.Frame):
    def __init__(self, master=None):
        messagebox.showinfo('Welcome!','Welcome to PyQuiz!\nA quiz built in Python to test your general knowledge.')
        tk.Frame.__init__(self, master)
        self.grid()
        self.optionA = tk.StringVar()
        self.optionB = tk.StringVar()
        self.optionC = tk.StringVar()
        self.optionD = tk.StringVar()
        self.selected_answer = tk.StringVar()
        self.correct_answer = ""
        self.question = tk.StringVar()
        self.file = open('questions.json',"r")
        self.questions = json.loads(self.file.read())
        self.question_index = []
        self.score = tk.IntVar()
        top = self.winfo_toplevel()
        self.createWidgets(top)
        self.load_question(top)
    def new_game(self ,top) :
        self.load_question(top)
        self.score.set(0)
        
    def about(self):
        messagebox.showinfo("About " ,"Devloped by Saksham Aurora & Shashwat Bilgrami.")
    def confirm_quit(self) :
        choice = messagebox.askyesno('Quit Application' , 'Are you sure you wish to stop playing ?')
        if choice==True :
            exit(0)
        elif choice==False :
            pass
    def set_ans(self,answer):
        if answer ==1 :
            self.selected_answer = self.optionA.get()
        elif answer==2 :
            self.selected_answer = self.optionB.get()
        elif answer==3 :
            self.selected_answer = self.optionC.get()
        elif answer==4 :
            self.selected_answer = self.optionD.get()
    def validate_ans(self):
        print("In Validate answer:")
        print("selected:",self.selected_answer)
        print("Correct:",self.correct_answer)
        self.py_var = ["PY_VAR1","PY_VAR2","PY_VAR3","PY_VAR4"]
        if str(self.selected_answer) == str(self.correct_answer):
            self.score.set(int(self.score.get()) + 5)
            print("Correct!")
        elif str(self.selected_answer) in self.py_var :
            print("IN py var if")
            pass
        else :
            self.score.set(int(self.score.get()) - 5)
            print("InCorrect!")
    def load_question(self,top):
        self.validate_ans()
        randomindex = random.randint(0,len(self.questions["results"])-1)
        if randomindex not in self.question_index:
            self.question_index.append(randomindex)
            pass
        else :
            randomindex = random.randint(0,len(self.questions["results"])-1)
            self.question_index.append(randomindex)
            print("Debug:")
            print(self.questions["results"][randomindex]["question"])
        self.correct_answer = self.questions["results"][randomindex]["correct_answer"]
        self.answers = self.questions["results"][randomindex]["incorrect_answers"]
        self.answers.append(self.correct_answer)
        self.question.set(self.questions["results"][randomindex]["question"])
        length=len(self.question.get())
        width=str(100+20*length)
        top.geometry(width+"x180")
        self.optionA.set(self.answers.pop(random.randrange(len(self.answers))))
        self.optionB.set(self.answers.pop(random.randrange(len(self.answers))))
        self.optionC.set(self.answers.pop(random.randrange(len(self.answers))))
        self.optionD.set(self.answers.pop(random.randrange(len(self.answers))))
        self.radioButtonA.deselect()
        self.radioButtonB.deselect()
        self.radioButtonC.deselect()
        self.radioButtonD.deselect()
    def createWidgets(self,top):
        top.geometry("800x500")
        top.resizable(True,True)
        top.grid_columnconfigure(0,weight=1)
        top.grid_columnconfigure(9,weight=1)
        top.grid_rowconfigure(0,weight=1)
        top.grid_rowconfigure(9,weight=1)
        self.optionA.set('Hello A!')
        self.optionB.set('Hello B!')
        self.optionC.set('Hello C!')
        self.optionD.set('Hello D!')
        self.question.set('Demo Question')
        self.menu = tk.Menu(self)
        self.menubar = tk.Menu(self.menu, tearoff=0)
        self.menubar.add_command(label="New Game", command=lambda:self.new_game(top))
        self.menubar.add_command(label="About", command=self.about)
        self.menubar.add_command(label="Quit", command=self.confirm_quit)
        top.config(menu=self.menubar)
        self.quitButton = tk.Button(self, text='Quit', command=self.confirm_quit)
        self.nextButton = tk.Button(self, text='Next', command=lambda:self.load_question(top))
        self.radioButtonA = tk.Radiobutton(self,anchor='w',textvariable=self.optionA,variable = self.selected_answer,value = 'A',command = lambda: self.set_ans(1) , font=("Lucida Sans" ,15))
        self.radioButtonB = tk.Radiobutton(self,anchor='w',textvariable=self.optionB,variable = self.selected_answer,value = 'B',command = lambda: self.set_ans(2),font=("Lucida Sans" ,15))
        self.radioButtonC = tk.Radiobutton(self,anchor='w',textvariable=self.optionC,variable = self.selected_answer,value = 'C',command = lambda: self.set_ans(3),font=("Lucida Sans" ,15))
        self.radioButtonD = tk.Radiobutton(self,anchor='w',textvariable=self.optionD,variable = self.selected_answer,value = 'D',command = lambda: self.set_ans(4),font=("Lucida Sans" ,15))
        self.label_question = tk.Label(self,textvariable=self.question , font=("Lucida Sans" , 18))
        self.label_score = tk.Label(self,text='Score:')
        self.label_score_value = tk.Label(self,textvariable=self.score,anchor='e')
        self.label_question.grid(column=3,row=1,columnspan=4)
        self.label_score.grid(column=7,row=3)
        self.label_score_value.grid(column=8,row=3,sticky=tk.N+tk.S+tk.W+tk.E)
        self.radioButtonA.grid(column=2,row=4,sticky=tk.N+tk.S+tk.W+tk.E)
        self.radioButtonB.grid(column=5,row=4,sticky=tk.N+tk.S+tk.W+tk.E)
        self.radioButtonC.grid(column=2,row=6,sticky=tk.N+tk.S+tk.E+tk.W)
        self.radioButtonD.grid(column=5,row=6,sticky=tk.N+tk.S+tk.E+tk.W)
        self.quitButton.grid(column=4,row=8)
        self.nextButton.grid(column=3,row=8)
main()
