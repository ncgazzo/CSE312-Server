from util.response import Response
from util.request import Request

class Route:

    def __init__(self, method, path, action, exact_path=False):
        self.method = ""
        self.path = ""
        self.exact = ""
        self.action = ""
