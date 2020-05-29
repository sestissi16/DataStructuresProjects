import time

def test():
    listnew = []
    for i in range(50,000):
        listnew.append(i)
    return listnew

start_time = time.time()
test()
print(time.time() - start_time)
        
    
