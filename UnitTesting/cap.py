def cap_text(text):
    tokens = text.split()
    return " ".join([x.capitalize() for x in tokens])


if __name__ == "__main__":
    print(cap_text("python lang"))
