number_a = 5
number_b = 0

try:
    divide = number_a / number_b
    print(divide)
except ZeroDivisionError:
    print("error ZeroDivisionError!")
except:
    print("error!")
else:
    print("ok!")
finally:
    print("run somefunction()")
