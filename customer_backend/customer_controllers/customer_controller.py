from customer_config.customer_db_config import get_customer_db_connecction

def save_customer_data(customer_name, address, city, state, ZIP_code):
    con = get_customer_db_connecction()
    cursor = con.cursor()
    
    query = """INSERT INTO customer_details ( customer_name , address , city , state , ZIP_code) 
            VALUES (%s ,%s ,%s , %s , %s)
            """
    values = (customer_name, address, city, state, ZIP_code)

    cursor.execute(query, values)
    con.commit()
    
    cursor.close()
    con.close()

    return {"message": "Customer Details inserted successfully"}