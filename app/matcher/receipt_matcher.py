import json


class ReceiptMatcher:

    def __init__(self):
        self.foot_print_data = json.loads('../carbon_data/carbon_data.json')

    def match(self, item):
        pass


if __name__ == '__main__':
    ReceiptMatcher().match('Eier')
