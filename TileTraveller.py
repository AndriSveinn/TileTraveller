# https://github.com/AndriSveinn/TileTraveller

#1.implematation 2 var miklu erfiðari hefði ég byrjað á því, en af því ég er búinn með nr1
#2.implematation 2 var miklu auðlesanlegri kerfið var um 10 línur 109
#3. Miklu auðveldara skrifaði bara yfirfall sem vikar á allt en i fyrri þurfti 
#  ég alltaf að skrifa línur sem hentaði hverjum reit fyrir sig

#                           SAUÐKÓÐUI
# Staðsetning = [1,1]
# norður='(N)orth' 
# suður='(S)outh'
# austur='(E)ast'
# vestur='(W)est'

# while Staðsetning != [3,1]:
#     if Staðsetning == [1,1]:
#         print('You can travel: ' + norður + '.')
#         færsla=input('Direction: ')
#         færsla=færsla.lower()
#         while færsla != 'n':
#             print('Not a valid direction!')
#             færsla=input('Direction: ')
#             færsla=færsla.lower()
#         Staðsetning[1] += 1

#     elif Staðsetning == [1,2]:
#         print('You can travel: ' + norður + ' or ' + austur + ' or ' + suður + '.')
#         færsla=input('Direction: ')
#         færsla=færsla.lower()
#         while færsla != 'n' and færsla != 's' and færsla != 'e':
#             print('Not a valid direction!')
#             færsla=input('Direction: ')
#             færsla=færsla.lower()
#         if færsla =='n':
#             Staðsetning[1] += 1
#         elif færsla =='s':
#             Staðsetning[1] -= 1
#         elif færsla =='e':
#             Staðsetning[0] += 1

#     elif Staðsetning == [1,3]:
#         print('You can travel: ' + austur + ' or ' +suður + '.')
#         færsla=input('Direction: ')
#         færsla=færsla.lower()
#         while færsla != 's' and færsla != 'e':
#             print('Not a valid direction!')
#             færsla=input('Direction: ')
#             færsla=færsla.lower()
#         if færsla =='s':
#             Staðsetning[1] -= 1
#         elif færsla =='e':
#             Staðsetning[0] += 1

#     elif Staðsetning == [2,1]:
#         print('You can travel: ' + norður + '.')
#         færsla=input('Direction: ')
#         færsla=færsla.lower()
#         while færsla != 'n':
#             print('Not a valid direction!')
#             færsla=input('Direction: ')
#             færsla=færsla.lower()
#         Staðsetning[1] += 1

#     elif Staðsetning == [2,2]:
#         print('You can travel: ' + suður + ' or ' + vestur + '.')
#         færsla=input('Direction: ')
#         færsla=færsla.lower()
#         while færsla != 's' and færsla != 'w':
#             print('Not a valid direction!')
#             færsla=input('Direction: ')
#             færsla=færsla.lower()
#         if færsla =='w':
#             Staðsetning[0] -= 1
#         elif færsla =='s':
#             Staðsetning[1] -= 1

#     elif Staðsetning == [2,3]:
#         print('You can travel: ' + austur + ' or ' + vestur + '.')
#         færsla=input('Direction: ')
#         færsla=færsla.lower()
#         while færsla != 'w' and færsla != 'e':
#             print('Not a valid direction!')
#             færsla=input('Direction: ')
#             færsla=færsla.lower()
#         if færsla =='w':
#             Staðsetning[0] -= 1
#         elif færsla =='e':
#             Staðsetning[0] += 1

#     elif Staðsetning == [3,3]:
#         print('You can travel: ' + suður + ' or ' + vestur + '.')
#         færsla=input('Direction: ')
#         færsla=færsla.lower()
#         while færsla != 'w' and færsla != 's':
#             print('Not a valid direction!')
#             færsla=input('Direction: ')
#             færsla=færsla.lower()
#         if færsla =='w':
#             Staðsetning[0] -= 1
#         elif færsla =='s':
#             Staðsetning[1] -= 1

#     elif Staðsetning == [3,2]:
#         print('You can travel: ' + norður + ' or ' + suður + '.')
#         færsla=input('Direction: ')
#         færsla=færsla.lower()
#         while færsla != 'n' and færsla != 's':
#             print('Not a valid direction!')
#             færsla=input('Direction: ')
#             færsla=færsla.lower()
#         if færsla =='n':
#             Staðsetning[1] += 1
#         elif færsla =='s':
#             Staðsetning[1] -= 1
    
# else:
#     print('Victory!')


def has_won(Staðsetning):
    if Staðsetning == [3,1]:
        return True
    else:
        return False

def move(Staðsetning,færsla):
    if færsla=='n':
        Staðsetning[1] += 1
    elif færsla=='s':
        Staðsetning[1] -= 1
    elif færsla=='e':
        Staðsetning[0] += 1
    elif færsla=='w':
        Staðsetning[0] -= 1  
    return Staðsetning 

def instructions(Staðsetning):
    norður='(N)orth' 
    suður='(S)outh'
    austur='(E)ast'
    vestur='(W)est'
    if Staðsetning == [1,1]:
        print('You can travel: ' + norður + '.')
    elif Staðsetning == [1,2]:
        print('You can travel: ' + norður + ' or ' + austur + ' or ' + suður + '.')
    elif Staðsetning == [1,3]:
        print('You can travel: ' + austur + ' or ' +suður + '.')
    elif Staðsetning == [2,1]:
        print('You can travel: ' + norður + '.')
    elif Staðsetning == [2,2]:
        print('You can travel: ' + suður + ' or ' + vestur + '.')    
    elif Staðsetning == [2,3]:
        print('You can travel: ' + austur + ' or ' + vestur + '.')
    elif Staðsetning == [3,3]:
        print('You can travel: ' + suður + ' or ' + vestur + '.')
    elif Staðsetning == [3,2]:
        print('You can travel: ' + norður + ' or ' + suður + '.')

def get_input():
    return input('Direction: ')

def is_valid(færsla,Staðsetning):
    if Staðsetning == [1,1]:
        if færsla =='n':
            return True
        else:
            return False
    elif Staðsetning == [1,2]:
        if færsla =='n' or færsla == 'e' or færsla=='s':
            return True
        else:
            return False
    elif Staðsetning == [1,3]:
        if færsla =='e' or færsla=='s':
            return True
        else:
            return False
    elif Staðsetning == [2,1]:
        if færsla =='n':
            return True
        else:
            return False
    elif Staðsetning == [2,2]:
        if færsla =='s' or færsla == 'w':
            return True
        else:
            return False    
    elif Staðsetning == [2,3]:
        if færsla =='e' or færsla == 'w':
            return True
        else:
            return False
    elif Staðsetning == [3,3]:
        if færsla =='s' or færsla == 'w':
            return True
        else:
            return False
    elif Staðsetning == [3,2]:
        if færsla =='n' or færsla=='s' :
            return True
        else:
            return False        

#Forritið er völundarhús, þar sem notandinn er á byrjunarreit og reynir að komast á lokareit
Staðsetning = [1,1]

while not has_won(Staðsetning):
    instructions(Staðsetning)
    færsla=get_input().lower()
    while not is_valid(færsla,Staðsetning):
        print('Not a valid direction!')
        færsla=get_input().lower()
    Staðsetning = move(Staðsetning,færsla)
print('Victory!')



