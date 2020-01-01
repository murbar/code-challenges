def reconstructTrip(tickets):
    legs = {}
    route = [None] * (len(tickets) - 1)

    for t in tickets:
        if t[0] == None:
            route[0] = t[1]

        legs[t[0]] = t[1]

    for i in range(1, len(tickets)-1):
        route[i] = legs[route[i-1]]

    return route


# Some tests
shorterSet = [
    [None, 'PDX'],
    ['PDX', 'DCA'],
    ['DCA', None],
]

longerSet = [
    ['PIT', 'ORD'],
    ['XNA', 'CID'],
    ['SFO', 'BHM'],
    ['FLG', 'XNA'],
    [None, 'LAX'],
    ['LAX', 'SFO'],
    ['CID', 'SLC'],
    ['ORD', None],
    ['SLC', 'PIT'],
    ['BHM', 'FLG'],
]

print(reconstructTrip(shorterSet))  # should print [ 'PDX', 'DCA' ]
# should print [ 'LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'CID', 'SLC', 'PIT', 'ORD' ]
print(reconstructTrip(longerSet))
