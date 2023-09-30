#Taking inputs

nominee1 = input("Enter the name of the 1st nominee")
nominee2 = input("Enter the name of the 2nd nominee")

# Vote count for all the nominee needs to be equal to 0

nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

while True:
    if voter_id == []: #to check if voter list is completed
        print("Voting session is over")
        if nm1_votes>nm2_votes:
            percent = (nm1_votes/no_of_voter)*100#To calculate the percentage
            print(nominee1, "has won", percent,"% of votes")
            break # to get rid of infinite loop
        elif nm2_votes > nm1_votes:
            percent = (nm2_votes/no_of_voter) * 100  # To calculate the percentage
            print(nominee2, "has won", percent, "% of votes")
            break  # to get rid of infinite loop
        else:
            print("Both have equal number of vote")
            break


    voter = int(input("Enter your voter id:"))
    if voter in voter_id:
        print(" You are a voter")
        voter_id.remove(voter) #We will remove it so that the same voter can't vote
        print("To give vote to", nominee1,"Press 1")
        print("To give vote to", nominee2, "Press 2")

        vote =int(input("Enter your precious vote:"))
        if vote ==1:
            nm1_votes +=1
            print(nominee1, "Thank you for your vote")
        elif vote ==2:
            nm2_votes +=1
            print(nominee2, "Thank you for your vote")
        elif vote >2:
            print("Check your pressed key and try again")
        else:
            print("You are not a voter Or you have already voted")


