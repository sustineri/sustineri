from os import environ

import requests
from dotenv import load_dotenv


class CreditSuisseApi:
    def get_etf(self):
        response = requests.post('https://csopenbankingzh.azurewebsites.net/securities/search', headers={
            **{'Content-Type': 'application/json'},
            **{'Accept': 'application/json'},
            **{'Authorization': environ.get('CREDIT_SUISSE_API_TOKEN')}}, json={
            "filter": [
                {
                    "andOr": "and",
                    "attribute": "isin",
                    "operator": "in",
                    "value": f"('US92189F5026', 'US33733E5006', 'US26923G3011', 'US46138G7060')"
                }

            ],
            "sorting": " ISIN asc"
        })

        return response


if __name__ == '__main__':
    load_dotenv()
    print(CreditSuisseApi().get_etf().content)
