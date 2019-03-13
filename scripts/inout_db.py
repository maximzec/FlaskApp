import MySQLdb as db

connection = db.connect(user='maximzec3200', password='27854565A', host='db4free.net', database='answerstable')
cursor = connection.cursor()


def add_user(user):
    return user

def get_user(email , password):
    get_request = "SELECT * WHERE "
