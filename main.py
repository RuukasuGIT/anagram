words = ["Xyz","Abc","Aba","Test"]

def solve():
  x = input("\n  Input Anagram:\n    >>> ")
  for i in range(len(words)):
            if sorted(words[i]) == sorted(x):
                print("\n ",x,"is an anagram of",words[i])
                input("  Press Enter To Continue")
                init()
        print("\n ",x,"is not an anagram of any registered word.")
        input("  Press Enter To Continue")
       
solve()
