from __future__ import annotations

from dataclasses import dataclass, field
from json import dumps, loads


@dataclass
class RPC:
    method: str = "query"
    parameters: list = field(default_factory=list)
    result: list = field(default_factory=list)

    debugMessage: str = ""

    # proxy is not working now
    # proxy: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return self.__dict__

    def to_string(self) -> str:
        return dumps(self.to_dict())

    @classmethod
    def from_dict(cls, **kwargs) -> RPC:
        return cls(**kwargs)

    @classmethod
    def from_string(cls, string: str) -> RPC:
        return cls(**loads(string)) if string else cls()
