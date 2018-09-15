import json
from os.path import abspath, dirname, join

from dotenv import load_dotenv

CARBON_DATA_PATH = abspath(join(dirname(abspath(__file__)), '..', 'carbon_data'))


class ReceiptMatcher:

    def __init__(self):
        self.foot_print_data = json.loads(open(join(CARBON_DATA_PATH, 'carbon_data.json')).read())

    def match(self, input_food_name):
        global_word_match_count = 0
        closest_match = ''
        match_footprint = 0

        for foot_print_item in self.foot_print_data:
            local_word_match_count = 0
            food_name = foot_print_item['name']
            target_words = [food_name_part.lower() for food_name_part in food_name.split(' ')]
            source_words = input_food_name.lower().split(' ')
            for source_word in source_words:
                if source_word in target_words:
                    local_word_match_count += 1
                if local_word_match_count > global_word_match_count:
                    global_word_match_count = local_word_match_count
                    closest_match = food_name
                    match_footprint = foot_print_item['gwp']

        return closest_match, match_footprint


if __name__ == '__main__':
    load_dotenv()
    print(f'Match: {ReceiptMatcher().match("Schweinefleisch")}')
