import pandas as pd
import constant as cst
import datetime
from redminelib import Redmine

redmine = Redmine(cst.URL, key=cst.KEY)
df = pd.read_csv(cst.I_PATH, parse_dates=["start_date","due_date"])
#df = pd.read_csv(cst.I_PATH)

df = df.astype({"tracker_id": object})
df = df.astype({"status_id": object})
df = df.astype({"priority_id": object})
df = df.astype({"assigned_to_id": object})

print("Data Load Done.Start Post Data")

for i in df.index:
  issue = redmine.issue.new()
  issue.project_id = df.iloc[i,0]
  issue.subject = df.iloc[i,1]
  issue.tracker_id = df.iloc[i,2]
  issue.description = df.iloc[i,3]
  issue.status_id = df.iloc[i,4]
  issue.priority_id = df.iloc[i,5]
  issue.assigned_to_id = df.iloc[i,6]
  issue.custom_fields = [{"id": 1, "value": df.iloc[i,7]}]
#  issue.start_date = datetime.date(df.iloc[i,8])
#  issue.due_date = datetime.date(df.iloc[i,9])
  print("Read Data Row : {}:{}".format(i+1,issue.subject))
  issue.save()

