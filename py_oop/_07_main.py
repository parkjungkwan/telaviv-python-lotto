# ************
# -- Main
# ************
from _07_animal import Cat 
from _07_animal import Dog 
def main():
    dog = Dog(True)
    dog.name = "어미개"
    dog.eat("피자")
    dog.poop()
    print (dog.__dict__)
    bill = Cat("검은고양이", "흰검")
    print (bill.__dict__)
if __name__ == "__main__": # main
    main()