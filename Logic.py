from GUI import *  
import re 
import csv



def submit(gui_instance) -> None:
    '''
    Handles logic for the submit button
    
    
    '''
    id_regex = r'\b\d{' + str(3) + r'}\b' 
    dob_regex = r'\b(0[1-9]|1[0,1,2])\/(0[1-9]|[12][0-9]|3[01])\/(19|20)\d{2}\b'
    

    
    try:
       vote = gui_instance.option.get()
       name = gui_instance.entry_voting_name.get().strip()
       id = gui_instance.entry_voting_ID.get().strip()
       dob = gui_instance.entry_voting_DOB.get()
       if not name:
            raise ValueError("Name cannot be empty.")
       if not id :
              raise ValueError("ID cannot be empty")
       if not re.fullmatch(id_regex, id):
           raise TypeError("Please provide a valid ID")
       
       if not dob:
            raise ValueError("Date of Birth cannot be empty.")
       if not re.fullmatch(dob_regex, dob):
              raise TypeError("Please enter the date in (MM/DD/YY) format")
       gui_instance.label_voting_pane.config(text="Submission successful!", fg="green")
       #Above checks input to confirm it is in correct format
       with open('Logging_data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, id, dob, vote])
       #Writes the data to a csv file 
       gui_instance.entry_voting_name.delete(0, END)
       gui_instance.entry_voting_ID.delete(0, END)
       gui_instance.entry_voting_DOB.delete(0, END)
       gui_instance.option.set(None)
       gui_instance.entry_voting_name.focus_set()
       #Resets the pane for another user

    except ValueError as ve: 
       gui_instance.label_voting_pane.config(text=str(ve), fg="red")
    except TypeError as te :
       gui_instance.label_voting_pane.config(text=str(te), fg="red")      
       #Handles exceptions 
def view_results(results_instance) -> int:
       """
       Creates the Results Gui to view the current results of the voting
       
       
       """
      
       #Initializes the Results Window 
       from GUI import Results
       tally_p = {}
       tally_s = {}
       with open("Logging_data.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
              
              vote = row["Vote"].strip()  
              if vote == "Pedro_Sanchez":
                    tally_p[vote] = tally_p.get(vote, 0) + 1
              elif vote == "Summer_Wheatly":
                    tally_s[vote] = tally_s.get(vote, 0) + 1

              

       total_pedro = sum(tally_p.values())
       total_summer = sum(tally_s.values())
       window1 = Tk()
       window1.title("Results Window")
       window1.geometry("250x250")
       window1.resizable(False, False)
       Results(window1, total_pedro, total_summer)
       window1.mainloop()


       
                 





