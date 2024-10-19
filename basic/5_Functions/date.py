import sys


def is_leap(year):
    if (year % 100) == 0 or (year % 100 != 0 and year % 4 == 0):
        return 1
    else:
        return 0


def increase_date(dd, mm, yy):
    dd += 1
    if mm > 12:
        m = mm - 12
        mm = m
        yy += 1

    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        if dd == 31:
            dd = 1
            mm += 1
    elif mm == 2:
        if is_leap(yy):
            if dd > 29:
                d = dd - 29
                dd = d
                mm += 1
        else:
            if dd > 28:
                d = dd - 28
                dd = d
                mm += 1
    else:
        if dd > 31:
            d = dd - 31
            dd = d
            mm += 1
    return dd, mm, yy


if __name__ == "__main__":
    (dd, mm, yy) = (int(x)
                    for x in input("Enter date (DD/MM/YY) : ").split("/"))

    if (yy < 1850 or yy > 2050) or (mm < 1 or mm > 12) or (dd < 1 or dd > 31):
        print("Invalid Date...!!")
        sys.exit()

    else:
        if mm == 2:
            if is_leap(yy):
                if dd > 29:
                    print("Invalid Date...!!")
                    sys.exit()
            else:
                if dd > 28:
                    print("Invalid Date...!!")
                    sys.exit()
        elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
            if dd == 31:
                print("Invalid Date...!!")
                sys.exit()

    print("Date is : {}/{}/{}".format(dd, mm, yy))
    (dd, mm, yy) = increase_date(dd, mm, yy)
    print("Increased Date is : {}/{}/{}".format(dd, mm, yy))
