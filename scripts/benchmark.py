import time
import platform
import sys

def run_benchmark():
    print("="*50)
    print("SYSTEM INFORMATION")
    print("="*50)
    print(f"OS:         {platform.system()} {platform.release()}")
    print(f"Python:     {sys.version.split()[0]}")
    
    print("\n" + "="*50)
    print("BENCHMARKING OPERATIONS")
    print("="*50)
    
    start = time.time()
    _ = [i**2 for i in range(10**6)]
    end = time.time()
    print(f"Math (Squares): {end - start:.4f}s")

if __name__ == "__main__":
    run_benchmark()
