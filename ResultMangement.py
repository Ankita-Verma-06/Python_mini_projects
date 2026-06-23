sr={"Jyoti":{"python":90, "math":96, "english":92, "dsa":93},
    "Pinky":{"python":85, "math":82, "english":88, "dsa":80},
    "Ritu":{"python":70, "math":70, "english":85, "dsa":72},
    "Rahul":{"python":50, "math":52, "english":59, "dsa":51},
    "Sahil":{"python":60, "math":50, "english":65, "dsa":53},
    "Mohit":{"python":68, "math":55, "english":89, "dsa":77}}
sum=0
total_sum=0
topper=""
highest_marks=0
grades=[]
for key, value in sr.items():
  print(key)
  for key2, value2 in value.items():
    print(key2+":",value2)
    sum=sum+value2
    total_sum=total_sum+value2
  print("sum:",sum)
  if sum > highest_marks:
      highest_marks = sum
      topper = key
  if sum >= 380:
        grade = "A+"
  elif sum >= 360:
        grade = "A"
  elif sum >= 340:
        grade = "B+"
  elif sum >= 320:
        grade = "B"
  elif sum >= 300:
        grade = "C+"
  elif sum >= 280:
        grade = "C"
  elif sum >= 260:
        grade = "D+"
  elif sum >= 240:
        grade = "C"
  else:
        grade = "D"
  grades.append(grade)
  print("\n")
  sum=0
average=total_sum/len(sr)
print("average marks of class: ", average)
print("topper of the class: ", topper)
print(grades)


