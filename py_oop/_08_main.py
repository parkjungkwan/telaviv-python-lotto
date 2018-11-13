from _08_calc import Calc 
def main():
     calc = Calc(4, 2)
     print(calc.first)
     print(calc.second)
     print("{} + {} = {}".format(calc.first,
                                 calc.second,
                                 calc.sum()))
     print(calc.div())
     print("{} / {} = {}".format(calc.first,
                                 calc.second,
                                 calc.div()))
if __name__=='__main__':
    main()


