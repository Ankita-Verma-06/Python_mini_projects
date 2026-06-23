target=60
atempt=1
for num in range(1,101):
  num=int(input("enter a number between 1 to 100: "))
  if(num<=100 and num>=0):
    if num==target:
     print("you won")
     print("no. of attempts: ",atempt)
     break
    elif(num>60 and num<=70):
      print("a bit high (go lower)")
      atempt+1
    elif(num>70 and num<=80):
      print("high (go lower)")
      atempt+1
    elif(num>80 and num<=90):
      print("very high (go lower)")
      atempt+1
    elif(num>90 and num<=100):
      print("very very high (go lower)")
      atempt+1
    elif(num>=0 and num<=10):
      print("too much low (go higher)")
      atempt+1
    elif(num>=10 and num<=20):
      print("very very low (go higher)")
      atempt+1
    elif(num>20 and num<=30):
      print(" very low (go higher)")
      atempt+1
    elif(num>30 and num<=40):
      print("low (go higher)")
      atempt+1
    elif(num>40 and num<=50):
      print("a bit low (go higher)")
      atempt+1
    elif(num>50 and num<60):
      print("little bit low (go higher)")
      atempt+1
    else:
      print("invalid input")
      atempt+1
  else:
    print("please enter number between 1 to 100")
    atempt+1
