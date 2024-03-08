import http.server
import socketserver

# Define el puerto en el que deseas ejecutar el servidor
PORT = 8000

# Define la clase para manejar las peticiones HTTP
class MiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Aquí puedes personalizar la respuesta para diferentes rutas
        # Por ejemplo, puedes leer archivos de diferentes ubicaciones del sistema de archivos y devolverlos como respuesta
        # Puedes modificar esta función según las necesidades de tu sitio web
        super().do_GET()

# Configura el servidor
with socketserver.TCPServer(("", PORT), MiHandler) as httpd:
    print("Servidor activo en el puerto", PORT)
    # Inicia el bucle para esperar y manejar las solicitudes entrantes
    httpd.serve_forever()
