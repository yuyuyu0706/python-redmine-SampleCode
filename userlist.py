import constant as cst
import datetime
from redminelib import Redmine

redmine = Redmine(cst.URL, key=cst.KEY)

users = redmine.user.all(sort='category:desc')
for user in users:
  last_login_on = getattr(user, "last_login_on", None)
  print ('{},{},{},{}'.format(user.id, user.login, user.firstname, last_login_on))

