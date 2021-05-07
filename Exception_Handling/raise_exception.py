# Standard Exception
try:
    raise MemoryError("Memory error")
except Exception as e:
    print("Exception Occured:", e)


# Userdefined Exception
class Accident(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg

    def print_exception(self):
        print("Exception:", self.msg)


try:
    raise Accident("Crash two cars")

except Exception as e:
    print(e)
