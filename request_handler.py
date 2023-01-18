import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import (
    get_all_products, get_single_product,
    get_all_product_types, get_product_id, create_product_type
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
        elif resource == "types":
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
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        new_post = None
        if resource == "types":
            new_post = create_product_type(post_body)
            if 'id' in new_post:
                self._set_headers(201)
            else:
                self._set_headers(400)


        self.wfile.write(json.dumps(new_post).encode())

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
