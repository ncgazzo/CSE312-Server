class Request:

    def __init__(self, request: bytes):
        # TODO: parse the bytes of the request and populate the following instance variables

        request = request.split(b"\r\n\r\n")
        self.body = request.pop(1)                      # pop body from request and save before decoding

        request = request.pop().decode("utf-8")
        splitRequest = request.split('\r\n')            # split on newline to break into each line

        requestLine = splitRequest.pop(0).split(' ')    # split first line on spaces to get 3 parts of request line

        self.method = requestLine[0]
        self.path = requestLine[1]
        self.http_version = requestLine[2]

        self.headers = {}
        self.cookies = {}
                                                        # remaining lines of request are all headers
        for line in splitRequest:                       # headers are written key: value
            splitHeader = line.split(': ')              # space is "optional" but must be included here for localhost:8080

            self.headers[splitHeader[0].strip()] = splitHeader[1].strip()

            if splitHeader[0].strip().lower() == "cookie":      # cookies are written key= value and split on ;
                cookies = splitHeader[1].strip().split(";")

                for cookie in cookies:                  # choosing to ignore runtime out of laziness :P
                    splitCookie = cookie.split("=")
                    self.cookies[splitCookie[0].strip()] = splitCookie[1].strip()



def test1():
    request = Request(b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\n\r\n')
    assert request.method == "GET"
    assert "Host" in request.headers
    assert request.headers["Host"] == "localhost:8080"  # note: The leading space in the header value must be removed
    assert request.body == b""  # There is no body for this request.
    # When parsing POST requests, the body must be in bytes, not str

    # This is the start of a simple way (ie. no external libraries) to test your code.
    # It's recommended that you complete this test and add others, including at least one
    # test using a POST request. Also, ensure that the types of all values are correct


if __name__ == '__main__':
    test1()
