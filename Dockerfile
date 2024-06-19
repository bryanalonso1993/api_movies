FROM python:3.12.3

WORKDIR /datapath

COPY . .

RUN pip3 install pipenv

RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python3", "app.py"]

EXPOSE 7070
