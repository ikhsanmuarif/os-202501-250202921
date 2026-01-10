#!/usr/bin/env python3
"""
Program uji untuk mengamati dampak resource limit (CPU & Memory)
pada Docker container
"""

import time
import sys
import os

def cpu_intensive_task(duration=5):
    """Tugas komputasi intensif untuk menguji limit CPU"""
    print(f"[CPU TEST] Memulai komputasi intensif selama {duration} detik...")
    start_time = time.time()
    counter = 0
    
    while time.time() - start_time < duration:
        # Operasi matematika berulang
        result = sum([i**2 for i in range(1000)])
        counter += 1
    
    elapsed = time.time() - start_time
    print(f"[CPU TEST] Selesai!")
    print(f"[CPU TEST] Iterasi: {counter:,}")
    print(f"[CPU TEST] Waktu: {elapsed:.2f} detik")
    print(f"[CPU TEST] Rate: {counter/elapsed:.2f} iterasi/detik")
    return counter

def memory_intensive_task(size_mb=100):
    """Tugas alokasi memori untuk menguji limit memory"""
    print(f"\n[MEMORY TEST] Mencoba alokasi memori {size_mb} MB...")
    try:
        # Alokasi memori bertahap
        data = []
        chunk_size = 1024 * 1024  # 1 MB
        
        for i in range(size_mb):
            # Alokasi 1 MB data
            chunk = bytearray(chunk_size)
            data.append(chunk)
            
            if (i + 1) % 50 == 0:
                print(f"[MEMORY TEST] Teralokasi: {i + 1} MB")
        
        print(f"[MEMORY TEST] Berhasil alokasi {size_mb} MB")
        print(f"[MEMORY TEST] Total items: {len(data)}")
        
        # Tahan memori sebentar
        time.sleep(2)
        
        return True
    except MemoryError:
        print(f"[MEMORY TEST] GAGAL! Memory Error saat alokasi")
        return False
    except Exception as e:
        print(f"[MEMORY TEST] ERROR: {e}")
        return False

def print_header():
    """Cetak header informasi"""
    print("=" * 60)
    print("DOCKER RESOURCE LIMIT TEST")
    print("=" * 60)
    print(f"PID: {os.getpid()}")
    print(f"Python: {sys.version.split()[0]}")
    print("=" * 60)

def main():
    print_header()
    
    # Test 1: CPU Intensive
    print("\n--- TEST 1: CPU INTENSIVE ---")
    iterations = cpu_intensive_task(duration=5)
    
    # Test 2: Memory Allocation
    print("\n--- TEST 2: MEMORY ALLOCATION ---")
    memory_success = memory_intensive_task(size_mb=150)
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"CPU Test: {iterations:,} iterasi")
    print(f"Memory Test: {'SUKSES' if memory_success else 'GAGAL'}")
    print("=" * 60)

if __name__ == "__main__":
    main()