from .utility import clearScreen
from .utility import WelcomeNote
from .utility import Exit

from pymongo import DESCENDING


CLIENT = None
db = None
collection = None

def getMenuList():
    return ["Add Subscriber", "View Subscriber", "Update Subscriber", "Delete Subscriber", "Restart Subscriber", "Exit"]


def Switch(choice):
    action = {
        1: AddSubscriber,
        2: ViewSubscriber,
        3: UpdateSubscriber,
        4: DeleteSubscriber,
        5: RestartSubscriber,
        6: TurnOnSubscriber,
        7: TurnOffSubscriber,
        8: Exit
    }
    if choice in action.keys():
        return action[choice]
    else:
        clearScreen()
        input("Enter the valid choice. Press enter to continue")


def AddSubscriber():
    global collection
    # subscriber = {
	# 	"subscriber_id": 1,
	# 	"type":"default",
	# 	"topic":"test/topic",
	# 	"publisher": False,
	# 	"subscriber": True,
	# 	"default": 35,
	# 	"status": True
	# }
    print(collection)
    

    last_record = collection.find_one({}, sort=[('subscriber_id',DESCENDING)])
    nextId = last_record["subscriber_id"] + 1

    choice = 0
    subscriber = {
        "subscriber_id" : nextId
    }

    while choice != 3:
        WelcomeNote()
        print("1. Add One\n2. Add Multiple\n3. Go Back")
        
        try:
            choice = int(input("Enter your choice:"))
            clearScreen()
            if choice == 3:
                return
        except:
            clearScreen()
            input("Enter the valid choice. Press enter to continue")
            continue

        if choice ==1:    
            subscriber = acceptSubscriberData(subscriber)    
            if subscriber is not None:
                collection.insert_one(subscriber)
            else:
                clearScreen()
                input("Unexpected Error Occured. Press enter to continue...")
                return
    
    clearScreen()
    input("Subscriber Has Been Successfully Added!\nPress Enter To Continue")
    return

def acceptSubscriberData(subscriber):
    type = ["Default", "Runtime"]
    channels = ["test/", "prod/"]

    try:  
        # Get Subscriber Type
        print("Choose Type:\n1. Default\n2. Runtime\n")
        value = input("Enter Your Choice : ")
        
        if value in [1,2]:
            subscriber["type"] = type[value]
        else:
            subscriber["type"] = "default"


        # Get Subscriber topic
        print("\nChoose To Subscribe At :\n1. test\n2. prod")
        channel = input("Enter your choice : ")
        value = input("Enter your topic name : ")

        if channel == "2":
            subscriber["topic"] = channels[1] + value
        else:
            subscriber["topic"] = "test/" + value

        subscriber["publisher"] = False
        subscriber["subscriber"] = True

        # Get default sensor value
        # value = float(input("Enter default sensor value : "))
        # sensor["default"] = value
        
        # Set subscriber
        subscriber["status"] = True
            
        return subscriber
    
    except Exception as e:
        clearScreen()
        key = 0
        value = 0
        input(f"Sensors can't be of same details -> {key}:{value}\nPress enter tocontinue...")
        return None

def ViewSubscriber():
    pass

def UpdateSubscriber():
    pass

def RestartSubscriber():
    pass

def DeleteSubscriber():
    pass

def TurnOnSubscriber():
    pass

def TurnOffSubscriber():
    pass

def Menu(client):
    clearScreen()
    choice = ""
   
    # Database()
    global CLIENT
    global db
    global collection
    CLIENT = client
    db = client["iot_data"]
    collection = db["subscribers"]
    
    
    if client.server_info():
        while choice != len(getMenuList()):
            WelcomeNote()

            for counter, option in enumerate    (getMenuList()):
                print(f"{counter+1}.{option}")

            try:
                choice = int(input("Enter your  choice:"))
            except:
                clearScreen()
                input("Enter the valid choice.  Press enter  to continue")
                continue

            execute = Switch(choice)

            if execute is not None:
                execute()

            clearScreen()
    else:
        clearScreen()
        input("Server Disconnected. Please Press Enter To Continue..")
        return