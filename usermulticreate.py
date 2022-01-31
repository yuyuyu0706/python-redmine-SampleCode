import pandas as pd
import constant as cst
import datetime
import redminelib
from redminelib import Redmine

#PATH="./data/input_users.csv"

redmine = Redmine(cst.URL, key=cst.KEY)
df = pd.read_csv(cst.U_PATH)

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
  
