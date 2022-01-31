import constant as cst
import datetime
from redminelib import Redmine

redmine = Redmine(cst.URL, key=cst.KEY)
groups = redmine.group.all(sort='category:desc')

for group in groups:
  for user in list(group.users):
    print ('{},{},{},{}'.format(group.id, group.name, user.id, user.name))

