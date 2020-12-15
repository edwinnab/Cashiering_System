#declare the class and methods
class CahieringSystem:
    def __init__(self, a = 0, r = 0, recieve = 0, change = 0, temp = 0):
        print("\n\n*******WELCOME TO MY RESTRAUNT*******\n")
        self.a = a
        self.r = r
        self.recieve = recieve
        self.change = change
        self.temp = temp
        #ordering method
    def foods(self):
        print("*****RESTRAUNT MENU******")
        print("1.Fries-----------> 50", "\n2.Sausages-----------> 30", "\n3.Smokies-----------> 40", "\n4.Cebab-----------> 50", "\n5.CashOut", "\n6.Exit")
        while(1):
            c = int(input("Choose: \n"))
            if (c == 1):
                d = int(input("Enter the quantity: \n"))
                self.r = self.r + 50 * d
            elif (c == 2):
                d = int(input("Enter the quantity: \n"))
                self.r = self.r + 30 * d
            elif (c == 3):
                d = int(input("Enter the quantity: \n"))
                self.r = self.r + 40 * d
            elif (c == 4):
                d = int(input("Enter the quantity: \n"))
                self.r = self.r + 50 * d
            elif (c == 5):
                print("Total: ", self.r)
                if (self.r > 0):
                    recieve = int(input("Input Money Received: \n"))
                    print("Your Change is: ", recieve - self.r)
                    print("***Thank You Come Again******")
            elif (c == 6):
                quit()
            else:
                print("Invalid Option")
def main():
    a = CahieringSystem()
    while(1):
        a.foods()
main()



