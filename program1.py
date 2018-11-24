print "   ***************************ONE DAY MATCH**********************"
print "*********************************************************************"
cricket_score_1={"overs":10,"balls":60,"runs":0,"wickets":10}
cricket_score_2={"overs":10,"balls":60,"runs":0,"wickets":10}
for j in range(2):
    print "Choose the batting team   =    Team A           "
    print "                               Team B           "
    choice_1=raw_input("Enter the choice :")
    if j==0:
        print "1st innings"
    else:
        print "2nd innings"
        if (choice_1=='B' or choice_1=='b'):
            print "Team B needs ",cricket_score_1["runs"]+1," to win"
        else:
            print "Team A needs ",cricket_score_2["runs"]+1," to win"
    if (choice_1=='A' or choice_1=='a'):
        print "******currently team",choice_1,"is batting******"
        print cricket_score_1
        for i in range(0,60,1):
            f=input("Enter the number of runs taken    :")
            if (f==0):
                print "wicket lost or not"
                print "If yes Enter y"
                print "if no  Enter n"
                rep_1=raw_input("Enter your choice  :")
                if (rep_1=='y'):
                    cricket_score_1["wickets"]-=1
                    cricket_score_1["balls"]-=1
                    print "out!!!!"
                    if (cricket_score_1["wickets"]==0):
                        print  "Team",choice_1,"s batting is over!!!!!"
                        break
                else:
                    cricket_score_1["balls"]-=1
            elif(f>6):
                    print "Invalid"
            else:
                cricket_score_1["runs"]+=f
                cricket_score_1["balls"]-=1
                if (cricket_score_1["balls"]%6==0):
                    cricket_score_1["overs"]-=1
            
            print "No of overs left :",cricket_score_1["overs"]
            print "No of balls left :",cricket_score_1["balls"]
            print "No of runs taken :",cricket_score_1["runs"]
            print "No of wickets left :",cricket_score_1["wickets"]
        
    else:
        if (choice_1== 'B' or choice_1=='b'):
            print "******currently team",choice_1,"is batting******"
            print cricket_score_2
            for i in range(0,60,1):
                f=input("Enter the number of runs taken    :")
                if (f==0):
                    print "wicket lost or not"
                    print "If yes Enter y"
                    print "if no  Enter n"
                    rep_2=raw_input("Enter your choice  :")
                    if (rep_2=='y'):
                        cricket_score_2["wickets"]-=1
                        cricket_score_2["balls"]-=1
                        print "out!!!!"
                        if (cricket_score_2["wickets"]==10):
                            print  "Team",choice_1,"s batting is over!!!!!"
                    else:
                        cricket_score_2["balls"]-=1
                elif(f>6):
                    print "Invalid"
                else:
                    cricket_score_2["runs"]+=f
                    cricket_score_2["balls"]-=1
                    if (cricket_score_2["balls"]%6==0):
                        cricket_score_2["overs"]-=1
            
                print "No of overs left :",cricket_score_2["overs"]
                print "No of balls left :",cricket_score_2["balls"]
                print "No of runs taken :",cricket_score_2["runs"]
                print "No of wickets left :",cricket_score_2["wickets"]
    if j==1:
        if (choice_1=='A' or choice_1=='a'):
            if (cricket_score_1["runs"]) > (cricket_score_2["runs"]):
                print "Team A wins by ",cricket_score_1["runs"]-cricket_score_2["runs"]," runs"
            else:
                print "Team A loses by ",cricket_score_2["runs"]-cricket_score_1["runs"],"runs"

        else:
            if (cricket_score_1["runs"]) > (cricket_score_2["runs"]):
                print "Team B loses by ",cricket_score_1["runs"]-cricket_score_2["runs"],"runs"
            else:
                print "Team B wins by ",cricket_score_2["runs"]-cricket_score_1["runs"],"runs"

      
    

