# 1. Use Python's queue data structure to implement a stack.
    # *Input*: push(1), push(2), pop(), push(3), pop(), pop()
    # *Output*: "1, None, 3, None, None"


from queue import LifoQueue

def implement_stack():
    stack = LifoQueue()

    stack.put(1)  # push(1)
    stack.put(2)  # push(2)
    popped_value = stack.get()  # pop()
    print(popped_value)

    stack.put(3)  # push(3)
    popped_value = stack.get()  # pop()
    print(popped_value)

    popped_value = stack.get()  # pop()
    print(popped_value)

implement_stack()
