pip install fastapi uvicorn uvloop

uvicorn app-fastapi.main:app --app-dir=./ --reload --workers=1 --host=0.0.0.0 --port=8080  --use-colors --loop=uvloop