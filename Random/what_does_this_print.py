'''
What does this print?
'''


def paradox():
    try:
        raise Exception("Here")
    except:
        return "There"
    finally:
        return "Or maybe there"

    return "Or here?"


print(paradox())
