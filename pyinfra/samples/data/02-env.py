from pyinfra import config, logger
from pyinfra.operations import python, server

config.INHERIT_ENV = ["KEY1", "KEY2", "KEY3"]

config.ENV = {
    "KEY1": "CONFIG VALUE",
    "KEY2": "CONFIG VALUE",
}

result = server.shell(
    name="Print environment KEY",
    commands=[
        "echo $KEY1",
        "echo $KEY2",
        "echo $KEY3",
    ],
    _env={
        "KEY1": "ARG VALUE"
    },
)


def output(result):
    logger.info(result.stdout)


python.call(
    name="Display output",
    function=output,
    result=result,
)
