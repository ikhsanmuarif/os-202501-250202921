import csv

def read_dataset(filename):
    processes = []
    allocation = {}
    request = {}

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = row['Process']
            processes.append(p)
            allocation[p] = row['Allocation']
            request[p] = row['Request']

    return processes, allocation, request


def detect_deadlock(processes, allocation, request):
    graph = {}

    for p in processes:
        graph[p] = request[p]

    deadlock_processes = []

    for p in processes:
        visited = set()
        current = p

        while current not in visited:
            visited.add(current)
            next_resource = graph[current]

            found = False
            for q in processes:
                if allocation[q] == next_resource:
                    current = q
                    found = True
                    break

            if not found:
                break
        else:
            deadlock_processes.extend(list(visited))

    return set(deadlock_processes)


if __name__ == "__main__":
    processes, allocation, request = read_dataset("dataset_deadlock.csv")
    deadlock = detect_deadlock(processes, allocation, request)

    print("=== HASIL DETEKSI DEADLOCK ===")
    if deadlock:
        print("Deadlock terdeteksi pada proses:")
        for p in deadlock:
            print("-", p)
    else:
        print("Tidak terjadi deadlock")
