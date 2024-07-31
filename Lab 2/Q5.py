# 5. Compute a)sin of 60 degree b)cos of pi c)sin(0.8660254037844386) d)tan of 90 degree

import math

# a) Sine of 60 degrees
sin_60_degrees = math.sin(math.radians(60))

# b) Cosine of pi
cos_pi = math.cos(math.pi)

# c) Sine of 0.8660254037844386
sin_value = math.sin(0.8660254037844386)

# d) Tangent of 90 degrees (This will result in an undefined value in mathematics and an error in most implementations)
try:
    tan_90_degrees = math.tan(math.radians(90))
except ValueError as e:
    tan_90_degrees = str(e)

print(f"Sine of 60 degrees is: {sin_60_degrees}")
print(f"Cosine of pi is: {cos_pi}")
print(f"Sine of 0.8660254037844386 is: {sin_value}")
print(f"Tangent of 90 degrees is: {tan_90_degrees}")
