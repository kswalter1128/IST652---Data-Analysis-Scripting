#%%
# Consider the following 2 dictionaries
stock ={"banana":6, "apple":0, "orange":32, "pear":15}
prices = {"banana":4, "apple":2, "orange":1.5, "pear":3}
# %%
# A - Show the expression that gets the value of the stock dictionary at key 'orange'.
stock['orange']
# %%
# Show a statement that adds an item to the stock dictionary called 'cherry' with some interger value and that adds 'cherry' to the prices dictionary witha  numeric value.
stock['cherry']=45
prices['cherry']=1.25
# %%
# b Write the code for a loop that iterates over the stock dictionary and prints each key and value
for key, value in stock.items():
    print(key, value)
# %%
# C suppose we have a list
groceries = ['apple','banana','pear']
#write a code that will sum the total stock of items in the groceries list.
stockAmt =[]
for item in groceries:
    stockAmt.append(stock[item])
print('The total stock for groceries is: ',sum(stockAmt))
# %%
#D  Write the code that can print out the total value in stock of all the items. This program can iterate over the stock dictionary and for each item multiply the number in stock times the price of that item in the prices dictionary.
stockValue=[]
for key in sorted(stock):
    stockValue.append(prices[key]*stock[key])
print('The total value of stock is: ', sum(stockValue))
# %%
