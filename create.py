from application import db
from application.models import menu, member, Typedish

db.drop_all()
db.create_all()

