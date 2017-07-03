'''
Problem: 

Input could include ":(" frown or ":)" smileys, check if the input is parenthese balance
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
            smileys = smileys - (closeParenth-openParenth)
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
