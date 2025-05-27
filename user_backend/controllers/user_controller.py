# def save_user_data(data):
#     # For now, just print (later DB save panna use pannu)
#     print("Saving user data:", data)
# controllers/user_controller.py

from config.db_config import get_db_connection

def save_user_data(name ,user_name, email ,password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "INSERT INTO users (name ,user_name, email ,password) VALUES (%s, %s ,%s,%s)"
    values = (name ,user_name, email ,password)
    
    cursor.execute(query, values)
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return {"message": "User inserted successfully"}

