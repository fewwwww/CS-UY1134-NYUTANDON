from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
from copy import deepcopy
from math import factorial


def permutations(lst):
    stack = ArrayStack()
    result = ArrayQueue()
    for i in range(len(lst)):
        stack.push(lst[i])
    elementPrev = [stack.pop()]
    result.enqueue(elementPrev)
    while not stack.is_empty():
        elementNext = stack.pop()
        count = factorial(len(result.first()))
        for eachElement in range(count):
            elementPrev = result.dequeue()
            for eachTime in range(len(elementPrev)+1):
                element = deepcopy(elementPrev)
                element.insert(eachTime, elementNext)
                result.enqueue(element)
    return [result.dequeue() for i in range(len(result))]
