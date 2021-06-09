menu=['coffee','juice','pizza','tea']
price =[100,300,400]
food =dict(zip(menu,price))
choice=input('What do you want?')
price=food.get(choice,'Not available')
print(f'{choice}-{price}')