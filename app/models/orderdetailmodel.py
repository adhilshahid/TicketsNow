#order details model
from app.app import db
from app.models.usermodel import User

class OrderDetails(db.Document):
	itemname = db.StringField(required=True)
	nooftickets = db.StringField(required=True)
	ordereduser = db.ReferenceField(User)
	statusoforder = db.StringField(default="Yet to confirm")
	orderid = db.StringField(required=True)
	cost = db.StringField(required=True)