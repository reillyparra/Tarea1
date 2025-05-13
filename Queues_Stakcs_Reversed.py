import time
from collections import deque

def enqueue(stack_in, value):
    stack_in.append(value)

def dequeue(stack_in, stack_out):
    if not stack_out:
        while stack_in:
            stack_out.append(stack_in.pop())
    return stack_out.pop() if stack_out else None

# 2. Pila con Colas (StackWithQueues)
def push(queue1, value):
    queue1.append(value)

def pop(queue1, queue2):
    if not queue1:
        return None
    while len(queue1) > 1:
        queue2.append(queue1.popleft())
    top_value = queue1.popleft()
    queue1, queue2 = queue2, queue1  # Intercambio de colas
    return top_value

# 3. Invertir una lista enlazada en tiempo Theta(n) con memoria constante


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev