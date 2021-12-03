#Exercise 1
mp = 'Today is a Great DAY'
mp.lower()
mp.upper()
mp.strip()
mp.startswith('i')
mp.find('G')

#Exercise 2
tring = 'X-DSPAM-Confidenc:0.8475'
number = float(tring[tring.find('0'):])
format(number, '.2')
round(number, 2)

#youtube sample
print(dir(sys))

import timeit
list_test = timeit.timeit(stmt = "[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt = "(1,2,3,4,5)", number=1000000)
print('List time:' , list_test)
print('Tuple time:', tuple_test)
#Exercise 3

ostens = ["Merl","Willie","Elden","Carol", "Linda","Lee","Liela","Lola","Loretta","LaRae","Terry","Leta"]
ostenT = ("Merl","Willie","Elden","Carol", "Linda","Lee","Liela","Lola","Loretta","LaRae","Terry","Leta")
print('List Length: ', len(ostens))
print("Tuple Length:", len(ostenT))
