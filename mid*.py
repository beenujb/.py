def replacelwith*(input, pattern, replaceWith): 
    return input.replace(pattern, replaceWith) 
  

if __name__ == "__main__": 
    input   = 'hello'
    pattern = 'l'
    replaceWith = '*'
    print replacelwith*(input,pattern,replaceWith) 
