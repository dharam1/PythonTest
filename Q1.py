#python 3
def validate(s):
    if (len(s) < 6 or len(s) > 12 ):
        print("Not Valid")
    else:
        small = capital = special = digit = 0
        for i in s:
            if(ord(i) in range(97,123)):
                small = 1
            if(ord(i) in range(65,91)):
                capital = 1
            if(i.isdigit()):
                digit = 1
            if(ord(i) == 36 or ord(i) == 35 or ord(i) == 64):
                special =1
        if(small == 1 and capital == 1 and digit == 1 and special == 1):
            print("Valid")
        else:
            print("Not Valid")
def main():
    s = input()
    validate(s)
if __name__== "__main__":
    main()
                