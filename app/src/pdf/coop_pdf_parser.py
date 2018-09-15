import base64
import pdftotext
import re


class CoopPdfParser:
    START_ROW = 5
    STOP_ROW = 'Total CHF'
    AMOUNT_INDEX = 1
    PRICE_INDEX = 2

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

            products.append((product_name,
                             product_data[CoopPdfParser.AMOUNT_INDEX],
                             product_data[CoopPdfParser.PRICE_INDEX]))

        return products
