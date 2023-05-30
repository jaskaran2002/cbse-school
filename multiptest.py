import multiprocessing
multiprocessing.set_start_method("fork")
a = 5

def func():
    global a
    a += 1
    print(f'{a}')

processes = []

for i in range(8):
    p = multiprocessing.Process(target=func)
    p.start()
    processes.append(p)

for process in processes:
    process.join()

print('done')