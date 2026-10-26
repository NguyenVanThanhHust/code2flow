from code2flow import Node


def test_rshift():
    assert Node("a") >> Node("b") == "a >> b"
