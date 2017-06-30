# Problem 1: Remove comments JAVA


# Note: "singleLine or multiLine:" can never be the first, oterwise "singleLine" "multiLine" can never be set to False

def removeComment(code):
    singleLine = False
    multiLine = False
    result = []
    i = 0
    while i < len(code):
        
        if singleLine and code[i] == '\n':
            singleLine = False

        elif multiLine and code[i] == '*' and code[i+1] == '/':
            multiLine = False
            i += 1

        elif singleLine or multiLine:
            i += 1
            continue

        elif code[i] == '/' and code[i+1] == '/':
            singleLine = True
            i += 1

        elif code[i] == '/' and code[i+1] == '*':
            multiLine = True
            i += 1

        else:
            result.append(code[i])

        i += 1
    
    return ''.join(result)


test = '/*comment1 \n comment2\n comment3 */ int a = 1;'
print removeComment(test)






# Problem 2: Remove comments Python

def removeComment(code):
    singleLine = False
    multiLine = False
    result = []
    i = 0
    while i < len(code):

        if singleLine and code[i] == '\n':
            singleLine = False

        elif multiLine and (code[i] == '\'' or code[i] == '\"') and (code[i+1] == '\'' or code[i+1] == '\"') and (code[i+2] == '\'' or code[i+2] == '\"'):
            multiLine = False
            i += 2

        elif singleLine or multiLine:
            i += 1
            continue

        elif code[i] == '#':
            singleLine = True

        elif (code[i] == '\'' or code[i] == '\"') and (code[i+1] == '\'' or code[i+1] == '\"') and (code[i+2] == '\'' or code[i+2] == '\"'):
            multiLine = True
            i += 2

        else:
            result.append(code[i])

        i += 1
    
    return ''.join(result)


test = '\'\'\'comment1 \n comment2\n comment3 \'\'\' a = 1'
test = '#comment\n a = 2'
print removeComment(test)
