items=["shoes", "couch", "blender", "water bottle", "tv"]
categories={"shoes", "couch", "blender", "water bottle", "tv"}
name_price={"shoes": 400, "couch": 6000, "blender": 2000, "water_bottle": 800, "tv": 40000}
total_bill=0;
while True:
  print("items present in cart: ")
  for item in items:
    print(item)
  p=input(("enter 'a' for Adding new item, 'r' for removing item or 'e' to exit: "))
  if p=='a':
    name=input("enter the name of item: ")
    price=int(input("enter the price of item: "))
    items.append(name)
    categories.add(name)
    name_price[name]=price
    print("item added")
  elif p=='r':
    name=input("enter the name of item to be removed: ")
    if name in items:
      items.remove(name)
      del name_price[name]
      print("item removed")
      if name in categories:
        categories.remove(name)
    else:
      print("item not found")
  elif p=='e':
      print("exiting")
      break
  else:
    print("invalid input(please enter 'a' to add or 'r' to remove or 'e' to exit)")
  for price in name_price.values():
    total_bill=total_bill+price
  print("total price of all items:",total_bill)
