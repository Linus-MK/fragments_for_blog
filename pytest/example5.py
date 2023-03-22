import logging
import pytest

def logging_with_dict(var1, var2):
    logging.warning({"foo": var1, "bar": var2})

def test_logging_with_dict(caplog):
    logging_with_dict("1234", "example")

    assert caplog.record_tuples[0][2] == str({"foo": "1234", "bar": "example"})

    assert caplog.records[0].message == str({"foo": "1234", "bar": "example"})

    assert caplog.records[0].msg == {"foo": "1234", "bar": "example"}
