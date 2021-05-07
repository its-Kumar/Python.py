from datetime import date, datetime


def ValidateCard(expDate):
    if expDate > datetime.now().date():
        return "Valid"
    else:
        return "Expired"


if __name__ == "__main__":
    print(ValidateCard(date(2021, 2, 2)))
