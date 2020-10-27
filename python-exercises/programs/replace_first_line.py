def readerreplace():
    new_line = 'this is a new line\n'
    file1 = open('programs/teams2.txt', 'r')
    Lines = file1.readlines()
    file1.close()
    Lines[0] = new_line
    file1 = open('programs/teams3.txt', 'w')

    file1.writelines(Lines)
    file1.close()
    print(Lines)


       
    

if __name__ == '__main__':

    readerreplace()