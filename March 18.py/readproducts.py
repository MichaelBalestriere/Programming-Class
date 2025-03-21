def read_products(filename):
    products = []
    with open(filename, 'r') as file:
        for line in file:
            product_id,name,price = line.strip().split(',')
            products.append({
                'id': product_id,
                'name': name,
                'price': float(price)
            })
    return products

def display_products(products):
    print("Available products:")
    print("{:<10} {:<20} {:<10}".format('ProductID', 'ProductName', 'Price'))
    for product in products:
        print("{:<10} {:<20} {:<10}".format(product['id'], product['name'], product['price']))

def select_products(products):
    selected_products = []
    while True:
        product_id = input('Enter product id: ')
        if product_id.lower() == 'done':
            break
        try:
            quantity = int(input('Enter quantity: '))
        except ValueError:
            print('Invalid quantity')
            continue
        for product in products:
            if product['id'] == product_id:
                selected_products.append({
                    'product': product['id'],
                    'name': product['name'],
                    'price': product['price'],
                    'quantity': quantity
                })
                break
        else:
            print('Invalid product id')
    return selected_products

def calculate_total(selected_products):
    total = 0
    for product in selected_products:
        total += product['price'] * product['quantity']
    return total

def write_transaction(filename, selected_products, total):
    with open(filename, 'a') as file:
        for product in selected_products:
            file.write(f"{product['product']},{product['name']},{product['price']},{product['quantity']}\n")
        file.write(f"Total,{total}\n")
        
def main():
    products = read_products('products.txt')
    display_products(products)
    selected_products = select_products(products)
    total = calculate_total(selected_products)
    write_transaction('transactions.txt', selected_products, total)
    print('Total: ${:.2f}'.format(total))
    
if __name__ == '__main__':
    main()