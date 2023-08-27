import http.server
import socketserver
import threading
import webbrowser

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

def reload_page():
    with open("index.html", "r") as f:
        content = f.read()
    content += "\n<script>window.location.reload();</script>\n"
    with open("index.html", "w") as f:
        f.write(content)

def start_timer():
    threading.Timer(10, reload_page).start()

if __name__ == "__main__":
    # Set the port number to serve the files
    PORT = 8000

    # Create a server with the custom request handler
    with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        
        # Open the default web browser
        webbrowser.open_new_tab(f"http://localhost:{PORT}")
        
        # Start the timer to reload the page
        start_timer()
        
        # Start serving
        httpd.serve_forever()
