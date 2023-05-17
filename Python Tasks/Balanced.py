def Check_Balanced(str="{}"):
    L_string = list(Strings)
    O_brakets = ['(','{','[']
    C_brakets = [')','}',']']
    x = (len(L_string))/2
    y = len(L_string)-1 
    List_String = True
    if (len(L_string))%2 == 0 :
        v = 0
        while v < x :  
            j = 0
            while j < 3 : 
            
                if L_string[v] == O_brakets[j] and L_string[y] == C_brakets[j]:
                    List_String == True
                    
                    
                else:
                    List_String == False
                
                j = j+1    
            
            v = v+1
            y =y-1
        if List_String == True:
            print("It's Balanced Brackets ")
        else:
            print ("It's Not_Balancd")
        
    else:
        print("It's Not Balanced")
 
Strings = input(" Enter Your Brakets please :- ")   

Check_Balanced(Strings)