names = ["Bob", "Bill", "Jilll"]
names2 = {"name1": "Bob", "name2": "Bill", "name3": "Jill"}
s = "hello"
name = "Jill"

def do_something():
  """This will do something"""
  for name in names:
    global s
    s = name

if name == "Bob":
  print(len(name))
elif name == "Bill":
  print("gfasfg")
elif name == "Jill":
  print("Jill")
else:
  print("nothing here")




do_something()
# print(s)

