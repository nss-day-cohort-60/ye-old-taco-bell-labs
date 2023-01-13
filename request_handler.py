import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import (
    get_all_products, get_single_product,
    get_all_product_types, get_product_id,
    remove_product
)


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            if path_params[2] == 'random':
                id = get_product_id()

        return (resource, id)  # This is a tuple


    def do_GET(self):
        """Handles GET requests to the server
        """

        (resource, id) = self.parse_url(self.path)

        if resource == "products":
            if id is not None:
                self._set_headers(200)
                response = get_single_product(id)
            else:
                self._set_headers(200)
                response = get_all_products()
        elif resource == "product_types":
            if id is not None:
                self._set_headers(405)
                response = ""
            else:
                self._set_headers(200)
                response = get_all_product_types()
        else:
            response = []

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server"""

        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = { "payload": post_body }
        self.wfile.write(json.dumps(response).encode())

    def do_DELETE(self):
        """Handle all DELETE requests
        """
        (resource, id) = self.parse_url(self.path)

        success = False
        if resource == 'products':
            success = remove_product(id)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())


    def do_PUT(self):
        """Handles PUT requests to the server"""
        self.do_PUT()

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()



def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
