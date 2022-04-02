import sys
from ctypes import *


bit_depth_of_Python = "x64" if sys.maxsize > 2 ** 32 else "x86"

lib = cdll.LoadLibrary(fr"Dll\{bit_depth_of_Python}\DllPastFunction.dll")
lib.FunctionPrint1()
print()
lib.FunctionPrint2()
print()
lib.FunctionPrint3()

lib.sum_int(5, 6)  # Складывает два int
# lib.sum_double(a, b)  # Складывает два double
# lib.sum_char(a, b)  # Складывает два char
# lib.is_true(t)  # Проверяет, является ли t = True1
