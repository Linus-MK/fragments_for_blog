def logging_dummy(msg, *args, **kwargs):
    print(msg)
    print(args)
    print(kwargs)

print("Example 1")
logging_dummy("simple string")
print("Example 2")
logging_dummy("%s before you %s", "Look", "leap!")
print("Example 3")
logging_dummy({"foo": "1234", "bar": "example"})
print("END")
