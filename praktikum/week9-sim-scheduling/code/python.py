# Simulasi Scheduling CPU FCFS

processes = [
    ("P1", 0, 6),
    ("P2", 1, 8),
    ("P3", 2, 7),
    ("P4", 3, 3),
]

def fcfs(processes):
    time = 0
    result = []

    for p in processes:
        pid, arrival, burst = p
        if time < arrival:
            time = arrival
        waiting = time - arrival
        turnaround = waiting + burst
        time += burst
        result.append((pid, waiting, turnaround))

    return result


print("=== FCFS ===")
for p in fcfs(processes):
    print(p)


