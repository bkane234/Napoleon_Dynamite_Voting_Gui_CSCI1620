from tkinter import * 





class GUI:
    def __init__(self, window) -> None:
        """
        Initializes each of the variables and places them accordingly.
        
        
        """
        
        self.window = window
        self.option = StringVar(None)
        self.label_voting_name = Label(self.window, text="Enter your name:")
        self.label_voting_ID = Label(self.window, text="Enter your unique ID:") 
        self.label_voting_DOB = Label(self.window, text="Enter your Date of Birth (MM/DD/YY):")
        self.label_voting_pane = Label(self.window, text="Choose one candidate:")
        

        pedro_image = PhotoImage(file=r"C:\Users\bkane\OneDrive\Documents\GitHub\Voting_Lab_Napoleon_Dynamite\Pedro.gif")
        pedro_image = pedro_image.subsample(4,4)
        summer_image = PhotoImage(file=r"C:\Users\bkane\OneDrive\Documents\GitHub\Voting_Lab_Napoleon_Dynamite\Summer.gif")
        summer_image = summer_image.subsample(4,4)
        #Creates the images for use with radio buttons

        self.entry_voting_name = Entry(self.window, width=20)
        self.entry_voting_ID = Entry(self.window, width=20)
        self.entry_voting_DOB = Entry(self.window, width=20)
        self.option.set(None)
        self.radio_pedro = Radiobutton(self.window, text= "Pedro Sanchez",variable=self.option, value="Pedro_Sanchez", image=pedro_image, compound="left")
        self.radio_pedro.image = pedro_image 
        self.radio_summer = Radiobutton(self.window, text= "Summer Wheatly",variable=self.option, value="Summer_Wheatly", image=summer_image, compound ="left")
        self.radio_summer.image = summer_image
        self.button_submit = Button(self.window, text="Submit", command=self.submit)
        self.button_view_results = Button(self.window, text="View Results", command=self.view_results)
        #Creates various input boxes

        self.label_voting_name.pack(side="top", padx = 10, pady=15, anchor="w")
        self.entry_voting_name.place(x=150, y=17)
        self.label_voting_ID.pack(side="top", padx = 10, pady=15, anchor="w")
        self.entry_voting_ID.place(x=150, y=67)
        self.label_voting_DOB.pack(side="top", padx = 10, pady=15, anchor="w")
        self.entry_voting_DOB.place(x=220, y=118)
        self.label_voting_pane.pack(side="top", anchor='center')
        self.radio_pedro.pack(side="top", pady=10, anchor="w")
        self.radio_summer.pack(side="top", pady=10, anchor="w")
        self.button_view_results.pack(side="bottom", padx =10, anchor="center")
        self.button_submit.pack(side="bottom", padx =10, anchor="center")
        #Places each widget
    def submit(self):
        from Logic import submit  
        submit(self)
    def view_results(self):
        from Logic import view_results  
        view_results(self)  
    
class Results(GUI):
    def __init__(self, window1, total_pedro, total_summer) -> None:
    
        self.window = window1
        
        self.res = Label(self.window, text="Current Results")
        self.divider = Label(self.window, text="-"*40)
        self.total_pedro = Label(self.window, text=f"Votes for Pedro: {total_pedro}")
        self.total_summer = Label(self.window, text=f"Votes for Summer: {total_summer}")

        self.res.pack(side="top", anchor="n")
        self.divider.pack(side="top", anchor="n")
        self.total_pedro.pack(side="top", padx =5, pady =1, anchor="e")
        self.total_summer.pack(side="top", padx =5, pady = 1, anchor="nw")
    
        
          
    