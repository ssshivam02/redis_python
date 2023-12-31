from multiprocessing import Pool
import time
def func_lazy(n):
    time.sleep(n)
    string_out = f" Sleep completed with time {str(n)}"
    return string_out
# time1 = time.time()
time_intervals = [1,2,3,4,5,6]
# for i in time_intervals:
#     print(func_lazy(i))
# time2 = time.time()
# print(f"time taken without multiprocessing: {time2 - time1}")

# using multiprocessing 
def main():
    pool = Pool(6)
    result = pool.imap_unordered(func_lazy, time_intervals)
    for each in result:
        print(each)

if __name__ == "__main__":
    time1 = time.time()
    main()
    time2 = time.time()
    print(f"time taken with multiprocessing: {time2 - time1}")
