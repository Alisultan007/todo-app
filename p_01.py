#import os

#for i in range(1, 11):
    #os.makedirs(f'./test/lesson_{i}')


import os

for i in range(1, 11):
    os.makedirs(f'./test/test-v1/lesson_{"0" + str(i) if i < 10 else i}')

for i in range(1, 11):
    os.makedirs(f'./test/test-v2/lesson_{i:02d}')

for i in range(1, 11):
    os.makedirs(f'./test/test-v3/lesson_{str(i).zfill(2)}')

# os.removedirs(f'./test/test-v1/lesson_10')
# os.rmdir(f'./test/test-v1/lesson_10')
# os.remove(f'./test-v1/')

# print(os.listdir())