def solution(prices):
    length = len(prices)
    result = [ i for i in range (length - 1, -1, -1)]
    stack = [0]
    
    for i in range (1, length, 1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
        
    return result