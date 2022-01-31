import constant as cst
import datetime
from redminelib import Redmine

redmine = Redmine(cst.URL, key=cst.KEY)

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

