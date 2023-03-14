def appmain():
    def CommandsMain():
        mylistchelp = ["0.Exit", "1.Calculator", "2.Games", "3.ComingSoon"]
        print("Welcome To CommandPlus APP")
        print("Type help to see all commands available")
        z = 0
        while z < 99999999999999999999999999999:
            z += 0.00000000000000001
            Nm = str(input(">>> "))
            if Nm == "1":
                Calculatoroprning()
                break
            elif Nm == "help":
                for x in mylistchelp:
                    print(x)
            elif Nm == "0":
                appmain(exit())
            elif Nm == "2":
                SCW()
            else:
                print("This Command Is not Existed")
    def Calculatoroprning():
        print("Opening Calculator")
        x = 0
        while x < 999999999999999999999999999999:
            x += 0.00000000000000001
            num1 = float(input("Num: "))
            Symbols = (input(">>> "))
            num2 = float(input("Num: "))
            #CalculSyS
            if Symbols == "+":
                print(num1 + num2)
            elif Symbols == "-":
                print(num1 - num2)
            elif Symbols == "/":
                print(num1 / num2)
            elif Symbols == "*":
                print(num1 * num2)
            elif Symbols == "**":
                print(num1 ** num2)
            else:
                print("Invalid Operator")
                print(">>> " + Symbols)
                print("There is an Error in " + Symbols)
            y = input(">>> ")
            listhelp = ["0.Exit"]
            if y == "help":
                print(listhelp)
            elif y == "0":
                CommandsMain()
                break
    def SCW():
        print("Open GamesLauncher")
        hh = 0
        listhelp = ["1.GuessGame", "2.ComingSoon", "3.ComingSoon"]
        while hh < 99999999999999999999999999999999999:
            hh += 0.000000000000001
            y = input(">>> ")
            if y == "help":
                for i in listhelp:
                    print(i)

            elif y == "exit":
                CommandsMain()
                break
            elif y == "1":
                GuessGame()
                break
    def GuessGame():
        print("Opening GuessGame")
        x = 0
        while x < 999999:
            x += 0.0000000001
            lishelp = ["0.Exit", "1.MainApp"]
            yh = input(">>> ")
            if yh == "help":
                for c in lishelp:
                    print(c)
            elif yh == "0":
                SCW()
                break
            elif yh == "1":
                CommandsMain()
                break
    CommandsMain()

appmain()