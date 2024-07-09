import psycopg2

conn_params = {
    'database': 'n48',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': 5432
}


class DBConnect:
    def __init__(self, conn_params):
        self.conn_params = conn_params

    def __enter__(self):
        self.conn = psycopg2.connect(**conn_params)

        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

        if self.cur:
            self.cur.close()


# # select query
# with DBConnect(conn_params) as (conn, cur):
#     select_query = '''select * from users;'''
#     cur.execute(select_query)
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)

# # insert table query
# with DBConnect(conn_params) as (conn, cur):
#     insert_query = '''insert into users (firstname,lastname,username,email,age)
#                       values ('Steve','Brian','steve777','brian@gmail.com',50);'''
#     cur.execute(insert_query)
#     conn.commit()

# # update table
# with DBConnect(conn_params) as (conn, cur):
#     update_query = '''update users set age = 25 where id = 2;'''
#     cur.execute(update_query)
#     conn.commit()

# delete query
with DBConnect(conn_params) as (conn, cur):
    delete_query = '''delete from users where id = 4;'''
    cur.execute(delete_query)
    conn.commit()
