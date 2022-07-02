from turtle import clear

#creating an empty dictionary to store the bidders and their respective bids
bidders = {}
#this will let us know when the auction is over
bidding_finished = False

#this is a function that wil find the highest bidder in the auction room
def find_highest_bidder(bids):
  winning_bid = 0
  winner = ""
  for bidder in bids:
    current_bid = bids[bidder]
    if current_bid > winning_bid:
      winning_bid = current_bid
      winner = bidder
  print(f"The winner is {winner} with a bid of ${winning_bid} !")

#as long as the auction is not over, we will continue to accept bids from bidders
while not bidding_finished:
    username = input("What is your name?: ")
    userbid = int(input("What is your bid?: $"))
    bidders[username] = userbid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    #this means there are no other people willing to bid and so this marks the end of the auction
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bidders)
    #this means there are more willing bidders, meaning the show must go on!!
    elif should_continue == "yes":
        clear() 



  
