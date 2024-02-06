import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
players = True
bidders = {}
print(logo)
print("Welcome to the secret auction!")

def bidding(player, money):
    bidders[player] = money

while players is True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidding(player=name, money=bid)
    question = input("Are there any more bidders? Type 'yes' or 'no'.\n").lower()
    if question == "yes":
        os.system("clear")
    elif question == "no":
        highest_bidder = max(bidders, key=bidders.get)  # type: ignore
        highest_bid = max(bidders.values())
        os.system("clear")
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
        players = False
