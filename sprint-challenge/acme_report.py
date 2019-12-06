from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    for num in range(0, num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price_weight = random.randint(5, 100)
        flam = random.uniform(0.0, 2.5)
        p = Product(name, price_weight, price_weight, flam)
        products.append(p)
    return products


def inventory_report(products):
    pricetot=0
    weighttot=0
    flamtot=0
    name_list = []
    for x in range(0,len(products)):
        pricetot = pricetot + products[x].price
        weighttot = weighttot + products[x].weight
        flamtot = flamtot + products[x].flammability
        if products[x].name not in name_list:
            name_list.append(products[x].name)
        else:
            pass
    unique = len(name_list)
    pricemean = pricetot / len(products)
    weightmean = weighttot / len(products)
    flammean = flamtot / len(products)
    print(f'ACME CORPORATION OFFICIAL INVENTORY REPORT\nUnique Product Names: {unique}\nAverage Price: {pricemean}\nAverage Weight: {weightmean}\nAverage Flammability: {flammean}')

if __name__ == '__main__':
    inventory_report(generate_products)
