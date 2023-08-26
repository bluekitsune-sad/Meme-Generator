import http.server
import socketserver

# Set the port number to serve the files
PORT = 8000

# Create a simple HTTP server
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at http://localhost:{PORT}")
# Start serving
httpd.serve_forever()