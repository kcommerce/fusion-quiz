import http.server
import ssl

PORT = 4443  # Choose a port for HTTPS (e.g., 4443)

httpd = http.server.HTTPServer(('localhost', PORT), http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="certs/key.pem", certfile="certs/cert.pem", server_side=True)
print(f"Serving HTTPS on port {PORT}")
httpd.serve_forever()
