def appmain():
    def CommandsMain():
        mylistchelp = ["--exit -app: This Command Let's You Exit The APP", "--calculator: This Command Opens You The Calculator", "--games -open: This Command Opens You The Games Launcher"]
        print("Welcome To CommandPlus APP")
        print("Type help To see All Commands Available")
        z = 0
        while z < 99999999999999999999999999999:
            z += 0.00000000000000001
            Nm = str(input("TypeCommand>> "))
            if Nm == "--calculator":
                Calculatoroprning()
                break
            elif Nm == "help":
                for x in mylistchelp:
                    print(x)
            elif Nm == "--exit -app":
                appmain(exit())
            elif Nm == "--games -open":
                SCW()
            else:
                print("This Command Is not Existed")
    def Calculatoroprning():
        print("Opening Calculator")
        print("After You see The Answer Type help To see All Commands Available")
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
            y = input("Type Command>> ")
            listhelp = ["--back: this command let's you go to the Func Before"]
            if y == "help":
                print(listhelp)
            elif y == "--back":
                CommandsMain()
                break
    def SCW():
        print("Open GamesLauncher")
        print("Type help To see All Commands Available")
        hh = 0
        listgames = ["1.GuessGame", "2.ComingSoon", "3.ComingSoon"]
        listhelp = ["--back: this command let's you go to the Func Before", "--games: This Command Show you All Games Available", "--open game (game num): This Command Let's you Open The Games Available"]
        while hh < 99999999999999999999999999999999999:
            hh += 0.000000000000001
            y = input("Type Command>> ")
            if y == "--games":
                for i in listgames:
                    print(i)

            elif y == "--back":
                CommandsMain()
                break
            elif y == "--open game (1)":
                GuessGame()
                break
            elif y == "help":
                for i in listhelp:
                    print(i)
            else:
                print("This Command Not Available")
    def GuessGame():
        print("Opening GuessGame")
        print("Type help To see All Commands Available")
        x = 0
        while x < 999999:
            x += 0.0000000001
            lishelp = ["--back: this command let's you go to the Func Before", "--ma: --ma is a command use it to return the main of app", "start -- 'Name Of the Game'"]
            yh = input(">>> ")
            if yh == "help":
                for c in lishelp:
                    print(c)
            elif yh == "--back":
                SCW()
                break
            elif yh == "--ma":
                CommandsMain()
                break
    CommandsMain()

appmain()