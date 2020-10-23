





def times_tabels():
    tables = []                                                            
    for i in range (1, 11):                               
        new = []                        
        for j in range (1, 11):            
            new.append(i*j)              
        tables.append(new)

    return tables















if __name__ == '__main__':

    print(times_tabels())
