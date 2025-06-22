from server.server import *
from server.url.handler import *
from utils.tomlutils import *

mainServer = ServerConf("0.0.0.0", 3456, [HandlerConf("index", HandleTypes.REDIRECT, redirect_to="0.0.0.0:2222")])

register_server(mainServer)

save()