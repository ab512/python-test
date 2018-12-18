birthday=input("birthday:")
if birthday > 18:
  print("adult")
  print("age is %s" % birthday)
elif(birthday > 12):
  print("teenager")
  print("age is %s"% birthday)
else:
  print("kid")
  print("age is %s"% birthday)
  