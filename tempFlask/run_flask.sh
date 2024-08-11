pip install -r src/requirements.txt
pip install gunicorn

gunicorn -w 4 -b 0.0.0.0:5000 'src.app-flask.main:app' --reload
