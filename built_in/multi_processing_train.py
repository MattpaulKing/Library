import time
import concurrent.futures
from temp_lib import do_something

if __name__ == '__main__':  

    start = time.perf_counter()

    #with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
    #    results = [executor.submit(do_something, 1) for x in range(10)]
    #    for f in concurrent.futures.as_completed(results):
    #        print(f.result())

    with concurrent.futures.ProcessPoolExecutor() as executor:

        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    # List to hold the processes
    #processes = []

    #Starting all the processes
    #for _ in range(10):
    #    p = multiprocess.Process(target=do_something, args=[1.5])
    #    p.start()
    #    processes.append(p)
    
    #Joining the processes back
    #for process in processes:
    #   process.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")

    