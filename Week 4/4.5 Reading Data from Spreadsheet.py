# %%
import csv
import numpy as np
infile = 'price_of_gasoline.xl.csv'
#create new empty lists: years and prices that come from the day
yearsList = []
priceList =[]

#Create name of months list for reporting
monthList = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# read the data
with open(infile, 'rU') as csvfile:
    #the csv file reader returns a list of csv items
    priceRead = csv.reader(csvfile, dialect='excel', delimiter=',')
    for line in priceRead:
        if line[0]=='' or line[0].startswith('Price') or line[0].startswith('Year'):
            continue
        else:
            try:
                yearsList.append(line[0])
                priceList.append(line[1:])
            except IndexError:
                print('Error: ', line)
csvfile.close
print("Read", len(yearsList), "years of prices")
data = np.array(priceList)
print('Shape of prices data', data.shape)
#converts empty data to zero
data[data=='']='0'
prices = data.astype(np.float)

print(prices)
monthTotalPrices = np.sum(prices, axis = 0)
monthAveragePrices = monthTotalPrices/len(yearsList)

print("\nAverage gas price for each month\n")

#print the average price for each month
for i, mon in enumerate(monthList):
    print(mon, ':', monthAveragePrices[i])

#Or display the monthl average as a simple plot
import matplotlib.pyplot as pp

x = np.arange(12)
pp.xticks(x, monthList)
pp.plot(x, monthAveragePrices)
pp.show()

# or we can also display the years with a simple plot
x = np.arange(len(yearsList)-1)
pp.xticks(x, yearsList)
pp.plot(x, yearAveragePrices)
pp.show()
# %%
