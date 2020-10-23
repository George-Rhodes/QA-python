
def find_isbn(string_isbn):

    strip_isbn = string_isbn.replace('-','')
    digit13 = 0
    x = 0
    leng = len(strip_isbn)
    while x < leng:
        
        num = int(strip_isbn[x])
        if (x % 2) == 0:
            digit13 += num
                       
        else:
            
            digit13 += (num*3)
            
        
        x += 1
    digit = 10 - (digit13 % 10) 
    #print(strip_isbn)
    #print(len(strip_isbn))

    return digit






if __name__ == '__main__':
    string_isbn = str(input("please enter isbn: " ))
    lastdig = find_isbn(string_isbn)
    print(string_isbn + str(lastdig))

