menu_list = ['tea', 'coffee', 'sandwich', 'panini']

stock_dict = {'tea' : 5,
              'coffee' : 10, 
              'sandwich' : 8, 
              'panini' : 7} 

price_dict = {'tea' : 0.99, 
              'coffee' : 1.99, 
              'sandwich' : 4.99, 
              'panini' : 5.99} 

total_all_items_value=0 
for item in menu_list:
    total_value = price_dict[item] * stock_dict[item]
    total_all_items_value += total_value 
    print(f"\n{item.capitalize()} value: £{total_value:.2f}")
 

print(f"\nTotal value of all stock: £{total_all_items_value}") 

