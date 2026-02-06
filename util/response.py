import json


class Response:
    def __init__(self):
        self.status = b'200 OK'
        self.contentType = b'Content-Type: text/plain; charset=utf-8'
        self.contentLength = 0
        self.headersString = b''
        self.cookiesString = b''
        self.bodyString = b''


    def set_status(self, code, text):
        self.status = b''+ code + text
        return self

    def headers(self, headers):
        for header in headers:
            if header[0].lower() == "content-type":
                self.contentType = b'Content-Type: ' + header[1] + b'\r\n'

            if header[0].lower() == "content-length":
                self.contentLength = header[1]

            else:
                self.headersString += header + b': ' + headers[header] + b'\r\n' # headers are written key: value

        return self

    def cookies(self, cookies):
        for cookie in cookies:

            self.cookiesString += cookie + b': ' + cookies[cookie] + b'\r\n'
        return self

    def bytes(self, data):
        self.bodyString += data.encode('utf-8')
        self.contentLength += len(self.bodyString)
        return self

    def text(self, data):
        self.bodyString += data.encode('utf-8')
        self.contentLength += len(self.bodyString)
        return self

    def json(self, data):
        data = json.dumps(data)
        self.bodyString = data
        self.contentType += b'Content-Type: application/json;'
        self.contentLength = len(self.bodyString)
        return self

    def to_data(self):
        length = b'Content-Length: ' + str(self.contentLength).encode('utf-8') + b'\r\n'
        self.headersString += b'X-Content-Type-Options: nosniff'
        return b'HTTP/1.1 ' + self.status + b'\r\n' + self.contentType + b'\r\n' + length +  self.headersString + self.cookiesString + b'\r\n' + self.bodyString


def test1():
    res = Response()
    res.text("hello")
    expected = b'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\nContent-Length: 5\r\n\r\nhello'
    actual = res.to_data()
    assert actual == expected


if __name__ == '__main__':
    test1()
