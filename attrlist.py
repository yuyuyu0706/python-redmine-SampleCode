import datetime
from redminelib import Redmine

URL="http://localhost:3010/"
KEY="4b65396a022e1658495caeef7e0684a8dcd186a7"

redmine = Redmine(URL, key=KEY)

project = redmine.project.get(1)
user = redmine.user.get(1)
group = redmine.group.get(6)
issue = redmine.issue.get(1)
field = redmine.custom_field.get(1)

print("Project AttrList")
print("----------------")
print("{}\n".format(dir(project)))

print("User AttrList")
print("----------------")
print("{}\n".format(dir(user)))

print("Group AttrList")
print("----------------")
print("{}\n".format(dir(group)))

print("Group users AttrList")
print("----------------")
if len(group.users) > 0:
  print("{}\n".format(dir(list(group.users)[0])))
else:
  print("Empty Group users\n")

print("Group Memberships AttrList")
print("----------------")
if len(group.memberships) > 0:
  print("{}\n".format(dir(list(group.memberships)[0])))
else:
  print("Empty Memberships\n")

print("Issue AttrList")
print("----------------")
print("{}\n".format(dir(issue)))

print("Custom Field AttrList")
print("----------------")
print("{}\n".format(dir(field)))

