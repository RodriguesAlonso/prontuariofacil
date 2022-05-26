install:
	pip install -e .

app:
	export FLASK_APP=prontuariofacil/app.py
	export FLASK_ENV=development
	
debug:
	export FLASK_ENV=development