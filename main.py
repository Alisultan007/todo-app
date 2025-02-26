from math import *

x = float(input())
radians_x = radians(x)
radians_2x = radians(2 * x)

sin_x = sin(radians_x)
cos_x = cos(radians_x)
tan_2x = tan(radians_2x)

result = sin_x + cos_x + tan_2x
print(result)