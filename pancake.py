import sys 
def pancake_pie(syrup):
    letters = "abcdefghijklmnopqrstuvwxyz"
    oga_input = input("What you want on your pancake? ")
    reality = ""
    final = ""
    sir = ""
    for flap in oga_input:
        if flap.lower() in letters:
            reality += flap.upper()
    for s in reality:
        if (ord(s) + syrup) > 90:
            final += chr(ord(s) - (26 - syrup))
        else:
            final += chr(ord(s) + syrup)
    locate = 5
    timing = 0
    for i in range(0, len(final), 5):
        sir += final[i:locate]
        sir += " "
        locate += 5
        timing += 1
        if (timing % 10) == 0:
            sir += "\n"
    return sir

waf = int(sys.argv[1])
print(pancake_pie(waf))
