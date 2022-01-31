import constant as cst
import datetime
from redminelib import Redmine

redmine = Redmine(cst.URL, key=cst.KEY)

user = redmine.user.new()
user.login = 'test10'
user.password = 'password'
user.firstname = 'yamada'
user.lastname = 'hanako'
user.mail = 'yamada10@mail.com'
user.auth_source_id = 1
user.save()

