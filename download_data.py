import requests
from PIL import Image
# from tika import parser
from pathlib import Path
from pdf2image import convert_from_path

import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image


def download_pdf(url: str,filename: str, payload: dict = {}, headers: dict = {}) -> int:

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    filename.write_bytes(response.content)

def pdf_to_image(pdf_path: str, supermarket_name: str, img_format: str = 'png'):
  pages = convert_from_path(f'{supermarket_name}-encarte.pdf')

  for i in range(len(pages)):
    pages[i].save(f'encarte_{supermarket_name}-'+ str(i) + f'.{img_format.lower()}', img_format.upper())


url = "https://arquivos.superredesupermercados.com.br/imagens/encartes/90/encarte.pdf" #"https://www.supermercadosguanabara.com.br/encarte/baixe"
supermarket_name = 'superrede'
pdf_path = f'{supermarket_name}-encarte.pdf'
filename = Path(pdf_path)
img_format = 'jpeg'

download_pdf(url, filename)

pdf_to_image(pdf_path,supermarket_name, img_format)

extractedInformation = pytesseract.image_to_string(Image.open('encarte_superrede-0.jpeg'))