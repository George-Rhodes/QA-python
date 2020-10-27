def readerfor_1_4():
    with open("programs/teams.txt", 'r') as file:
        listy = []
        for i in range(1, 6):
            if i == 1 or i == 4:                
                listy.append(file.readline())
            else:
                file.readline()
            
            
        print(listy)




if __name__ == '__main__':

    readerfor_1_4()