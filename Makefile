install-requirements:
	python3 -m pip install -r requirements.txt

scrapp-data:
	python3 data/poc_prezunic.py
	python3 data/poc_mercadolivre.py
	python3 data/poc_paodeacucar.py


up-api:
	python3 -m uvicorn api.main:app --reload

get-api:
	python3 get.py > response.txt

post-api:
	python3 post.py

delete-api:
	python3 delete.py

all:
	make install-requirements
	up-api
