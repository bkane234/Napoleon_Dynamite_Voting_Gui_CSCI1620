#This Logic file handles all of the internal logic for the inputs and buttons, as well as a csv reader to help count votes
from GUI import *  
import re 
import csv



def submit(gui_instance) -> None:
    '''
    Handles logic for the submit button
    
    
    '''
    id_regex: str = r'\b\d{' + str(3) + r'}\b' #Regex for checking syntax of the ID entry field, from stackoverflow.com
    dob_regex: str = r'\b(0[1-9]|1[0,1,2])\/(0[1-9]|[12][0-9]|3[01])\/(19|20)\d{2}\b' #Regex for checking the birthday syntax of the DOB entry field, also from stackoverflow.com
    

    
    try:
       vote: str = gui_instance.option.get() #The following get statements grab the input from the GUI file and strips it down
       name: str = gui_instance.entry_voting_name.get().strip()
       id: str = gui_instance.entry_voting_ID.get().strip()
       dob: str = gui_instance.entry_voting_DOB.get()
       student_info: dict = {"111": "Ben Kane"} #Dictionary to keep track of all students (For the purposes of this project it will remain small)
       if name not in student_info.values(): #The following are various checks to make sure the user is entering the correct data
            raise ValueError("Student name not found")
            # Value errors are handled below in the except blocks which print a warning message to the user. 
       if id not in student_info.keys():
            raise ValueError("Student ID not found")
       
       if not name:
            raise ValueError("Name cannot be empty.")
       if not id :
              raise ValueError("ID cannot be empty")
       if not re.fullmatch(id_regex, id):
           raise TypeError("Please provide a valid ID")
       
       if not dob:
            raise ValueError("Date of Birth cannot be empty.")
       if not re.fullmatch(dob_regex, dob):
              raise TypeError("Please enter the date in (MM/DD/YYYY) format")
       if vote == "None":
            
            raise ValueError("Please choose a candidate")
       gui_instance.label_voting_pane.config(text="Submission successful!", fg="green") #Checks input to confirm it is in correct format
       with open('Logging_data.csv', 'a', newline='') as file: #This block opens the data file so the votes can be logged as such.
                writer = csv.writer(file)
                writer.writerow([name, id, dob, vote])
       #Writes the data to a csv file 
       gui_instance.entry_voting_name.delete(0, END)#The following resets the pane for another user
       gui_instance.entry_voting_ID.delete(0, END)
       gui_instance.entry_voting_DOB.delete(0, END)
       gui_instance.option.set(None)
       gui_instance.entry_voting_name.focus_set()
       

    except ValueError as ve: #The following handle any errors experienced by the above Try/except block.
       gui_instance.label_voting_pane.config(text=str(ve), fg="red")
    except TypeError as te :
       gui_instance.label_voting_pane.config(text=str(te), fg="red")      
       #Handles exceptions 
def view_results(results_instance) -> int:
       """
       Creates the Results Gui to view the current results of the voting by user input
       
       
       """
      
       
       from GUI import Results #Initializes the Results Window 
       tally_p: dict = {} #Creates two dictionaries to store votes for each candidate
       tally_s: dict = {}
       with open("Logging_data.csv", mode="r") as file: #This time, the file is opened in read mode and a reader object is created
            reader = csv.DictReader(file)
            for row in reader:
              
              vote = row["Vote"].strip()  
              if vote == "Pedro_Sanchez": #Here the votes are read and tallied use addition and the get method.
                    tally_p[vote] = tally_p.get(vote, 0) + 1
              elif vote == "Summer_Wheatly":
                    tally_s[vote] = tally_s.get(vote, 0) + 1

              

       total_pedro = sum(tally_p.values()) # The sum method adds all the votes from the dictionaries to create the final totals we see in the results pane
       total_summer = sum(tally_s.values())
       window1 = Tk() # The following creates the Results window pending user input 
       window1.title("Results Window")
       window1.geometry("250x250")
       window1.resizable(False, False)
       Results(window1, total_pedro, total_summer)
       window1.mainloop()


       
                 





