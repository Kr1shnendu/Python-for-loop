try:
    a = 10000000
    for i in range(a):
        print(i, end=" ")
except Exception as e:
    print("Exception is handled, ERROR:", e)


# can't handle this -> KeyboardInterrupt got as Error
# output:
# 70075 70076 70077 70078 70079 70080 70081 70082 70083 70084 70085 70086 70087 70088Traceback (most recent call last):
#   File "c:\Users\majik\OneDrive\Desktop\python_tasks\day8\ex1.py", line 4, in <module>
#     print(i, end=" ")
# KeyboardInterrupt
# ^C