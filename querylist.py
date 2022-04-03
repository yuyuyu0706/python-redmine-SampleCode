import constant as cst
import datetime
from redminelib import Redmine

redmine = Redmine(cst.URL, key=cst.KEY)

querys = redmine.query.all(sort='category:desc')
for query in querys:
  print ('{},{}'.format(query.id, query.name))

