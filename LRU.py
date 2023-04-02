def add_elements(o_num):

    l = [] # list with elements

    for i in range(1, o_num+1): # user enters each element
        el = int(input(f"Enter element number {i}: "))
        l.append(el)

    return l


def t(q, capacity):

    l = []

    p_faults = 0 # number of Page Faults
    no_p_faults = 0

    history = [] # list with history of all accesses (first one is the most recent one)

    for i in range(len(q)):
        
        c = 0 # counter to check if value in list

        temp = []

        history.insert(0, q[i])
        

        for s in l:

            if q[i] == s:

                c = 1
                no_p_faults +=1
                break

            else:

                c = 0
                
        if c == 0:

            p_faults += 1

            if i >= capacity:
                
                for a in history:
                    if a in l: # we checking only the values we have in l now
                        if a not in temp: # if it was used before it is not most receantly used
                            temp.append(a) # we will get a list with history of using elements in l and the last one will be the least recently used

                b = temp[len(temp)-1] # extracting the last element
                #i = l.index (b) # checking the index of element we need to remove
                l.remove(b) # removing the least recently used element

            l.append(q[i])


    result = [l, p_faults, no_p_faults] # gathering all values

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
