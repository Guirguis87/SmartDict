import json
from difflib import SequenceMatcher
from difflib import get_close_matches 

data = json.load(open(r"D:\Courses - Trainings\Programming\Projects\Dict\data.json","r"))
while True: 
    print(" Welcome to RMC Soft for Engineering Solutions , Your dream became a code " + "\n")
    user_input = input (" Please Enter the word : ")

    def definition_fun(w):

        if user_input.lower() in data :
            return (data[user_input.lower()])
        
        elif len(get_close_matches("w",data.keys())) > 0:
            matching_func= (get_close_matches(w, data.keys()))[0:3]
            user_input2= input (f"Your Entry is not accurate , Did you mean {matching_func} ?  if Yes Please Enter Y , if No please Enter N :   ")

            if user_input2.upper() == "Y":
                user_input3= input("which word to define: ")
                if user_input3.lower() in matching_func:
                    return (data[user_input3.lower()])
                else:
                    return (" Your Entry is not correct , please check again !!")

                
            elif user_input2.upper() == "N":
                return ("Your word doesn't exist")
            else:
                return ( " Your Entry is not correct , please check it again")

        else:
            return ("Your word doesn't exist , please double check !")
    output = definition_fun(user_input.lower())

    if type(output) == list: 
        for definitions in output:
            print (definitions)
    else:
        print (output)

    user_decision = "Y" or "N"
    while user_decision != "Y" or "N":
        user_decision = input ("Would you like to search for another word ?  Please Press (Y) if yes or (N) if No  :  ")
        user_decision.upper()

        if user_decision.upper() == "Y":
            break

        elif  user_decision.upper() == "N":
            print ( "Thanks for your time ! we hope you enjoyed")
            break
        else:
            print("Your Entry is not clear ! Please double check it ")
    if user_decision.upper() == "Y":
        continue
    else:
        break

  

