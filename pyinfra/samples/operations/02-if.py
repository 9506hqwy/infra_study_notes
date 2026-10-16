from pyinfra import host
from pyinfra.facts.files import File
from pyinfra.facts.server import LinuxName
from pyinfra.operations import files, server

if host.get_fact(LinuxName) == "CentOS":
    server.shell(commands='echo Static Condition')

server.shell(
    commands='echo Dynamic Condition1',
    _if=lambda: host.get_fact(File, "/tmp/test.txt")
)

files.file("/tmp/test.txt")

server.shell(
    commands='echo Dynamic Condition2',
    _if=lambda: host.get_fact(File, "/tmp/test.txt")
)
