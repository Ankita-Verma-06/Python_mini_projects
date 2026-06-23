cb={1:{"Ankita": 8816837262},
    2:{"Pinky": 7432904817},
    3:{"Ritu": 6029330293},
    4:{"Monu": 9923667530},
    5:{"Rahul": 8892305578},
    6:{"Pinky": 7432904817}}

while True:
  print("\nCurrent Contacts:")
  if not cb:
    print("No contacts available.")
  for key, value in cb.items():
    for name, number in value.items():
      print(key, name, ":", number)
  seen_numbers = {}
  duplicates_found = False
  for contact_id, contact_info in cb.items():
      for name, number in contact_info.items():
          if number in seen_numbers:
              original_id, original_name = seen_numbers[number]
              print(f" Duplicate Found! Number {number} is shared by:")
              print(f"   - Original: {original_name} (ID: {original_id})")
              print(f"   - Duplicate: {name} (ID: {contact_id})")
              duplicates_found = True
          else:
              seen_numbers[number] = (contact_id, name)

  if not duplicates_found:
    print("no duplicates")
  p=input("Enter 'a' to add a contact, 'd' to delete a contact, 'u' to update a contact, or 'q' to quit: ")
  if p=='a':
    k1=(input("Enter the name to add: "))
    v1=int(input("Enter mobile number: "))
    next_id = max(cb.keys()) + 1 if cb else 1
    cb[next_id] = {k1: v1}
    print("Contact", k1, "added with", next_id)

  elif p=="d":
    k2=input("Enter the name to be deleted: ")
    deleted_id = None

    for contact_id, contact_info in list(cb.items()):
      if k2 in contact_info:
        deleted_id = contact_id
        break
    if deleted_id is not None:
      del cb[deleted_id]
      print(k2,  "is deleted.")
    else:
      print(k2, "not found.")

  elif p=="u":
    k3=input("Enter the name to be updated: ")
    v2=int(input("Enter the new mobile number: "))
    updated = False
    for contact_id, contact_info in cb.items():
      if k3 in contact_info:
        contact_info[k3] = v2
        print(k3, "updated with new number",v2)
        updated = True
        break
    if not updated:
      print(k3, "not found.")

  elif p=='q':
    print("Exiting contact manager.")
    break

  else:
    print("Invalid input. Please choose 'a', 'd', 'u', or 'q'.")
