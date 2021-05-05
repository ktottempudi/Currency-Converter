from http.server import HTTPServer
from server import serverHandler

HOST_NAME = 'localhost'
PORT = 8000

if __name__ == '__main__':

	server = HTTPServer((HOST_NAME, PORT), serverHandler)
	print("Server Running on PORT %s" % PORT)
	try:
		server.serve_forever()  
	except KeyboardInterrupt:
		server.server_close()

	print("Server is being closed")

