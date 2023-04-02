def add_data(processes_num):

    process_data = []

    for i in range(processes_num):

        temp = []

        process_id = int(input("Enter Process ID: "))
        arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
        burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
        print()

        temp.append(process_id) # 0 element
        temp.append(arrival_time) # 1 element
        temp.append(burst_time) # 2 element
        temp.append(0) # 3 element

        # state of the process: 0 - not executed, 1 - execution complete
        
        process_data.append(temp)

    return process_data


def test(process, time, req_time):

    # 0 element - id
    # 1 - arrival time
    # 2 - burst time
    # 3 - status
    # 4 - completion time
    # 5 - turnaround time
    # 6 - waiting time

    time += req_time # it'll be the time it finished running (but it can be not completed)
    process[2] -= req_time # setting the time that left to finish the process
    if process[2] <= 0: # if it's finished (no burst time left)
        process[3] = 1 # setting status "executed"
        process.append(time) # adding a time of completion


def calculateTurnaroundTime(process_data):

    total_turnaround_time = 0 # time for all processes to execute

    for i in range(len(process_data)):

        # turnaround_time = completion_time - arrival_time
        turnaround_time = process_data[i][4] - process_data[i][1]

        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time) # to conviniently print it in printData

    # average_turnaround_time = total_turnaround_time / processes_num
    average_turnaround_time = total_turnaround_time / len(process_data)

    return average_turnaround_time


def calculateWaitingTime(process_data, wt):

    total_waiting_time = 0 # time all processes were waiting

    for i in range(len(process_data)):

        if process_data[i][0] in wt: # if it was waiting 
            waiting_time = wt[process_data[i][0]] # taking it from dict
        else:
            waiting_time = 0

        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time) # with this we can conviniently print processes' waiting time in printData

    # average_waiting_time = total_waiting_time / processes_num
    average_waiting_time = total_waiting_time / len(process_data)

    return average_waiting_time


def printData(data, bt, wt):

    # sort processes according to the PID
    data.sort(key=lambda x: x[0])

    t_time = calculateTurnaroundTime(data)
    w_time = calculateWaitingTime(data, wt)
    
    print("Process_ID | Arrival_Time | Burst_Time   |   Completed | Completion_Time | Turnaround_Time | Waiting_Time")
    print("---------------------------------------------------------------------------------------------------------")

    for i in range(len(data)):

        for j in range(len(data[i])):

            if j == 2: # if it is a burst time we checking it in a dict
                print("      ", bt[data[i][0]], end="      |")
            else:
                print("      ", data[i][j], end="      |")

        print()

    print(f'Average Turnaround Time: {t_time}')
    print(f'Average Waiting Time: {w_time}')


def printProcess(queue_data, bt):

    # sort processes according to the PID
    queue_data.sort(key=lambda x: x[0])
    
    print("Process_ID | Arrival_Time | Burst_Time   |   Completed | Completion_Time")
    print("------------------------------------------------------------------------")

    for i in range(len(queue_data)):

        for j in range(len(queue_data[i])):

            if j != 2: # if it is a burst time we checking it in a dict
                print("     ", queue_data[i][j], end="     |")
            else:
                print("     ", bt[queue_data[i][j]], end="     |")
            
        print()


def main():

    processes_num = int(input("Enter number of processes: ")) # entering num of processes

    req_time = int(input("Enter required time to run a process: ")) # time for a process to process

    print()
    print("Reading data...")
    print()

    bt = {} # burst time dict
    wt = {} # waiting time dict

    process_data = add_data(processes_num) # adding all the data to a list (of lists)

    for process in process_data:
        bt[process[0]] = process[2] # assigning burst times to a process in dict

    temp = process_data
    temp.sort(key = lambda x:x[1]) # sorting by arrival time so we can add them to a queue in a right order

    print()
    print("Thank you!")
    print("Starting to analize data...")
    print()

    # start time: time at which the execution of the process starts
    # completion time: time at which the process completes its execution
    # burst time: total amount of time required to execute the process

    queue = [] # queue of processes

    for process in temp:
        queue.append(process) # filling queue with arrived processes (in arrival order)

    temp = [] # cleaning the temp for using it later

    l = len(queue) # it's for while we are checking all processes in queue

    time = queue[0][1] # present time but we are starting from first arriced process

    while l != 0:

        for process in queue:

            #print("Process arrived...")

            test(process, time, req_time)

            if process[3] == 0: # if not finished

                queue.append(process) # process is now the last one

                if process[0] not in wt: # if it haven't been waiting till this moment

                    wt[process[0]] = req_time*(len(queue)-1) # assigning waiting time for this process (it's the last one so it will wait required time for len-1 times)

                else:

                    w = wt[process[0]]
                    w += req_time*(len(queue)-1)
                    wt[process[0]] = w # just increasing the number with the same logic


            else:
                temp.append(process) # process finished so we are saving the results

            #print()
            #printProcess(queue, bt)
            #print()

            queue.remove(process) # deleting analized process

            time += 2 # present time counting
            
        l = len(queue)

    print("Here's your result:")
    print()

    printData(temp, bt, wt) # beatiful output (must be...)

main()
