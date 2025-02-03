from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2
from urllib.parse import parse_qs
import os

# Database 
DB_NAME = "mydbcrud"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

class CRUDHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.serve_file("templates/index.html")
        elif self.path == "/create":
            self.serve_file("templates/create.html")
        elif self.path == "/read":
            self.serve_read_page()
        elif self.path == "/update":
            self.serve_file("templates/update.html")
        elif self.path == "/delete":
            self.serve_file("templates/delete.html")
        else:
            self.send_error(404, "Page not found")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = parse_qs(post_data)

        if self.path == "/create":
            name = data.get("name")[0]
            email = data.get("email")[0]
            self.create_user(name, email)
        elif self.path == "/update":
            user_id = int(data.get("id")[0])
            name = data.get("name", [None])[0]
            email = data.get("email", [None])[0]
            self.update_user(user_id, name, email)
        elif self.path == "/delete":
            user_id = int(data.get("id")[0])
            self.delete_user(user_id)

    def serve_file(self, file_path):
        try:
            with open(file_path, "rb") as file:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, "File not found")

    def serve_read_page(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            content = "<h1>Users List</h1><ul>"
            for user in users:
                content += f"<li>{user[0]}: {user[1]}, {user[2]}</li>"
            content += "</ul><a href='/'>Back to Home</a>"
            self.send_response(200)
            self.end_headers()
            self.wfile.write(content.encode())
        except Exception as e:
            self.send_error(500, f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def create_user(self, name, email):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            self.redirect("/")
        except Exception as e:
            self.send_error(500, f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def update_user(self, user_id, name, email):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            updates = []
            params = []
            if name:
                updates.append("name = %s")
                params.append(name)
            if email:
                updates.append("email = %s")
                params.append(email)
            params.append(user_id)
            query = f"UPDATE users SET {', '.join(updates)} WHERE id = %s"
            cursor.execute(query, params)
            conn.commit()
            self.redirect("/")
        except Exception as e:
            self.send_error(500, f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def delete_user(self, user_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            conn.commit()
            self.redirect("/")
        except Exception as e:
            self.send_error(500, f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def redirect(self, path):
        self.send_response(303)
        self.send_header("Location", path)
        self.end_headers()

if __name__ == "__main__":
    PORT = 8080
    server = HTTPServer(("localhost", PORT), CRUDHandler)
    print(f"Server running at http://localhost:{PORT}")
    server.serve_forever()
