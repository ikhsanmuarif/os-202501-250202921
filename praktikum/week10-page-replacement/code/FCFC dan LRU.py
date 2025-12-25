# Simulasi Page Replacement FIFO dan LRU
# Praktikum Sistem Operasi - Bab 10

def fifo(reference, frames):
    memory = []
    page_fault = 0
    pointer = 0

    print("=== FIFO ===")
    for page in reference:
        if page not in memory:
            page_fault += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory[pointer] = page
                pointer = (pointer + 1) % frames
            status = "Page Fault"
        else:
            status = "Page Hit"

        print(f"Page {page} -> {memory} ({status})")

    return page_fault


def lru(reference, frames):
    memory = []
    page_fault = 0
    last_used = {}

    print("\n=== LRU ===")
    for i, page in enumerate(reference):
        if page not in memory:
            page_fault += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = min(last_used, key=last_used.get)
                memory[memory.index(lru_page)] = page
                del last_used[lru_page]
            status = "Page Fault"
        else:
            status = "Page Hit"

        last_used[page] = i
        print(f"Page {page} -> {memory} ({status})")

    return page_fault


if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    print("Reference String:", reference_string)
    print("Jumlah Frame:", frames)

    fifo_fault = fifo(reference_string, frames)
    lru_fault = lru(reference_string, frames)

    print("\n=== Perbandingan Akhir ===")
    print("FIFO Page Fault:", fifo_fault)
    print("LRU Page Fault :", lru_fault)
