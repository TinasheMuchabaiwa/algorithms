'''
PROBLEM DESCRIPTION:

Reverse a list of integers.
'''

# solution 1 - using recursion
'''The idea is to use recursion to reverse the list.
    The base case is when the list is empty, return an empty list.
    Otherwise, return the last element of the list,
    followed by the reversed list of the rest of the list.
'''


def reverse_list_rec1(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_list_rec1(lst[:-1])


def reverse_list_rec2(lst, lst2=[]):
    if len(lst) == 0:
        return lst2
    lst2.append(lst[-1])
    return reverse_list_rec2(lst[:-1], lst2)


# solution 2 - memoization
'''The idea is to use memoization to store the reversed list.
    The base case is when the list is empty, return an empty list.
    If the list is already stored in the memo dict, return the value.
    Otherwise, calculate the reversed list and store it in the memo dict.
'''


def reverse_list_memo1(lst, memo={}):
    if not lst:
        return []
    if tuple(lst) in memo:
        return memo[tuple(lst)]
    memo[tuple(lst)] = [lst[-1]] + reverse_list_memo1(lst[:-1], memo)
    return memo[tuple(lst)]


def reverse_list_memo2(lst, lst2=[], memo={}):
    if len(lst) == 0:
        return lst2
    if tuple(lst) in memo:
        return memo[tuple(lst)]
    lst2.append(lst[-1])
    memo[tuple(lst)] = reverse_list_memo2(lst[:-1], lst2, memo)
    return memo[tuple(lst)]


# solution 3 - using a loop
'''The idea is to use a loop to reverse the list.
    Initialize an empty list.
    Iterate over the list in reverse order,
    append each element to the new list.
    Return the new list.
'''


def reverse_list_loop(lst):
    new_lst = []
    for i in range(len(lst)-1, -1, -1):
        new_lst.append(lst[i])
    return new_lst
