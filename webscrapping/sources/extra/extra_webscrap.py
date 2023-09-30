
from requests import get
from bs4 import BeautifulSoup

url = "https://www.extra.com.br/c?filtro=d45876&ordenacao=_maisvendidos&icid=156589_hp_stc_c9_ps1_b0_pb15&page=1"

# url = "https://www.google.com/"
response = get(url)

print(response.text)