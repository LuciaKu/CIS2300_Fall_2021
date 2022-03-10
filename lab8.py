def checkPlayer(team):
    cont="Yes"
    while cont=="Yes" or cont=="yes":
        player=input("Enter a player you want to check\n")
        if player in team:
            print("This player is on the team")
        else:
            print("This player is not on the team")
        cont=input("Would you like to check another player?\nEnter yes or not\n")
        
def main():
    myTeam=["Lebron","Kobe","Davis","Jordan","Curry","Drumond"]
    checkPlayer(myTeam)
    
main()