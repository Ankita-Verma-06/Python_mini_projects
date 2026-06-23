current_amount=50000
pin=4729
pin_chances=3
pr_chances=1
while(pin_chances<4 and pin_chances>0):
  user_pin=int(input("enter your pin: "))
  if(user_pin==pin):
    print("pin verified")
    while pr_chances<5:
      process=input("do you want to withdraw or dpositor check balance (w/d/c): ").lower()
      if process=="d":
        deposit=int(input("enter deposit amount: "))
        currnt_amount=current_amount+deposit
        print("your current balance is: ", current_amount)
        pr_chances+=1
      elif process=="w":
        withdraw=int(input("enter withdraw amount: "))
        current_amount=current_amount-withdraw
        print("your current balance is: ", current_amount)
        pr_chances+=1
      elif process=="c":
        print("your current balance is: ", current_amount)
        pr_chances+=1
      else:
        print("invalid input(please select w or d or c)")
    print("you exceed the limit")
    break
  elif(user_pin!=pin):
      pin_chances=pin_chances-1
      print("invalid pin")
      print("try again! you have", pin_chances,"chances left")
print("try after 24 hours")
