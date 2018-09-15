import requests


class CreditSuisseApi:
    def get_etf(self, isin='US92189F5026'):
        response = requests.post('https://csopenbankingzh.azurewebsites.net/securities/search', headers={
            **{'Content-Type': 'application/json'},
            **{'Accept': 'application/json'},
            **{'Authorization': 'Bearer '
                             'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik9UUXlRVGRCTkRFNU1rWTNNMFZFTnpNeU9'
                             'EWkJOa1pETkRCR1FrRkZOamxDTTBJeE5EazRNdyJ9.eyJpc3MiOiJodHRwczovL2dicHJvamVjdC5hd'
                             'XRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWI5Y2NhZmZmMTY0MjcyMWFkODc3YjM4IiwiYXVkIjpbImh0'
                             'dHBzOi8vb3BlbmJhbmtpbmcuY29tL2FwaSIsImh0dHBzOi8vZ2Jwcm9qZWN0LmF1dGgwLmNvbS91c2V'
                             'yaW5mbyJdLCJpYXQiOjE1MzcwMDI2NjksImV4cCI6MTUzNzA4OTA2OSwiYXpwIjoicThJTVlzMVNLek'
                             't0WExvdjhWM0pab3oxaE43MHgzQTciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwiZ3R5I'
                             'joicGFzc3dvcmQifQ.msY9zkJImLl2-QzlSAw9IIaHyacZJhBAMTA1LwzdFCikUM4acsqfReyb6IQdp'
                             'NfYPLL7mM5cI8goo48z_1gcs1ewzyER6r-lG-yrQtI-ClFHiY2Kfs4BynuIpER64bUU-7i4kIDF6hGa'
                             'qsnexQlOCLNWAgkbBCqkSNnKOL6tw9J1D6wSbmKHhqDZkp7JkGe3brcEjuXdaJggWouHZYeaXjucHfF'
                             'X9-7gannx5oMP2UmY6w0gSLjhr_nCwwRMtOe6YB8i3moGlYQGKZFvi10lyjD8tKJkagLxbBnDHaci2k'
                             '5rz1KB3QIvT1GMKSVUkcmn_tZb22LdI9m1NGVph3v5Rw'},
        }, json={
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
    print(CreditSuisseApi().get_etf().content)
