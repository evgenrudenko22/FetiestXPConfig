from dataclasses import dataclass
from server.url.handler import HandlerConf


@dataclass
class ServerConf:
    host: str
    port: int
    all_handlers: list[HandlerConf]
