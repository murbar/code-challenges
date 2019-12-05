class TypedList:
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must be a list.")
        for element in initial_list:
            self.__check(element)
        self.elements = initial_list[:]

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError(
                "Attempted to add element of incorrect type to a typed list.")

    def __setitem__(self, i, element):
        self.__check(element)
        self.elements[i] = element

    def __getitem__(self, i):
        return self.elements[i]

# a more complete implementation should define __add__, __mul__, __len__, __delitem__, append, and insert methods
# Might also consider subclassing builtins List or UserList
# UserList exposes underlying data structure as "data" property
