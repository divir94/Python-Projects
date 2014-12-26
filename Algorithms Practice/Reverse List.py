'''
Reverse a list by pushing items onto a stack (i.e. system stack using recursion).
'''

def reverse_list(lst, stack=[]):
    if not lst: return
    push_item = lst[0]
    reverse_list(lst[1:], stack)
    stack.append(push_item)
    return stack

print reverse_list(range(5))