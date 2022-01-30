import datetime
from redminelib import Redmine

URL="http://localhost:3010/"
KEY="4b65396a022e1658495caeef7e0684a8dcd186a7"

redmine = Redmine(URL, key=KEY)
fields = redmine.custom_field.all()
for field in fields:
  print ('{},{},{},{},{}'.format(field.id, field.name, field.customized_type, field.field_format, field.trackers[0].name))

