import constant as cst
import datetime
from redminelib import Redmine

redmine = Redmine(cst.URL, key=cst.KEY)

project = redmine.project.get(1)
user = redmine.user.get(1)
group = redmine.group.get(5)
issue = redmine.issue.get(1)
query = redmine.query.get(1)
field = redmine.custom_field.get(1)

print("Redmine AttrList")
print("----------------")
print("{}\n".format(type(redmine)))

print("Project AttrList")
print("----------------")
print("{}\n".format(type(project)))
print("{}\n".format(dir(project)))

print("User AttrList")
print("----------------")
print("{}\n".format(type(user)))
print("{}\n".format(dir(user)))

print("Group AttrList")
print("----------------")
print("{}\n".format(type(group)))
print("{}\n".format(dir(group)))

print("Group users AttrList")
print("----------------")
if len(group.users) > 0:
  print("{}".format(type(group.users)))
  print("{}\n".format(type(list(group.users)[0])))
  print("{}\n".format(dir(list(group.users)[0])))
else:
  print("Empty Group users\n")

print("Group Memberships AttrList")
print("----------------")
if len(group.memberships) > 0:
  print("{}\n".format(type(list(group.memberships)[0])))
  print("{}\n".format(dir(list(group.memberships)[0])))
else:
  print("Empty Memberships\n")

print("Issue AttrList")
print("----------------")
print("{}\n".format(type(issue)))
print("{}\n".format(dir(issue)))

print("Query AttrList")
print("----------------")
print("{}\n".format(type(query)))
print("{}\n".format(dir(query)))

print("Custom Field AttrList")
print("----------------")
print("{}\n".format(type(field)))
print("{}\n".format(dir(field)))

