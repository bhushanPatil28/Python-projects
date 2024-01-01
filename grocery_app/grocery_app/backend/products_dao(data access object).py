import mysql.connector
from sql_connection import get_sql_connection
def get_all_products(connection):

    cursor = connection.cursor()

    query = "SELECT * FROM gs.products"

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, prise_per_unit) in cursor:
        response.append({
            'product_id':product_id, 
            'name':name, 
            'uom_id':uom_id, 
            'prise_per_unit':prise_per_unit
        })

    return response
if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))