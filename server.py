import http.server
import socketserver
import webbrowser
import threading

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

def reload_page():
    webbrowser.open_new_tab(f"http://localhost:{PORT}")

def start_timer():
    threading.Timer(10, start_timer).start()
    reload_page()

# Set the port number to serve the files
PORT = 8000

# Create a server with the custom request handler
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    # Automatically open the web browser
    start_timer()
    # Start serving
    httpd.serve_forever()
