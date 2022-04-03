import constant as cst
import datetime
from redminelib import Redmine

redmine = Redmine(cst.URL, key=cst.KEY)
issues = redmine.issue.all(sort='category:desc')
for issue in issues:
  print ('{},{},{},{},{}'.format(
    issue.id,
    issue.subject,
    issue.tracker,
    issue.status,
    #getattr(issue.custom_fields[0],'value',None),
    issue.start_date,
    )
  )

