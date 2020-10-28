
import pdb


def best_conjugation(word2):
    find1 = word2
    lines = []
    words = []
    number =0
    with open("wordlist.txt", 'r') as file:
        lines = file.readlines()
        # 
    #print(lines)      
    for line in lines:
        number +=1        
        nl = line.replace('\n', '')
        #print(nl)
        if nl in word2:
             words.append(nl)
                
    return words




if __name__ == "__main__":


    jeff = 'awesomeness'
    
    print(best_conjugation(jeff))


