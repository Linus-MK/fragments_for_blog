import logging
import pytest

def logging_with_dict(var1, var2):
    logging.warning({"foo": var1, "bar": var2})

def test_logging_with_dict(caplog):

    logging_with_dict("1234", "example")

    print(caplog.records[0])
    assert caplog.records[0].foo == "1234"
