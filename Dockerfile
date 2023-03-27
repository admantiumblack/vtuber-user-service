FROM tiangolo/uvicorn-gunicorn:python3.9

WORKDIR /project

COPY . /project

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "start.py"]