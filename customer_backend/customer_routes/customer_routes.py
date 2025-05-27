from flask import Blueprint,request,jsonify
from customer_controllers.customer_controller import save_customer_data

customer_routes =Blueprint("customer_routes",__name__)

@customer_routes.route("/register",methods=['POST'])
def register_customer():
    data = request.get_json()
    #customer_id = data.get('customer_id')
    customer_name = data.get('customer_name')
    address = data.get('address')
    city = data.get('city')
    state = data.get('state')
    ZIP_code = data.get('ZIP_code')
    
    if  not customer_name or not address or not city or not state or not ZIP_code:
        return jsonify({"error": "This customer Data not required"}), 400
    
    result = save_customer_data(customer_name,address,city,state,ZIP_code)
    return jsonify(result)