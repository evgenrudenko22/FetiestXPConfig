from server.server import ServerConf
from tomlkit import document, table
from tomlkit.toml_file import TOMLFile

tempToml = document()
hosts = table()

def register_server(config: ServerConf):
    server = table()
    server.add("host", config.host)
    server.add("port", config.port)
    handles = table()
    for a in config.all_handlers:
        handles[a.name] = [str(a.handle_type), a.redirect_to, a.site_name]
    server.add("all_handles", handles)
    hosts.add(config.host, server)

def save():
    tempToml.add("hosts", hosts)
    file = TOMLFile("/etc/fetiest/temp.toml")
    file.write(tempToml)
