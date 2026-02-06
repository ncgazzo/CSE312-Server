from util.response import Response
from util.request import Request
from util.Route import Route


class Router:

    def __init__(self):
        self.routesList = []


    def add_route(self, method, path, action, exact_path=False):
        self.routesList += Route(self, method,path,action,exact_path)
        # just create a new route object and add it to routeList



    def route_request(self, request, handler):
        path = request.path
        method = request.method
        res = Response()

        for route in self.routesList:

            if route.method == method:

                # if exact path is True the paths must match exactly
                if route.exact == True:
                    if route.path == path:
                        route.action(request,handler)
                        handler.request.sendall(res.to_data())
                        return

                # if exact path is false paths can partially match
                else:
                    if route.path.contains(path):
                        route.action(request,handler)
                        handler.request.sendall(res.to_data())
                        return

        # if it reaches down here no routes matched so return a 404
        res.set_status(404, "Not Found")
        res.text("Error: No Matching Path")
        handler.request.sendall("")
        return
