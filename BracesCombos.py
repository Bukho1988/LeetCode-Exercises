_input = "()"

def bracesChecker(braces):

    replace = True
    
    while replace:#while replace is true
        start_length = len(braces)#set start_lentgh to the lentgh of the input
        for inner in ['[]','()','{}']:#loop throug the valid braces options to see if they ecxist in the input
            braces = braces.replace(inner,"")#remove any valid braces combination from the input and replace it with notyhing
        if start_length == len(braces):# check if the length of the string has changed 
            replace = False#if the length of the string has not changed that means no valid braces cmbo was found thus break out of the while loop
            
    return braces == ""#return a boolean value of weather the input string is empty or not. If the string is not empty
#that means there invalid braces combos in the string and thus return false.

def fasterBracesChecker(braces):
    
    close_map = {'(':')','[':']','{':'}'}#create a dictionary mapping each open braces to its correct closing braces
    opens = []#initialize empty lis
    
    for brace in braces:#loop trhrough the input
        if brace in close_map.keys():#check that the relevent charecter is present as one of the keys in close_map dict
            opens.append(brace)#if the relevent charecter i present as a key in the close_map dict append to the opens list
        elif opens == [] or brace != close_map[opens.pop()]:#check if the opens list is empty. if the list is empty that means one could not find open braces in the close_map key list.
        #if the list is not empty but the relevent brace was not for in the close_map key list, remove the last charecter you inserted into the opens list and check that it matche sthe cuurent
        #brace as a combo. if it does not excute the expression
            return False
        
    return opens == []

x = bracesChecker(_input)
y = fasterBracesChecker(_input)

print(y)
            
