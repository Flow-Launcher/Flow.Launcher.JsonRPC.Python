from __future__ import annotations

from dataclasses import dataclass, field
from json import dumps, loads


@dataclass
class RPC:
    """
    FlowLauncher standard JSON-RPC container.

    Parameters
    ----------
    method : {"query", "context_menu", "Flow.Launcher.ChangeQuery", \
"Flow.Launcher.ShellRun", "Flow.Launcher.CloseApp", "Flow.Launcher.HideApp", \
"Flow.Launcher.ShowApp", "Flow.Launcher.ShowMsg", "Flow.Launcher.OpenSettingDialog",\
"Flow.Launcher.StartLoadingBar", "Flow.Launcher.StartLoadingBar", \
"Flow.Launcher.ReloadPlugins"}, default "query"

    parameters : list, default []

    result : list, default []

    debugMessage : str, default ""
    """

    method: str = "query"
    parameters: list = field(default_factory=list)
    result: list = field(default_factory=list)

    debugMessage: str = ""

    # proxy is not working now
    # proxy: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """
        Return JSON-RPC as dict.
        """

        return self.__dict__

    def to_string(self) -> str:
        """
        Convert JSON-RPC to string.
        """

        return dumps(self.to_dict())

    @classmethod
    def from_dict(cls, **kwargs) -> RPC:
        """
        Generate JSON-RPC from dict.

        Equivalent to ``RPC(**kwargs)``.
        """

        return cls(**kwargs)

    @classmethod
    def from_string(cls, string: str) -> RPC:
        """
        Generate JOSN-RPC from string.
        """

        return cls(**loads(string)) if string else cls()
