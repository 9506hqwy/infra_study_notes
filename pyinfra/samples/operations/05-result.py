from pyinfra import config, logger
from pyinfra.operations import python, server

result = server.shell(commands="echo Hello, World!")


def output(result):
    result = server.shell(commands=f"echo {result.stdout}")


python.call(function=output, result=result)
