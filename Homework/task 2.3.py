numbers = {0:'Zero', 
           1:'One', 
           2:'Two', 
           3:'Three', 
           4:'Four', 
           5:'Five', 
           6:'Six', 
           7:'Seven', 
           8:'Eight', 
           9:'Nine'}
a = int(input('Введите цифру: '))
def switch_it_up(number):

    number = numbers.get(a, None)
    print ('switch_it_up {a} -> ' + str(number))
switch_it_up(a)

