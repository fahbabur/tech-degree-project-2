import constants
import copy

theteams = copy.deepcopy(constants.TEAMS)
theplayers = copy.deepcopy(constants.PLAYERS)
expplayers = []
nonexpplayers = []
database = []
allthreeteams = []

def clean_data():
    # method to clean dataset to remove yes and no to booleans true or false and turn height to integers from string type
    for player in theplayers:
        if player['experience'] == 'YES':
            player['experience'] = True
            heightchange = player['height'].split()
            player['height'] = int(heightchange[0])
                                    
        if player['experience'] == 'NO':
            player['experience'] = False                          
            heightchange = player['height'].split()
            player['height'] = int(heightchange[0])
    

  
def split_players():
    # split players into two groups, experienced and inexperienced
    for each_player in theplayers:
        if each_player["experience"] == True:
            expplayers.append(each_player)
            
        if each_player["experience"] == False:
            nonexpplayers.append(each_player)

            
def divide_players():
    # divided players equally into a new collection (list)
    while expplayers and nonexpplayers:
        database.append(expplayers.pop(0))
        database.append(nonexpplayers.pop(0))
    
# divided the players in three groups with equal ability

def team_sort():
    for team in theteams:
	      allthreeteams.append(team.split())
    for each in allthreeteams:
        each.append(database[:6])
        del database[:6]


# functions to show basketball stats

def team_name(option_two):
    # display team name
    print("===========================")
    print("TEAMS NAME :", allthreeteams[option_two - 1][0].upper(), "\n")
    
    
def total_players(option_two):
    # display all the number of players in the team
    print("TOTAL PLAYERS : {}\n".format(len(allthreeteams[option_two - 1][1])))

    
def team_members(optiontwo):
    # print team members names in a line 
    print("team member :".upper(), end=" ")
    for each_member in allthreeteams[option_two - 1][1]:
        print(each_member['name'], end =', ')
    print("\n")
    
    
def number_of_experienced_players(option_two):
    # print name and number of experienced players
    count_exp = 0
    print("experienced players :".upper(), end =" ")
    for each_member in allthreeteams[option_two - 1][1]:
        if each_member['experience'] == True:
            print(each_member['name'], end =', ')
            count_exp += 1
    print("\n")
    print("number of experienced players : {}".upper().format(count_exp))
    print("\n")
    
def number_of_inexperienced_players(option_two):
    # print name and number of inexperienced players
    count_inexp = 0
    print("inexperienced players :".upper(), end =" ")
    for each_member in allthreeteams[option_two - 1][1]:
        if each_member['experience'] == False:
            print(each_member['name'],end =', ')
            count_inexp += 1
    print("\n")
    print("number of inexperienced players : {}".upper().format(count_inexp))
    print("\n")

def average_height(option_two):
    #print the average height of the team members  
    average_height = 0
    for each_member in allthreeteams[option_two - 1][1]:
        average_height = average_height + each_member['height']
    print("Average height :".upper(), average_height / len(allthreeteams[option_two - 1][1]))
    print("\n")
    
def players_guardians(option_two):
    # print the names of the guardians of team players
    print("players guardians:".upper(), end =" ")
    for each_member in allthreeteams[option_two - 1][1]:
        print(each_member['name'],":", "({}),".format(each_member['guardians']), end=" ")
    print("\n")

def show_team_stat(option_two):
    # too many function so i put the functions inside a function
    team_name(option_two)
    total_players(option_two)
    team_members(option_two)
    number_of_experienced_players(option_two)
    number_of_inexperienced_players(option_two)                                
    players_guardians(option_two)

clean_data()

split_players()

divide_players()

team_sort()


print("++++++++++++++++++++++++++++++++++++++")
print("      basketball teams stats tool".upper())
print("++++++++++++++++++++++++++++++++++++++\n")
print("=================MENU=================\n")


while True:  
    try:
        print("     here are your option:\n".upper())
        print("     press 1: Show teams stats\n".upper())
        print("     press 0: to quit program\n".upper())
        option_one = int(input("Enter a option >   ".upper()))
                
    except ValueError:
      print("\nOops thats not a number, try again\n".upper())
    
    else:
        if option_one > 1 or option_one < 0:
            print("\n your option and 0 or 1 \n".upper())
            continue
            
        if option_one == 1:      
            while True:
                try:
                    print("\n     heres the list of teams".upper())
                    for position, each in enumerate(allthreeteams):
                        print("\n      PRESS", position + 1,":", each[0])
                    print("\n      press 0 to return to menu\n".upper())
                        
                    option_two = int(input("pick a team: >  ".upper()))
                    print()
                    
                except ValueError:
                    print("Oop thats not a number, try again".upper())
                    
                else:
                    if option_two > 3 or option_two < 0:
                        print("\n your options and 1 ,2 and 3\n".upper())
                        continue
                    
                    if option_two == 1:
                        show_team_stat(option_two)
                        
                    if option_two == 2:
                        show_team_stat(option_two)
                        
                    if option_two == 3:
                        show_team_stat(option_two)
                
                    if option_two == 0:
                        break
            
        if option_one == 0:
            break
        
        
print("\nthank you for using the program, GOODBYE\n".upper())


if __name__ == "__main__":
    cleaned_data = clean_data()
    split_players()
    divide_players()
    team_sort()
	