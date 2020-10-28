
class student:

    
    
    def __init__(self, Sname, Sage):

        self.Sname = Sname
        self.Sage = Sage
        self.group = 'Student'
    


    def setClass(self,group):
        self.group = group
    
    def average_test_score(self, score1, score2, score3):

        average = (score1 + score2 + score3) / 3

        return average

    












if __name__ == '__main__':



    jeff = student('jeff wiggigns', 28 )

    print(jeff.average_test_score(29 , 39 ,89))
