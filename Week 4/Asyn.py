# %%
def computerpay(hours, rate):
    if hours > 40:
       pay = ((hours-40)*rate*1.5)+(40*rate)
    elif hours <=40:
        pay = (hours*rate)
    return print('Pay: {:.2f}'.format(pay))
computerpay(45, 20)
# %%
computerpay(60,122)
# %%
