products = []
while True:
	name = input('Products:')
	if name == 'q':
		break
	price = input('Price:')
	products.append([name, price])
print(products)
