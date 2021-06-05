import sys

bmodule = sys.builtin_module_names
print(bmodule)
print(dir(__builtins__))

#calculator 모듈 참조
import calculator
a= calculator.add(9, 8)
print(a)

