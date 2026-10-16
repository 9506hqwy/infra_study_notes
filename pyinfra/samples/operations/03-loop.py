from pyinfra import host
from pyinfra.operations import server

for i in host.loop(range(0, 3)):
    if i != 1:
        server.shell(commands=f'echo {i}')
