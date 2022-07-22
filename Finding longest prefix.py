
def prefixChecker(words):
    if len(words) == 0:#if the list of strings is empty return Null
        return None
    if len(words) == 1:
        return words[0]#if there is only one word in the list return that word
    
    pref = words[0]#initialize the prefix to the first word
    plen = len(words[0])#initialize the prefix lentgh to the length of the first word
    
    for word in words[1:]:#iterate through the list of words starting from the second word
        
        while pref != word[0:plen]:#while prefix is not contained in the word execute while body
            pref = pref[0:(plen-1)]#Remove las letter of the prefix
            plen -= 1#decrease the length of the prefix by one
            
            if plen == 0:#if the length of the prefix is zero execute if body
                return None
    
    return pref
    
_input = ["flower","flow","flight","fling","flinch"]
sec_input = ["try","trick","out","in"]


result = prefixChecker(sec_input) 

print(result)            
    

