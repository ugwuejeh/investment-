
# Build an Investment application that inputs an investors name, amount to invest. There’s a 50% increase in your wallet balance .

# To withdraw, Input the amount you want to withdraw ; if the amount is greater than the wallet balance - Print (insufficient funds) 
# But if the amount you want to withdraw is less than the wallet balance - Print (withdrawal successful, your account has been debited with 
# …….. and 7% VAT  has been deducted)

def createinvestment(): 
 
  bonus = 0.5    # "50%  invextment bonus"
#    Inside the function, we prompt the user to enter their name and amount to invest. 
  investor_name = input("enter your name, ")
  amount_invested = int(input("enter amount to invest, "))
  investment_bonus = amount_invested * bonus
  wallet_balance = amount_invested + investment_bonus
  print(investor_name, "your wallet balance is", "#",  wallet_balance)

# We prompt the user to enter the amount they want to withdraw 
  withdrawer_amount = int(input("enter amount to withdraw, "))
  
  tax = 0.07      #   7% vat to be deducted from each withdrawal
  withdrawer_tax = withdrawer_amount * tax
  total_withdrawer = withdrawer_amount 
  New_wallet_balance = wallet_balance - total_withdrawer - withdrawer_tax

  if wallet_balance > total_withdrawer:

     print("withdrawal successful, your account has been debited with", total_withdrawer,  
     "and 7% VAT  has been deducted", "your New_wallet balance is", "#", New_wallet_balance)
  else:
     print("insufficient funds.")
    
createinvestment()
