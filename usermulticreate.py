import datetime
import pandas as pd
import redminelib
from redminelib import Redmine

URL="http://localhost:3010/"
KEY="4b65396a022e1658495caeef7e0684a8dcd186a7"
PATH="./data/input_users.csv"

redmine = Redmine(URL, key=KEY)
df = pd.read_csv(PATH)

df = df.astype({"auth_source_id": object})

print("Data Load Done.Start Post Users")

for i in df.index:
  user = redmine.user.new()
  user.login = df.iloc[i,0]
  user.firstname = df.iloc[i,1]
  user.lastname = df.iloc[i,2]
  user.mail = df.iloc[i,3]
  user.auth_source_id = df.iloc[i,4]
  print("Read Data Row : {}:{}".format(i+1,user.login))
  try:
    user.save()
  except redminelib.exceptions.ValidationError as e:
    print(e)
    print(type(e))
  
