import csv
'''
load items from item.txt
'''
def load_items(filename):
    items = []
    f= open(filename,'r+')
    for line in f.readlines():
        name,price,priority = line.split(',')
        items.append([name,eval(price),eval(priority),1,0])#[name,price,priority,isrequired,isCompleted]
    items = sorted(items,key = lambda s:s[2])#sort item by priority
    print('{} items loaded from items.csv'.format(len(items)))
    return items
'''
save items to item.txt
'''
def save_items(filename,items):
    f= open(filename,'w+')
    i=0
    for item in items:
        s = item[0]+','+str(item[1])+','+str(item[2])+'\n'
        f.write(s)
        i+=1
    f.close()
    print('{} items saved to {}'.format(i,filename))
    print('Have a nice day :)')
'''
make the specified item completed
'''
def complete_an_item(items,number):
    '''
    parameter:
    number:int ,which item to complete
    '''
    i=0
    j=0
    for item in items:
        if item[-2] ==1:#required item
            i+=1
        if i-1 == number: #find the item to complete
            items[j][-1] = 1#change required flag
            items[j][-2] = 0#change completed flag
            print('{} marked as completed'.format(items[j][0]))
            break
        j+=1
    return items
'''
add an item to list-items
'''
def add_item(items):
    while(True):
        name = input('Item name: ')
        if name.strip() == '':#blank spaces
            print('Input can not be blank')
        else:
            break
    while(True):
        price = input('Price: $ ')
        try:
            price = float(price)# except not a number
        except Exception as e:
            print('Invalid input; enter a valid number')
            continue
        if price <=0 :#smaller than 0
            print('Price must be >= $0')
        else:
            break
    while(True):
        priority = input('Priority: ')
        try:
            priority = int(priority)#except not a number
        except Exception as e:
            print('Invalid input; enter a valid number')
            continue
        if priority not in [1,2,3]:#priority  is not 1,2,or 3
            print('Priority must be 1, 2 or 3')
        else:
            break
    items.append([name,price,priority,1,0])
    items = sorted(items,key = lambda s:s[2])
    print('{}, ${} (priority {}) added to shopping list'.format(name,price,priority))
    return items
'''
print menu
'''
def menu():
    print('Menu:')
    print('R - List required items')
    print('C - List completed items')
    print('A - Add new item')
    print('M - Mark an item as completed')
    print('Q - Quit')
    
    
'''
list items
list required items if field is 3
list completed items if field is 4
list items that can be marked completed if field is 3 and choose is 'm'
'''
def list_items(items,field,choose):
    '''
    parameters:
    items : list
    field: int ,3 or 4
    choose: char
    '''
    i=0
    sumall = 0#sum price
    has = False
    for item in items:
        if item[field] ==1:#flag is 1 ,list it
            if has ==False:
                if field == 3 and choose == 'R':
                    print('Required items: ')
                elif field == 4:
                    print('Completed items: ')
                else:
                    pass
                has = True
            print('{:<2}. {:<15}  $  {:<10} ({:<1})'.format(i,item[0],item[1],item[2]))
            sumall += item[1]
            i+=1
    if i == 0:#no items satisfied conditions
        if field == 3:
            print('No required items')
        else:
            print('No completed items')
        return i
    else:
        print('Total expected price for {} items: ${}'.format(i,sumall))
        return i
 
def main():
    print('Shopping List 1.0 - by Lindsay Ward')
    filename = 'item.txt'
    items = load_items(filename)
    while(True):
        menu()
        choose = input()
        if choose.upper() == 'R':#list required items
            num = list_items(items,3,choose.upper())
        elif choose.upper() == 'C':#list completed items
            list_items(items,4,choose.upper())
        elif choose.upper() == 'M':#mark one item completed
            num = list_items(items,3,choose.upper())
            if num>0:
                print('Enter the number of an item to mark as completed')
                while(True):
                    number = raw_input()
                    try:
                        number = int(number)
                    except Exception as e:
                        print('Invalid input; enter a number')
                        continue
                    
                    if number<0 or number >= num:
                        print('Invalid item number')
                    else:
                        items = complete_an_item(items,number)
                        break
            
        elif choose.upper() == 'A':#add
            items = add_item(items)
        elif choose.upper() == 'Q':#quit and save
            save_items(filename,items)
            break
        else:
            print('Invalid menu choice')#invalid choose
main()
    
    

