import datetime
from redminelib import Redmine

URL="http://localhost:3010/"
KEY="4b65396a022e1658495caeef7e0684a8dcd186a7"

redmine = Redmine(URL, key=KEY)

issue = redmine.issue.new()
issue.project_id = 'cirius'
issue.subject = 'Python-redmine'
issue.tracker_id = 1
issue.description = 'チケットの内容をしめす。\n改行もできる。'
issue.status_id = 1
issue.priority_id = 1
issue.assigned_to_id = 1
issue.start_date = datetime.date(2022, 1, 1)
issue.due_date = datetime.date(2022, 2, 1)

issue.save()

