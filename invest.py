
def createinvestment(): 
 
  bonus = 0.5("50% of your investment")
  investor_name = input("enter your name, ")
  amount_invested = int(input("enter amount to invest, "))
  investment_bonus = amount_invested * bonus
  wallet_balance = amount_invested + investment_bonus
  print(investor_name, "your wallet balance is", "#",  wallet_balance)
  
  withdrawer_amount = int(input("enter amount to withdraw, "))
  tax = 0.07("7% VAT on each withdraw")
  withdrawer_tax = withdrawer_amount * tax
  total_withdrawer = withdrawer_amount 
  New_wallet_balance = wallet_balance - total_withdrawer - withdrawer_tax

  if wallet_balance > total_withdrawer:

     print("your withdrawer is", "#", total_withdrawer, "your New_wallet balance is", "#", New_wallet_balance)
  else:
     print("you have insufficient balance.")
    
createinvestment()
