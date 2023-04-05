def createinvestment(): 
 
  bonus = 0.5
  investor_name = input("enter your name, ")
  amount_invested = int(input("enter amount to invest, "))
  investment_bonus = amount_invested * bonus
  wallet_balance = amount_invested + investment_bonus
  print(investor_name, "your wallet balance is", "#",  wallet_balance)
  
  withdrawer_amount = int(input("enter amount to withdraw, "))
  tax = 0.07
  withdrawer_tax = withdrawer_amount * tax
  total_withdrawer = withdrawer_amount - withdrawer_tax
  New_wallet_balance = wallet_balance - total_withdrawer

  if wallet_balance > total_withdrawer:

     print("your withdrawer is", "#", total_withdrawer, "your New_wallet balance is", "#", New_wallet_balance)
  else:
     print("you have insufficient balance.")
    
createinvestment()

