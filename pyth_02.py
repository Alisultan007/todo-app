import os

for i in os.listdir('test'):
   for j in os.listdir(f'test/{i}'):
       os.removedirs(f'test/test/{i}/p_01')

