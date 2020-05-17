from application import db
from application.models import Books, Movies

db.drop_all()
db.create_all()

