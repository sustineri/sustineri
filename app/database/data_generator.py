from random import randint, random

NR_OF_WEEKS = 37


def get_user_id():
    return randint(2, 10)


def generate_gwp_others():
    return f'{random() * 90:.2f}'


def generate_gwp_our_user():
    return f'{random() * 80:.2f}'


def generate_price():
    return randint(0, 20)


def generate_nr_of_receipts(min, max):
    return randint(min, max)


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

    print()

    receipt_id = 1
    for week_nr in range(NR_OF_WEEKS):
        # receipts
        for i in range(generate_nr_of_receipts(8, 10)):
            print(f'''INSERT INTO receipts (upload_week, user_id) VALUES ({week_nr}, {get_user_id()});''')

            # items
            for k in range(3):
                print(f'''INSERT INTO items (name, price, amount, gwp, receipt_id) VALUES ('{get_food_name()}', {generate_price()}, 1, {generate_gwp_others()}, {receipt_id});''')

            receipt_id += 1

        print(f'''INSERT INTO receipts (upload_week, user_id) VALUES ({week_nr}, 1);''')

        # items
        for k in range(3):
            print(f'''INSERT INTO items (name, price, amount, gwp, receipt_id) VALUES ('{get_food_name()}', {generate_price()}, 1, {generate_gwp_our_user()}, {receipt_id});''')

        receipt_id += 1
