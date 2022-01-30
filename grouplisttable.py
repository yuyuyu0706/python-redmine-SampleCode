import datetime
from redminelib import Redmine

URL="http://localhost:3010/"
KEY="4b65396a022e1658495caeef7e0684a8dcd186a7"

redmine = Redmine(URL, key=KEY)
groups = redmine.group.all(sort='category:desc')

for group in groups:
  for user in list(group.users):
    print ('{},{},{},{}'.format(group.id, group.name, user.id, user.name))

