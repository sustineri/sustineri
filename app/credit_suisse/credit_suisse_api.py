from os import environ

import requests
from dotenv import load_dotenv


class CreditSuisseApi:
    def get_etf(self, isin='US92189F5026'):
        response = requests.post('https://csopenbankingzh.azurewebsites.net/securities/search', headers={
            **{'Content-Type': 'application/json'},
            **{'Accept': 'application/json'},
            **{'Authorization': environ.get('CREDIT_SUISSE_API_TOKEN')}}, json={
            "filter": [
                {
                    "andOr": "and",
                    "attribute": "isin",
                    "operator": "=",
                    "value": f"'{isin}'"
                }

            ],
            "sorting": " ISIN asc"
        })

        return response


if __name__ == '__main__':
    load_dotenv()
    print(CreditSuisseApi().get_etf().content)
