Staðsetning = [1,1]
norður='(N)orth' 
suður='(S)outh'
austur='(W)est'
vestur='(E)ast'


while Staðsetning != [3,1]:
    if Staðsetning = [1,1]:
        print('You can travel:' + norður + '.')
        færsla=input('Direction:')
        færsla=færsla.lower()
        while færlsa != 'n':
            print('Not a valid direction')
            færsla=input('Direction:')
            færsla=færsla.lower()
        Staðsetning[1] = 1+1
    elif Staðsetning = [1,2]:
        print('You can travel:' + norður + 'or' + austur + 'or' +suður + '.')
        færsla=input('Direction:')
        færsla=færsla.lower()
        while færlsa != 'n' or færsla != 's' or færsla != 'e'):
            print('Not a valid direction')
            færsla=input('Direction:')
            færsla=færsla.lower()
        if færsla =='n':
            Staðsetning[1] += 1
        elif færsla =='s':
            Staðsetning[1] -= 1
        elif færsla =='e':
            Staðsetning[0] += 1
elif Staðsetning = [1,3]:
        print('You can travel:' + norður + 'or' + austur + 'or' +suður + '.')
        færsla=input('Direction:')
        færsla=færsla.lower()
        while færlsa != 'n' or færsla != 's' or færsla != 'e'):
            print('Not a valid direction')
            færsla=input('Direction:')
            færsla=færsla.lower()
        if færsla =='n':
            Staðsetning[1] += 1
        elif færsla =='s':
            Staðsetning[1] -= 1
        elif færsla =='e':
            Staðsetning[0] += 1

