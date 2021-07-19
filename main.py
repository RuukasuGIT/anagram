import os
words = ["Xyz","Abc","Aba","Test"]

def init():
    os.system("cls")
    mode = str(input("\n  Do you want your anagram to be capital sensitive? (Y/N)\n    >>> "))
    if mode.lower() == "y":
        solve(mode)
    elif mode.lower() == "n":
        solve(mode)
    else:
        init()

def solve(mode):
    if mode == "y":
        x = input("\n  Input Anagram:\n    >>> ")
        for i in range(len(words)):
            if sorted(words[i]) == sorted(x):
                print("\n ",x,"is an anagram of",words[i])
                input("  Press Enter To Continue")
                init()
        print("\n ",x,"is not an anagram of any registered word.")
        input("  Press Enter To Continue")
        init()
    else:
        x = input("\n  Input Anagram:\n    >>> ")
        for i in range(len(words)):
            if sorted(words[i].lower()) == sorted(x.lower()):
                print("\n ",x,"is an anagram of",words[i])
                input("  Press Enter To Continue")
                init()
        print("\n ",x,"is not an anagram of any registered word.")
        input("  Press Enter To Continue")
        init()

init()
