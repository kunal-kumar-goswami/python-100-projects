import art

print(art.logo)

#save data in dictionary
bidding = {}
bidding_continue = True

#function to find the highest bidder
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

#main bidding loop
while bidding_continue:
    your_name = input("Enter your name: ")
    your_bid = int(input("Enter your bid: $"))
    bidding[your_name] = your_bid

    #ask if there are more bidders
    more_bidders = input("Is there anybody else for bidding? Type 'yes' or 'no': ").lower()
    if more_bidders == "no":
        bidding_continue = False
        find_highest_bidder(bidding)