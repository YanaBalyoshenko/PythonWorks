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


def scheduling(process_data):

    start_time = []  # list with the time processes started to execute
    exit_time = [] # list with the time processes finished executing
    time = 0 # present time

    #sort processes according to the arrival time
    process_data.sort(key=lambda x: x[1])

    for i in range(len(process_data)): # each process

        ready_queue = [] #processes ready to execute
        queue = [] # not arrived processes

        temp = []

        # checking all processes (j - each process)
        for j in range(len(process_data)):

            if (process_data[j][1] <= time) and (process_data[j][3] == 0):
            # process've already arrived | process haven't been executed yet

                temp.append(process_data[j][0])
                temp.append(process_data[j][1])
                temp.append(process_data[j][2])

                ready_queue.append(temp) # add to a list with processes ready to execute

                temp = []

            elif process_data[j][3] == 0:
                # process haven't been executed and haven't arrived yet

                temp.append(process_data[j][0])
                temp.append(process_data[j][1])
                temp.append(process_data[j][2])

                queue.append(temp)

                temp = []

        if len(ready_queue) != 0: # if some processes arrived

            # sort the processes according to the burst time
            ready_queue.sort(key=lambda x: x[2])
            
            start_time.append(time)

            time += ready_queue[0][2] # present time += burst time of process next in queue

            e_time = time
            exit_time.append(e_time)

            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]: # if process is now executing
                    break

            process_data[k][3] = 1 # process status changing to executed
            process_data[k].append(e_time)

        elif len(ready_queue) == 0: # no processes arrived

            if time < queue[0][1]:
                time = queue[0][1] # setting present time to a time first process arrived

            start_time.append(time)

            time = time + queue[0][2]

            e_time = time
            exit_time.append(e_time)

            for k in range(len(process_data)):
                if process_data[k][0] == queue[0][0]:
                    break

            process_data[k][3] = 1
            process_data[k].append(e_time)

    return process_data


def calculateTurnaroundTime(process_data):

    total_turnaround_time = 0 # time for all processes to execute

    for i in range(len(process_data)):

        # turnaround_time = completion_time - arrival_time
        turnaround_time = process_data[i][4] - process_data[i][1]

        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)

    # average_turnaround_time = total_turnaround_time / processes_num
    average_turnaround_time = total_turnaround_time / len(process_data)

    return average_turnaround_time


def calculateWaitingTime(process_data):

    total_waiting_time = 0 # time all processes were waiting

    for i in range(len(process_data)):
        
        # waiting_time = turnaround_time - burst_time
        waiting_time = process_data[i][5] - process_data[i][2]

        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)

    # average_waiting_time = total_waiting_time / processes_num
    average_waiting_time = total_waiting_time / len(process_data)

    return average_waiting_time


def printData(process_data, average_turnaround_time, average_waiting_time):

    # sort processes according to the PID
    process_data.sort(key=lambda x: x[0])
    
    print("Process_ID | Arrival_Time | Burst_Time   |   Completed | Completion_Time | Turnaround_Time | Waiting_Time")
    print("---------------------------------------------------------------------------------------------------------")

    for i in range(len(process_data)):

        for j in range(len(process_data[i])):

            if j == 0:
                print("    ", process_data[i][j], end="     |      ")
            else:
                print(process_data[i][j], end="       |       ")
        print()

    print(f'Average Turnaround Time: {average_turnaround_time}')
    print(f'Average Waiting Time: {average_waiting_time}')


def main():

    processes_num = int(input("Enter number of processes: ")) #entering num of processes

    print()
    print("Please give a data:")
    print()

    process_data = add_data(processes_num) # adding all the data to a list (of lists)

    print()
    print("Thank you!")
    print("Starting to analize data...")
    print()

    data = scheduling(process_data) # deciding what to execute next and adding a queue to a list

    # start time: time at which the execution of the process starts
    # completion time: time at which the process completes its execution
    # burst time: total amount of time required to execute the process

    t_time = calculateTurnaroundTime(data) # turnaround time: completion time - arrival time
    w_time = calculateWaitingTime(data) # waiting time: turnaround time - burst time

    print("Here's your result:")
    print()

    printData(data, t_time, w_time) # beatiful output (must be...)

main()
