def minChar(n,pswd):
    lower=0
    upper=0
    special=0
    digit=0
    arr= ['!','@','#','$','%']
    for i in pswd:

        if(i.islower()):
            lower += 1
        if(i.isupper()):
            upper += 1
        if(i.isdigit()):
            digit += 1
        ex = i in arr
        if(ex):
            special += 1
    print('password contains')
    print('Special character', special)
    print('Digits',  digit)
    print('Upper character' , upper)
    print('Lower character' , lower)
    if(n<8):
        return str((8-n)) + 'more character to be added'
    else:
        return 'Strong Passowrd, good to go! '

n = int(input())
pswd = input()
print(minChar(n,pswd))