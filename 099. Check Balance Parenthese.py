'''
Problem: 

Input could include ":(" frown or ":)" smileys, check if the input is parenthese balance
'''

'''
Solution:

smileys 记录全部可能的smileys. 

smileys = smileys - (closeParenth - openParenth)  

closeParenth - openParenth: close 比 open 多的一定必须是 smileys(如果不是smileys, 那么 open 和 close 就不可能平衡了); 
那么"全部可能的smileys(smileys)" 减去 "一定必须是smiley的"，剩下的就是 "剩下的全部可能的smileys(新的smileys)"


closeParenth = openParenth 就是仍需要 match openParenth 的 closeParenth 的值。

'''

def checkBalanced(message):
    closeParenth = openParenth = 0
    smileys = frowns = 0
    emotion = False

    for char in message:
        if char == '(':
            if emotion:
                frowns += 1
            openParenth += 1
        elif char == ')':
            if emotion:
                smileys += 1
            closeParenth += 1

        if closeParenth > openParenth:
            if closeParenth - smileys > openParenth:
                return False
            smileys = smileys - (closeParenth - openParenth)    # smileys是: 用 ) match ( 了后剩下的来搭配 ) 做 :), 剩下的: 是新的 smileys
            closeParenth = openParenth

        if char == ':':
            emotion = True
        else:
            emotion = False

    if openParenth - frowns > closeParenth:
        return False

    return True


test = '((()):)'
print checkBalanced(test)
