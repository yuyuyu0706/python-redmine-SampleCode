import datetime
from redminelib import Redmine

URL="http://localhost:3010/"
KEY="4b65396a022e1658495caeef7e0684a8dcd186a7"

redmine = Redmine(URL, key=KEY)

user = redmine.user.new()
user.login = 'test10'
user.password = 'password'
user.firstname = 'yamada'
user.lastname = 'hanako'
user.mail = 'yamada10@mail.com'
user.auth_source_id = 1
user.save()

