# -*- coding: utf-8 -*-


import sys
from inspect import getmembers, ismethod

from RPC import RPC


class FlowLauncher:
    """
    Flow.Launcher python plugin base
    """

    def __init__(self):
        if len(sys.argv) > 1:
            # Gets JSON-RPC from Flow Launcher process.
            self.rpc_request = RPC.from_string(sys.argv[1])
        else:
            # defalut JSON-RPC
            self.rpc_request = RPC()

        # Run 'method'
        method_name = getmembers(self, predicate=ismethod)
        request_method = dict(method_name)[self.rpc_request.method]
        self.rpc_request.result = request_method(*self.rpc_request.parameters)

        if self.rpc_request.method in {"query", "context_menu"}:
            self.rpc_request.to_string()

    def query(self, param: str = "") -> list:
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
        self.debugMessage = msg
