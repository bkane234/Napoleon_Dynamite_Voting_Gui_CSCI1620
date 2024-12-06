#Code to Improve Lab 1-Voting App-Main File

from GUI import * 

window = Tk()
window.title("President Voting Window")
window.geometry("350x520")
window.resizable(False, False)
GUI(window)
window.mainloop()












'''def vote_menu():
    while True:
        dash = "-" *30
        print(dash)
        print("VOTE MENU")
        print(dash)
        print("v: Vote")
        print("x: Exit")
        option = input("Option: ").strip().lower()
        
        if option in ['v', 'x']:
            return option
        else:
            print("Invalid (v/x):", option)

def candidate_menu():
    while True:
        dash = "-" *30
        print(dash)
        print("CANDIDATE MENU")
        print(dash)
        print("1: Ben")
        print("2: Angie")
        print
        candidate = input("Candidate: ").strip()
        
        if candidate.isdigit() and candidate in ['1', '2']:
            return int(candidate)
        else:
            print("Invalid (1/2):", candidate)

def main():
    dash = "-" * 30
    votes = {'Ben': 0, 'Angie': 0}
    total_votes = 0
    
    
    while True:
        option = vote_menu()
        
        if option == 'x':
            break
        
        candidate = candidate_menu()
        
        if candidate == 1:
            votes['Ben'] += 1
            print("Voted Ben")
        elif candidate == 2:
            votes['Angie'] += 1
            print("Voted Angie")
        
        total_votes += 1
    print(dash)
    print(f"Ben — {votes['Ben']}, Angie — {votes['Angie']}, Total — {total_votes}")
    print(dash)
if __name__ == "__main__":
    main()'''