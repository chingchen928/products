products = []
while True:
	name = input('Products:')
	if name == 'q':
		break
	price = input('Price:')
	products.append([name, price])
print(products)

for p in products:
	print(p[0] + '的價格是' + p[1])

with open('products.csv', 'w', encoding= 'utf-8') as f:
	f.write('Products,Price' + '\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')