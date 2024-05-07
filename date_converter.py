from convertdate import persian

def to_persian(dt):
    """ Gets a datetime object, and converts it to persian datetime. """
    return persian.from_gregorian(int(dt.strftime("%Y")), int(dt.strftime("%m")), int(dt.strftime("%d")))