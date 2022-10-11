

mysql = {
    'host':'localhost',
    'user':'root',
    'password':'admin',
    'db':'item_store_db'
}

mysqlconfig = f"mysql+pymysql://{mysql['user']}:{mysql['password']}@{mysql['host']}/{mysql['db']}"