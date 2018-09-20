def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
        "default":"This is default",
    }
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    argument = "default"
    print (SwitchExample(argument))