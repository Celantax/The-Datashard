import math
import tools
import operation
print("write down 'exit' if you want to terminate the program ")
data = []
ShardLimit = 10
while len(data) < ShardLimit:
        try:
            Ent = input("Use the therminal for either paramethers: ").upper().strip()

            if Ent == "EXIT":
                print("Proqram is done, The datashard contains: ", data)
                break
    
            Len_Ent = Ent.split()

            if len(Len_Ent) == 2:
                Width, Length = map(int,Len_Ent)
                while True:
                    if tools.check(Width,Length):
                        Eza = tools.Area(Width,Length)
                        data.append(Eza)
                        print(f"The area of the rectangular is: {Eza} ")
                        break
                    else:
                        print("Number must be positive. The program will forcefully convert the negative numbers to positive ones")
                        Length = abs(Length)
                        Width = abs(Width)
            else:
                print("Add only 2 digits")

        except ValueError:
            print("Enter Proper Parameters")
print("The Data Collection Process Has finished. Your datashard's memory is: ", data)


while len(data) < ShardLimit:
        a = input("Do you wish adding couple rectangular areas manually? text 'yes' or 'no'").upper()
    
        if a == "YES":
            try:
                neware = int(input("Enter the new values: "))
                data.append(neware)
            except:
                print("Only numbers. it is not that hard")
        elif a == "NO":
            print("termination protocol has been successfully completed")
            break
        else:
            print("I think we both speak in english. only YES or NO")    

print("Data extraction protocol has been successfully completed. Please enter these keys for further Operations. The keys are: 'Mean','Range','Mode'")
print("Please do not forget to text 'cancel' for the termination of the protocol")
while True:
    nEnt = input("Enter the key code: ").upper()
    if nEnt == 'CANCEL':
        print("THe termination protocol has been successfully completed.")
        break
    elif nEnt == "RANGE":
        if data:
            print("The Range of the Shard is: ", operation.calculate_range(data))
            
        continue
    elif nEnt == "MODE":
        if data:
            print("The Mode of the Shard is: ", operation.calculate_mode(data))
        else:
            print("There is not enough data in shard. add atleast 3.")
        continue
    elif nEnt == "MEAN":
        if data:
            print("The Mean of the Shard is: ", operation.calculate_mean(data))
        continue
    else:
        print("Warning! Enter only valid commands")
