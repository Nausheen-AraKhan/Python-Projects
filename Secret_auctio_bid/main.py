import art
print(art.logo)
yes_no="YES"
auction_bit={}
while yes_no == "YES":
    name=input("What is your name? ")
    bid=int(input("What is your bid? $"))
    auction_bit[name]=bid
    yes_no=input("Are there any more bidders? Type 'YES' or 'NO': ").upper()
    if yes_no == "NO":
        break
    else:
        print("\n"*30)

winner=max(auction_bit, key=auction_bit.get)
print(f"The winner is {winner} with a bid of ${auction_bit[winner]}")
