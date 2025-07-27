import pymysql
import bcrypt

# Connection config
def connect_db():
    return pymysql.connect(
        host="mysql-199927-0.cloudclusters.net",
        port=10027,
        user="user001",
        password="user001@",
        database="qr_secure_db",
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# Create new user with hashed password
def create_user(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    try:
        with connect_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
                if cursor.fetchone():
                    return False
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed))
                conn.commit()
                return True
    except Exception as e:
        print(f"[ERROR] create_user: {e}")
        return False

# Verify user login
def verify_user(username, password):
    try:
        with connect_db() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
                result = cursor.fetchone()
                if result:
                    return bcrypt.checkpw(password.encode(), result['password'].encode())
    except Exception as e:
        print(f"[ERROR] verify_user: {e}")
    return False

# Fetch client data using QR
def get_client_by_qr(client_id, pin):
    try:
        with connect_db() as conn:
            with conn.cursor() as cursor:
                query = "SELECT * FROM clients WHERE id=%s AND pin=%s"
                cursor.execute(query, (client_id, pin))
                return cursor.fetchone()
    except Exception as e:
        print(f"[ERROR] get_client_by_qr: {e}")
        return None
