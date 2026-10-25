def get_user(cursor, uid):
    query = "SELECT * FROM users WHERE id = '" + uid + "'"
    cursor.execute(query)
    return cursor.fetchone()
