import logging

def logging_with_dict(var1, var2):
    logging.warning({"foo": var1, "bar": var2})

logging_with_dict("1234", "example")

# ```
# % python ./example2.py
# WARNING:root:{'foo': '1234', 'bar': 'example'}
# ```
