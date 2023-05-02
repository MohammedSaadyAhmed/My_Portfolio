def Mutation_fun(string, position, char):
#change string to a list
    L_string = list(string)
#change desired character
    L_string[position] = char
#back to string
    string = ''.join(L_string)
    print (string)

Mutation_fun('abracadabra', 4, 'k')