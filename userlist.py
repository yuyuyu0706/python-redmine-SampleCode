import datetime
from redminelib import Redmine

URL="http://localhost:3010/"
KEY="4b65396a022e1658495caeef7e0684a8dcd186a7"

redmine = Redmine(URL, key=KEY)
users = redmine.user.all(sort='category:desc')
for user in users:
  print ('{},{}'.format(user.id, user.firstname))

