def add_elements(o_num):

    l = [] # list with elements

    for i in range(1, o_num+1): # user enters each element
        el = int(input(f"Enter element number {i}: "))
        l.append(el)

    return l


def t(q, capacity):

    el = []

    p_faults = 0 # number of Page Faults
    no_p_faults = 0 

    for i in range(len(q)):
        
        c = 0 # counter to check if value in list

        for e in el:
            if e == q[i]:
                c = 1
                break
            else:
                c = 0
                
        if c == 0:
            
            if i < capacity:
                el.append(q[i])
            else:
                el.remove(el[0]) # changing first el (the one that was entered first) to a new value
                el.append(q[i])
            p_faults += 1

        else:
            no_p_faults += 1

    result = [el, p_faults, no_p_faults] # gathering all values

    return result


def main():

    o_num = int(input("Enter number of elements: "))
    print()

    queue = add_elements(o_num) # adding elements to a queue
    print()

    capacity = int(input("Enter capacity: ")) # length of the list
    print()

    result = t(queue, capacity)

    print("List: ", result[0], "; Page Faults: ", result[1], "; no Page Faults: ", result[2])


main()
