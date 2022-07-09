import uuid
from flask import jsonify,request,render_template,redirect, url_for
from flask_login import current_user
from app.models.usermodel import User
from app.models.orderdetailmodel import OrderDetails
def orderitem():
	#function for ordering item
	if request.method == 'POST':
		itemname = request.form["itemname"]
		nooftickets = request.form["nooftickets"]


		cost=request.form.get("cost")

		uniqueuid = uuid.uuid4().hex
		OrderDetails.objects.create(itemname=itemname,
			nooftickets=nooftickets,
			ordereduser = current_user.id,orderid=uniqueuid,cost=cost)
		user =  User.objects.get(id=current_user.id)
		orderitems = OrderDetails.objects(ordereduser=current_user.id)
		return render_template("order.html",user=user,orderitems=orderitems)
	else:
		user =  User.objects.get(id=current_user.id)
		orderitems = OrderDetails.objects(ordereduser=current_user.id)
		return render_template("order.html",user=user,orderitems=orderitems)
	


