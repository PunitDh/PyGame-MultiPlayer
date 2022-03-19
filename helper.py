def read_pos(string):
    string = string.split(",")
    return int(string[0]), int(string[1])
# end


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])
# end
