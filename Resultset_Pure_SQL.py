import sqlite3
import csv

#Company Database is "Data Engineer_ETL Assignment" :  
try:
    con = sqlite3.connect("Data Engineer_ETL Assignment.db")
    # Making cursor to excecute query 
    cur = con.cursor()

    # Preparing Query to get the desired resultset
    fetch_sql = '''SELECT c.customer_id as Customer,c.age as Age, i.item_name as Item, SUM(o.quantity) as Quantity 
                    FROM sales s
                    INNER JOIN customers c
                    ON s.customer_id = c.customer_id
                    INNER JOIN orders o
                    on s.sales_id = o.sales_id
                    INNER JOIN items i
                    on o.item_id = i.item_id
                    WHERE o.quantity >0
                    AND c.age BETWEEN 18 AND 35
                    GROUP BY 1,2,3 ;
                    '''
    try:
    # Excecuting the query
        res = cur.execute(fetch_sql)
        # Fetching the data
        result = res.fetchall()
        #writing resultset to CSV File
        with open('result.csv', 'w', newline='') as fp:
                a = csv.writer(fp, delimiter=';')
                for line in result:
                    a.writerow(line)
    except Exception as e:
     print("Query Error : ",e)
    finally:              
        # Closing the Connection and Cursor
        cur.close()
        con.close()
except Exception as e:
     print("DB Error : ",e)