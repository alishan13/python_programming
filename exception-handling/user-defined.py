class IvalidData(Exception):
    pass
class InvalidMarks(Exception):
    pass

marks=int(input("Enter Marks for students :"))
try:
    if marks <0 or marks>100:
        raise InvalidMarks
except InvalidMarks:
    print("Marks should be in between 0 and 100")