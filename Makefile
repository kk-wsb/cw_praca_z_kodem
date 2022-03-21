test:
	pylint app.py

run:
	pip install -r requirements.txt
	flask run
