# -*- coding: utf-8 -*-


import inspect
import sys

import demjson


class FlowLauncher:
    """
    Flow.Launcher python plugin base
    """

    def __init__(self):

        rpc_request = {'method': 'query', 'parameters': ['']}
        if len(sys.argv) > 1:
            rpc_request = demjson.decode(sys.argv[1])

        # proxy is not working now
        # self.proxy = rpc_request.get("proxy", {})

        request_method_name = rpc_request.get("method", "query")
        request_parameters = rpc_request.get("parameters", [])
        methods = inspect.getmembers(self, predicate=inspect.ismethod)

        request_method = dict(methods)[request_method_name]
        results = request_method(*request_parameters)

        if request_method_name in ["query", "context_menu"]:
            print(demjson.encode({"result": results}))

    def query(self, param: str = '') -> list:
        """
        sub class need to override this method
        """
        return []

    def context_menu(self, data) -> list:
        """
        optional context menu entries for a result
        """
        return []

    def debug(self, msg: str):
        """
        alert msg
        """
        print(f"DEBUG:{msg}")
        sys.exit()
