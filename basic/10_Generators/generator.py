"""
Generator saves memory as well as CPU.
"""


def remote_control_next():
    yield "cnn"
    yield "HBO"
    yield "CN"


itr = remote_control_next()
print(type(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))

for c in remote_control_next():
    print(c)
