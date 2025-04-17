from tkinter import*
import json
import os

import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist


class Setting:
    def __init__(self, window):
        self.window = window
        #===========Color==============
        self.textColor = StringVar()
        self.BG = StringVar()
        self.darkOrange = StringVar()
        self.buttonBG = StringVar()
        self.buttonText = StringVar()

        self.textColor.set("White")
        self.BG.set("#333230")
        self.darkOrange.set("#d95008")
        self.buttonBG.set("White")
        self.buttonText.set("Black")

        #===========Language==============
        self.languageOptions = ["English", "Persian", "Indian"]
        self.languageSelectedOption = StringVar(value=self.languageOptions[0])

class StartPage:
    def __init__(self, window, people, setting):
        self.people = people
        self.window = window
        self.setting = setting

        self.window.configure(bg=self.setting.BG.get())

        frameTitle = Frame(self.window, bg=self.setting.textColor.get())
        frameTitle.pack(fill=X)
        labelTitle = Label(frameTitle, text="SUMMARIZER", font=('Arial', 30, 'bold'), bg=self.setting.darkOrange.get())
        labelTitle.pack(fill=X)

        frameLoginOrCreat = Frame(self.window)
        frameLoginOrCreat.pack(pady=20)  
        Button(frameLoginOrCreat, text="Login", command=self.loginPage, width=15).pack(side=LEFT, padx=10)
        Button(frameLoginOrCreat, text="Create Account", command=self.creatAccountPage, width=15).pack(side=LEFT, padx=10)

        frameDeveloper = Frame(self.window).pack()
        Label(frameDeveloper, text="Developed By Parsa Asil", font="Arial, 8").pack()


    
    def loginPage(self):
        clearWindow(self.window)
        Loggin(self.window, self.people, self.setting)

    def creatAccountPage(self):
        clearWindow(self.window)
        CreateAccount(self.window, self.people, self.setting)

class Loggin(StartPage):
    def __init__(self, window, people, setting):
        self.people = people
        self.window = window
        self.setting = setting
        
        frame = Frame(self.window, bg=self.setting.darkOrange.get(), pady=10)
        frame.pack(fill=X)
        label = Label(frame, text='Login', fg="white", bg=self.setting.darkOrange.get(), font=("Arial", 30))
        label.pack()

        frameForm = Frame(self.window)
        frameForm.pack()

        labelFName = Label(frameForm, text="First Name: ")
        labelFName.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entryFName = Entry(frameForm)
        self.entryFName.grid(row=0, column=1, padx=5, pady=5)

        labelLName = Label(frameForm, text="Last Name: ")
        labelLName.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entryLName = Entry(frameForm)
        self.entryLName.grid(row=1, column=1, padx=5, pady=5)

        frameB = Frame(self.window)
        frameB.pack()
        buttonSubmit = Button(frameB, text="Login", command=self.proccessLoginData)
        buttonSubmit.pack()

        frameM = Frame(self.window)
        frameM.pack()
        message = Message(frameM, text="Please enter your login information", font=('Arial', 8), width=200)
        message.pack()

        frameBack = Frame(self.window).pack()
        Button(frameBack, text="Back", command=self.backButton).pack(side=LEFT)


    
    def proccessLoginData(self):
    
        FName = self.entryFName.get()
        upperFName = FName.upper()

        LName = self.entryLName.get()
        upperLName = LName.upper()

        found = False

        for person in self.people:
            if person["first_name"] == upperFName and person["last_name"] == upperLName:
                print("Logged in")
                found = True

                clearWindow(self.window)
                MainSlide(self.window, self.setting, self.people)

                break
            
        if not found:
            frameLoginMessage = Frame(self.window, bg='red')
            frameLoginMessage.pack(fill=X)
            loginMessage = Message(frameLoginMessage, text="Your information are not correct", width=400, bg="red", fg="white")
            loginMessage.pack(fill=X)  
    
    def backButton(self):
        clearWindow(self.window)
        StartPage(self.window, self.people, self.setting)

class CreateAccount(StartPage):
    def __init__(self, window, people, setting):
        self.people = people
        self.window = window
        self.setting = setting
        
        frame = Frame(self.window, bg=self.setting.darkOrange.get(), pady=10)
        label = Label(frame, text='Create Account', fg="white", bg=self.setting.darkOrange.get(), font=("Arial", 30))
        frame.pack(fill=X)
        label.pack()

        frameForm = Frame(self.window)
        frameForm.pack()

        labelFName = Label(frameForm, text="First Name: ")
        labelFName.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entryFName = Entry(frameForm)
        self.entryFName.grid(row=0, column=1, padx=5, pady=5)

        labelLName = Label(frameForm, text="Last Name: ")
        labelLName.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entryLName = Entry(frameForm)
        self.entryLName.grid(row=1, column=1, padx=5, pady=5)

        frameB = Frame(self.window)
        frameB.pack()
        buttonSubmit = Button(frameB, text="Submit", command=self.submitData)
        buttonSubmit.pack()

        frameM = Frame(self.window)
        frameM.pack()
        message = Message(frameM, text="Please enter your information", font=('Arial', 8), width=200)
        message.pack()

        frameBack = Frame(self.window).pack()
        Button(frameBack, text="Back", command=self.backButton).pack(side=LEFT)

    
    def submitData(self):
    
        FName = self.entryFName.get()
        upperFName = FName.upper()

        LName = self.entryLName.get()
        upperLName = LName.upper()

        self.people.append({"first_name": upperFName, "last_name": upperLName})
        savePeopleToFile(self.people)

        clearWindow(self.window)
        Loggin(self.window, self.people, self.setting)

    def backButton(self):
        clearWindow(self.window)
        StartPage(self.window, self.people, self.setting)

class MainSlide(Loggin):
    def __init__(self, window, setting, people):
        self.window = window
        self.setting = setting
        self.people = people

        frameTitle = Frame(self.window, bg=self.setting.darkOrange.get(), width=400, height=50)
        frameTitle.pack(fill=X)
        labelTitle = Label(frameTitle, text="SUMMARIZER", font=('Arial', 30, 'bold'), bg=self.setting.darkOrange.get())
        labelTitle.pack(side=LEFT, fill=BOTH)

        self.darkModeVar = StringVar(value='Dark')
        self.darkRadio = Radiobutton(
            frameTitle,
            text="Dark",
            variable=self.darkModeVar,
            value="Dark",
            command=self.LightMode,
            bg=self.setting.darkOrange.get(),
            fg= self.setting.textColor.get()
        )
        self.darkRadio.pack(side=LEFT, fill=BOTH, padx=20)
        self.lightRadio = Radiobutton(
            frameTitle,
            text="Light",
            variable=self.darkModeVar,
            value="Light",
            command=self.LightMode,
            bg=self.setting.darkOrange.get(),
            fg= self.setting.textColor.get()
        )
        self.lightRadio.pack(side=LEFT, fill=BOTH)

        self.languageMenu = OptionMenu(
        frameTitle,
        self.setting.languageSelectedOption,
        *self.setting.languageOptions,
        command=self.changeLanguage
        )
        self.languageMenu.config(bg=self.setting.darkOrange.get(), fg=self.setting.textColor.get())  # Set your colors
        self.languageMenu.pack(side=RIGHT, fill=BOTH)

        frameInputText = Frame(self.window)
        frameInputText.pack(pady= 15)
        self.textBox = Text(frameInputText,height=10, width=50) 
        self.textBox.pack()
        self.textBox.insert(END, "You can type here...\nSupports multiple lines.")
        self.submitButton = Button(frameInputText, text="Submit", command=self.startSummarizing)
        self.submitButton.pack()

        self.frameLogOutSetting = Frame(self.window, bg="White")
        self.frameLogOutSetting.pack(anchor="w", padx=10)  # Align to the left with some padding
        self.logOutButton = Button(self.frameLogOutSetting,text="Log Out", command=self.logOut, highlightbackground= self.setting.BG.get(), 
                                   fg=self.setting.buttonText.get(), bg=self.setting.buttonBG.get())
        self.logOutButton.pack(side=LEFT)

        

    def logOut(self):
        clearWindow(self.window)

        self.setting.BG.set("#333230")
        self.setting.textColor.set("White")
        self.setting.buttonBG.set("yellow")
        self.setting.buttonText.set("Black")

        StartPage(self.window, self.people, self.setting)

    def startSummarizing(self):
        content = self.textBox.get("1.0",END)#text box return
        TextSummarizer(content, self.textBox)

    def LightMode(self):
        getLightMode = self.darkModeVar.get()
        
        if getLightMode == "Light":
            self.setting.BG.set("#FCECDD")
            self.setting.textColor.set("Black")
            self.setting.buttonBG.set("red")
            self.setting.buttonText.set("Black")
            
        else:
            self.setting.BG.set("#333230")
            self.setting.textColor.set("White")
            self.setting.buttonBG.set("yellow")
            self.setting.buttonText.set("Black")

        self.window.configure(bg=self.setting.BG.get())
        #self.submitButton.configure(highlightbackground=self.setting.BG.get())
        self.logOutButton.configure(highlightbackground=self.setting.BG.get(), fg=self.setting.buttonText.get(), bg="lightblue")



    def changeLanguage(self, selected=None):
        self.textBox.delete("1.0", END)

        if selected == "English":
            self.textBox.insert(END, "You can type here...\nSupports multiple lines.")
        elif selected == "Persian":
            self.textBox.insert(END, "میتوانید اینجا تایپ کنید...\nاز چند خط پشتیبانی میکند.")
        elif selected == "Indian":
            self.textBox.insert(END, "यहाँ टाइप कर सकते हैं...\nयह कई लाइनों का समर्थन करता है।")

class TextSummarizer(MainSlide):
    def __init__(self, text, textBox):

        self.text = text
        self.textBox = textBox

        returnSummary = self.text_summarizer(self.text)

        self.textBox.delete("1.0", END)
        self.textBox.insert(END, returnSummary)


    def text_summarizer(self, text): #"Hello world. This is a test. How are you?"
        # Text into sentences
        sentences = sent_tokenize(text)  #['Hello world.', 'This is a test.', 'How are you?']

        # Text into words
        words = word_tokenize(text.lower()) #['hello', 'world', '.', 'this', 'is', 'a', 'test', '.']

        # Removing stop words
        stop_words = set(stopwords.words("english")) #remove these words {'the', 'is', 'a', 'in', 'it', 'to', 'and', 'of', 'for', 'on', 'with', 'as'}
        filtered_words = [word for word in words if word.casefold() not in stop_words] # output => ['hello', 'world', '.', 'test', '.']

        # Calculate word frequencies(how many times a word used in the text) ['hello': 1, 'world': 1, '.': 2, 'test': 1]
        fdist = FreqDist(filtered_words) 

        # Assign scores to sentences based on word frequencies(calculate score from frequecies words. [expample => hellow word => Score: 1 + 1 = 2]) output => [2, 1, 0]
        sentence_scores = [sum(fdist[word] for word in word_tokenize(sentence.lower()) if word in fdist)
                        for sentence in sentences]

        # This attaches each sentence’s original index to its score (input => [2, 1, 0]  output => [(0, 2), (1, 1), (2, 0)])
        sentence_scores = list(enumerate(sentence_scores))

        # Sorts the sentences by their score in descending order (higher scores come first)  input => [(0, 2), (1, 1), (2, 0)]    output => [(0, 2), (1, 1), (2, 0)]
        sorted_sentences = sorted(sentence_scores, key=lambda x: x[1], reverse=True)

        # Randomly select the top `num_sentences` sentences for the summary  input => [(0, 2), (1, 1), (2, 0)]    outpu => [(1, 1), (0, 2)]
        random_sentences = random.sample(sorted_sentences, 3)
 
        # Sort the randomly selected sentences based on their original order in the text     input => [(1, 1), (0, 2)]         output => [(0, 2), (1, 1)]
        summary_sentences = sorted(random_sentences, key=lambda x: x[0])

        # Create the summary(Joins the selected sentences into a final summary string) input => [(0, 2), (1, 1)]        outpu => 'Hello world. This is a test.'
        summary = ' '.join([sentences[i] for i, _ in summary_sentences])
        print(summary)
        return summary


def savePeopleToFile(people):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "peopleData.txt")
    with open(file_path, "w") as file:
        json.dump({"people": people}, file, indent=4)

def loadPeopleFromFile():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "peopleData.txt")
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data.get("people", [])
    except FileNotFoundError:
        return []
    
def clearWindow(window):
    for widget in window.winfo_children():
        widget.destroy()



people = loadPeopleFromFile()

window = Tk()
window.title('SUMMARIZER')
window.geometry("500x300")
#window.resizable(False, False)

setting = Setting(window)
StartPage(window,people,setting)

window.mainloop()
