
def calculate (grade1, grade2, grade3):
    grade = float((grade1+grade2+grade3)/3)
    print("you scored :" + str(grade) )
    if grade >= 70:
        print("you got an A")
        return
    elif grade >= 60:
        print("you got an B")
        return
    elif grade >= 50:
        print("you got an C")
        return
    elif grade >= 40:
        print("you got an D")
        return
    else:
        print("you fail")
        return

if __name__ == '__main__':
    maths_mark = int(input("input your matsh grade" ))
    chem_mark =  int(input("inpit chem mark"))
    phy_mark = int(input("inpt physics mark"))

    calculate(chem_mark, maths_mark, phy_mark)

    