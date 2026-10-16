from pyinfra.operations import files

created = files.file("/tmp/test.txt")

files.file(
    "/tmp/test.txt",
    present=False,
    _if=created.did_change,
)
