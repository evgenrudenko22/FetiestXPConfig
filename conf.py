from server.server import *
from server.url.handler import *
from utils.tomlutils import *

# Example how to create api handle
mainServer = ServerConf("0.0.0.0", 3456, [HandlerConf("index", HandleTypes.REDIRECT, redirect_to="0.0.0.0:2222")])
# example how to create website(html, css, js) handle
myWebSite = ServerConf("example.com", 80, [HandlerConf("index", HandleTypes.WWW, site_name="example.com")])

# register our servers
register_server(mainServer)
register_server(myWebSite)

# save it all in temp.toml
save()