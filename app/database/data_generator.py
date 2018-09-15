from random import randint, random

RECEIPT_SIZE = 300


def generate_week():
    return randint(0, 37)


def get_user_id():
    return randint(1, 10)


def generate_gwp():
    return f'{random() * 20:.2f}'


def generate_price():
    return randint(0, 20)


def get_food_name():
    food = ['Tomaten', 'Oliven', 'Reisgetränk', 'Schnitzel', 'Protein-Stick', 'Bio Avocado']
    return food[randint(0, len(food)-1)]


def get_receipt_id():
    return randint(1, RECEIPT_SIZE)


if __name__ == '__main__':
    print('''
INSERT INTO users (username, password) VALUES ('admin', 'admin');
INSERT INTO users (username, password) VALUES ('emanuele', 'pw');
INSERT INTO users (username, password) VALUES ('arik', 'pw');
INSERT INTO users (username, password) VALUES ('luca', 'pw');
INSERT INTO users (username, password) VALUES ('bedri', 'pw');
INSERT INTO users (username, password) VALUES ('peter', 'pw');
INSERT INTO users (username, password) VALUES ('david', 'pw');
INSERT INTO users (username, password) VALUES ('dani', 'pw');
INSERT INTO users (username, password) VALUES ('savino', 'pw');
INSERT INTO users (username, password) VALUES ('markus', 'pw');
    ''')
    # receipts
    for i in range(RECEIPT_SIZE+1):
        print(f'''INSERT INTO receipts (upload_week, user_id) VALUES ({generate_week()}, {get_user_id()});''')

    print()

    # items
    for i in range(1501):
        print(f'''INSERT INTO items (name, price, amount, gwp, receipt_id) VALUES ('{get_food_name()}', {generate_price()}, 1, {generate_gwp()}, {get_receipt_id()});''')
