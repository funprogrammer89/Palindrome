def test():
    while 1 < 2:
        print("Enter a String to test?")
        String = input()
        yes = True

        for i in range(int(len(String) / 2)):
            if String[i] == String[len(String) - 1 - i]:
                yes = True
            else:
                yes = False
                break
        if yes:
            print("yup")
        else:
            print("nope")

            
if __name__ == '__main__':
    test()