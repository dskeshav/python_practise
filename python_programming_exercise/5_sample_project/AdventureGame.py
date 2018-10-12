"""
    _________            ______________________  
   |         |__________|Kitchen  |Dinning Room|
   | Family     Hallway                        |
   | Room     __________ ____   __|____    ____|                     
   |_________|          |         |  Living    |
                        Enterence      Room    |
                        |_________|____________|

 """
import random

def msg(room):
    if room['msg']=='': # There is no custom message
        return "You have entered the "+room['name']+ "."
    else:
        return room['msg']

def get_choice(room,dire):
    if dire=="N":
        choice=0
    elif dire=="E":
        choice=1
    elif dire=="S":
        choice=2
    elif dire=="W":
        choice=3
    else:
        return -1
    
    if room['directions'][choice]==0:
        return 4
    else:
        return choice


def main():
    dirs=(0,0,0,0)

    entrance ={'name':'Enterance way','directions':dirs,'msg':''}
    livingroom={'name':'Livingroom','directions':dirs,'msg':''}
    hallway={'name':'Hallway','directions':dirs,'msg':''}
    kitchen={'name':'Kitchen','directions':dirs,'msg':''}
    dinningroom={'name':'Dinningroom','directions':dirs,'msg':''}
    family_room={'name':'Familyroom','directions':dirs,'msg':''}
    
    #directions are tuples: Rooms to the (N,E,S,W)
    entrance['directions']=(kitchen,livingroom,0,0)
    livingroom['directions']=(dinningroom,0,0,entrance)
    hallway['directions']=(0,kitchen,0,family_room)
    kitchen['directions']=(0,dinningroom,entrance,hallway)
    dinningroom['directions']=(0,0,livingroom,kitchen)
    family_room['directions']=(0,hallway,0,0)

   
    
    #rooms where Johnns basket might be
    rooms=[livingroom,hallway,kitchen,dinningroom,family_room]
    rooms_with_eggs=random.choice(rooms)
    eggs_delivered=False
    room=entrance

    print("Welcome Bunnay! Can you find Johnn's basket?")

    while True:
        if eggs_delivered and room['name']== "Entrance Way":
            print("You have delivered the eggs and returned to the entrance. "+
                "You can now leave.Congrats")
            break
        elif not eggs_delivered and room['name']==rooms_with_eggs['name']:
            eggs_delivered=True
            print(msg(room)+ "There\'s the basket and Johnny is sleeping"+
             "right next to it! You have delivered the eggs. "+
             "now get out quick!")
            room['msg']=('You are back in the '+room['name']+
                           "! You already delivered the eggs. "+
                           "Get out of here before Johnny wakes up!")
        else:
            print(msg(room))
            room['msg'] = "You are back in the "+ room['name']

        stuck=True
        
        while stuck:
            dire=input("Which direction do you want to go: N,E,S or W? ")
            choice= get_choice(room,dire)
            if choice==-1:
                print("Please enter N,E,S or W? ")
            elif choice==4:
                print("You cannot go in that direction.")
            else:
                room=room['directions'][choice]
                stuck=False

if __name__=='__main__':
    main()
