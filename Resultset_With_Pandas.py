import sqlite3
import pandas as pd

try:
    # I am assuming Company Database is "company" and making connection
    con = sqlite3.connect("company.db")
    # Making cursor to excecute query 
    cur = con.cursor()

    # Preparing Query to get the desired resultset
    fetch_sql = '''SELECT c.customer_id as Customer,c.age as Age, i.item_name as Item, SUM(o.quantity) as Quantity FROM Sales s
                        INNER JOIN Customer c
                        ON s.customer_id = c.customer_id
                        INNER JOIN Orders o
                        on s.sales_id = o.sales_id
                        INNNER JOIN Items i
                        on o.item_id = i.item_id
                    GROUP BY 1,2,3 ;
                    '''
    try:
        # Excecuting the query
        res = cur.execute(fetch_sql)
        # Fetching the data
        result = res.fetchall()
        df = pd.DataFrame(result, columns=['Customer', 'Age','Item','Quantity'])
        rslt_df = df[(18 <= df['Age'] <=35) & 
                (df['Quantity'] >0)]

        #writing resultset to CSV File
        rslt_df.to_csv('result.csv',sep = ';',header= True,index=False)
    
    except Exception as e:
     print("Query Error : ",e)
    finally:              
        # Closing the Connection and Cursor
        cur.close()
        con.close()
except Exception as e:
    print("DB Error : ",e)