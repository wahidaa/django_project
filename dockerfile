FROM python:3
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
#RUN python3 manage.py makemigrations api_app
#RUN python3 manage.py migrate api_app
#RUN python3 manage.py migrate --run-syncdb
#RUN python3 manage.py loaddata sample.json
#RUN pytest