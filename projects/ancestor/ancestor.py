
def earliest_ancestor(ancestors, starting_node):

    vertices = {}

    for i in ancestors:
        vert1 = i[0]
        vert2 = i[1]

        if vert1 not in vertices:
            vertices[vert1] = set()
        if vert2 not in vertices:
            vertices[vert2] = set()

        vertices[vert2].add(vert1)

    if len(vertices[starting_node]) == 0:
        return -1

    longest = []
    length = 0

    stack = []

    stack.append([starting_node])

    while len(stack) > 0:
        path = stack.pop()

        last = path[-1]

        if len(vertices[last]) == 0 and len(path) >= length:
            if len(path) == length:
                longest.append(path)

            if len(path) > length:
                longest = []
                longest.append(path)
                length = len(path)
        
        else:
            for parent in vertices[last]:
                new_path = path.copy()

                new_path.append(parent)

                stack.append(new_path)
    
    least = None
    for i in longest:
        if least == None:
            least = i[-1]
        
        elif i[-1] < least:
            least = i[-1]

    ##### TEST TO PRINT ALL VERTICES
    # for i in vertices:
    #     print(f"{i:3}: {vertices[i]}")

    return least
    




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]



print("Should be -1: ", earliest_ancestor(test_ancestors, 10))
print("Should be -1: ",earliest_ancestor(test_ancestors, 4))
print("Should be 4: ",earliest_ancestor(test_ancestors, 9))
print("Should be 4: ",earliest_ancestor(test_ancestors, 8))
print("Should be 10: ",earliest_ancestor(test_ancestors, 6))
print("Should be 4: ",earliest_ancestor(test_ancestors, 7))