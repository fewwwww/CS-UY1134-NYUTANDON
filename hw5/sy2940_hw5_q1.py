from ArrayStack import ArrayStack

arithmeticExpression = ["+", "-", "*", "/"]
inputPrompt = input("-->")

while inputPrompt != "done()":
    isAssigning = False
    stack = ArrayStack()
    inputPromptLst = inputPrompt.split()
    for char in inputPromptLst:
        if char == "=":
            isAssigning = True
            resultAssigned = stack.pop()
        elif char in arithmeticExpression:
            varNext = stack.pop()
            varPrev = stack.pop()
            result = eval(f"{varPrev}{char}{varNext}")
            stack.push(str(result))
        else:
            stack.push(char)
    resultPrinted = eval(stack.pop())
    if isAssigning:
        locals()[resultAssigned] = resultPrinted
        print(resultAssigned)
    else:
        print(resultPrinted)
    inputPrompt = input("-->")
