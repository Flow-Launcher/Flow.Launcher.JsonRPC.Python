# -*- coding: utf-8 -*-


import inspect
import json
import sys


class FlowLauncher:
    """
    Flow.Launcher python plugin base
    """

    def __init__(self):
        # TODO: try other way to get argv not using index
        # with this, to test a plugin, it has to likes `python test.py {}`. Add `{}`.
        # It is better with like this `python test.py`, when the input is empty.
        rpc_request = json.loads(sys.argv[1])

        # proxy is not working now
        self.proxy = rpc_request.get("proxy", {})
        request_method_name = rpc_request.get("method", "query")
        request_parameters = rpc_request.get("parameters", [])
        methods = inspect.getmembers(self, predicate=inspect.ismethod)

        request_method = dict(methods)[request_method_name]
        results = request_method(*request_parameters)

        if request_method_name in ["query", "context_menu"]:
            print(json.dumps({"result": results}))

    def query(self, param: str = ''):
        """
        sub class need to override this method
        """
        return []

    def context_menu(self, data):
        """
        optional context menu entries for a result
        """
        return []

    def debug(self, msg):
        """
        alert msg
        """
        print("DEBUG:{}".format(msg))
        sys.exit()
