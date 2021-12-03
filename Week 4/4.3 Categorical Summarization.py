numberList=[]
while True:
    nmbr = input('Please enter a number (or if done, please enter Done): ')
    if nmbr == 'Done' or nmbr=='done':
        break
    else:
        try:
            nmbr=float(nmbr)
            numberList.append(nmbr)
        except:
            print('Please enter a numeric value or Done')
print(
    'The sum of numbers entered is: ', sum(numberList),
    '\nThe total number of entries is: ', len(numberList),
    '\nThe average of the numbers entered is: ', sum(numberList)/len(numberList)
)