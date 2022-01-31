import constant as cst
import datetime
from redminelib import Redmine

redmine = Redmine(cst.URL, key=cst.KEY)

fields = redmine.custom_field.all()
for field in fields:
  print ('{},{},{},{}'.format(field.id, field.name, field.customized_type, field.field_format))

