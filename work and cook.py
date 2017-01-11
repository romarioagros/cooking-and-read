
cook_book={}
count=-100000000 #надеюсь что столько строк не будет, но при желании число можно сделать очень большим (100**1000)"
c=0
temple_list=["product",'quantity',"unit"]
with open('recepies.txt', encoding='cp1251') as document:
    
    for line in document :
        c=c+1
        if c==1:
            print (line)
            causine=line.rstrip('\n')
            cook_book[causine]={'name':causine,"type":"х.з","ingridients":[]}
            
        if c==2:
            count=int(line)
            #print("это каунт",count)
        if c>2 and  c<(3+count):
            items=list(map(str.rstrip,line.split(" | ")))
            items[1]=int(items[1])
            new_dict=dict(list(zip(temple_list,items)))
            cook_book[causine]["ingridients"].append(new_dict)
            #print (new_dict)
        if c==(2+count):
            c=-1
            


def get_shop_list_by_dishes(dishes, people_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in dish['ingridients']:
            new_shop_item = dict(ingridient)
            # пересчитали ингрединты по количеству людей
            new_shop_item['quantity'] = new_shop_item['quantity'] * people_count
            if new_shop_item['product'] not in shop_list:
                shop_list[new_shop_item['product']] = new_shop_item
            else:
                shop_list[new_shop_item['product']]['quantity'] += new_shop_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for key, shop_list_item in shop_list.items():
        print("{product} {quantity} {unit}".format(**shop_list_item))

def create_shop_list(people_count, first_dish, second_dish, third_dish):
    # получить блюда из кулинарной книги
    dish1 = cook_book[first_dish]
    dish2 = cook_book[second_dish]
    dish3 = cook_book[third_dish]
    dishes = [dish1, dish2, dish3]
    #заполнили список покупок
    shop_list = get_shop_list_by_dishes(dishes, people_count)
    # ¬ывести список покупок
    print_shop_list(shop_list)

print('¬ыберите первое блюдо: ')
first_dish = input()
print('¬ыберите второе блюдо: ')
second_dish = input()
print('¬ыберите третье блюдо: ')
third_dish = input()
print('Ќа сколько человек?')
people_count = int(input())

print('—писок покупок: ')
create_shop_list(people_count, first_dish, second_dish, third_dish)
