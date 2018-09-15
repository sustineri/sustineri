import base64
import pdftotext
import re


class CoopPdfParser:
    START_ROW = 5
    STOP_ROW = 'Total CHF'
    AMOUNT_INDEX = 0
    PRICE_INDEX = 1

    @staticmethod
    def parse(pdf_stream):
        with open('pdf_file.pdf', mode='wb') as fw:
            fw.write(base64.decodebytes(str.encode(pdf_stream)))

        with open('pdf_file.pdf', mode='rb') as fr:
            pdf = pdftotext.PDF(fr)

        products = []
        for line in pdf[0].splitlines()[CoopPdfParser.START_ROW:]:
            if line.startswith(CoopPdfParser.STOP_ROW):
                break

            product_name = line[:line.find('  ')].strip()
            product_data = re.sub('\s+', ' ', line[len(product_name):]).strip().split(' ')

            amount = float(product_data[CoopPdfParser.AMOUNT_INDEX])
            if amount == 1.0:
                amount = CoopPdfParser.__parse_amount(product_name)

            record = {}
            record['productName'] = product_name
            record['price'] = float(product_data[CoopPdfParser.PRICE_INDEX])
            record['amount'] = amount

            products.append(record)

        return products

    @staticmethod
    def __parse_amount(product_name):
        product_name = product_name.lower()

        match = re.search(r'[0-9]x[0-9]+kg', product_name)
        if match is not None:
            amount = match.group(0).split('x')
            return int(amount[0]) * float(amount[1][:-len('kg')])

        match = re.search(r'[0-9]+kg', product_name)
        if match is not None:
            return float(match.group(0)[:-len('kg')])

        match = re.search(r'[0-9]x[0-9]+g', product_name)
        if match is not None:
            amount = match.group(0).split('x')
            return int(amount[0]) * float(amount[1][:-len('g')]) / 1000

        match = re.search(r'[0-9]+g', product_name)
        if match is not None:
            return float(match.group(0)[:-len('g')]) / 1000

        match = re.search(r'[0-9]x[0-9]+l', product_name)
        if match is not None:
            amount = match.group(0).split('x')
            return int(amount[0]) * float(amount[1][:-len('l')])

        match = re.search(r'[0-9]+l', product_name)
        if match is not None:
            return float(match.group(0)[:-len('l')])

        match = re.search(r'[0-9]x[0-9]+cl', product_name)
        if match is not None:
            amount = match.group(0).split('x')
            return int(amount[0]) * float(amount[1][:-len('cl')]) / 100

        match = re.search(r'[0-9]+cl', product_name)
        if match is not None:
            return float(match.group(0)[:-len('cl')]) / 100

        return 1.0

