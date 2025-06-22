from dataclasses import dataclass
from enum import Enum


class HandleTypes(Enum):
    REDIRECT = 0
    WWW = 1

    def __str__(self):
        if self.value == self.REDIRECT:
            return "redirect"
        elif self.value == self.WWW:
            return "www"
        return ""

@dataclass
class HandlerConf:
    name: str
    handle_type: HandleTypes

    # for redirect
    redirect_to: str = ""

    # for www
    site_name: str = ""

    def _get_endpoint(self) -> list[str]:
        if self.handle_type == HandleTypes.REDIRECT:
            return ["url", self.redirect_to]
        elif self.handle_type == HandleTypes.WWW:
            return ["site", self.site_name]
        return ["none"]
