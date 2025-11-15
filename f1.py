'''
 create function that has arbitary arguments of string type and it display all strings into lower case.
toLowerCase('Apple','bAnana','ManGO','KIWI','graps')
output 
    apple banana mango kiwi graps

'''
def to_lowercase(*list1):            #function
    for word in list1:
        print(word.lower(),end=' ')         #call_lower for all list in lowercase 
        
    

list1=to_lowercase('Apple','bAnana','ManGO','KIWI','graps')
print(list1)
