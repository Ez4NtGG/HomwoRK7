
FROM python:3.11


ENV APP_HOME /app 


WORKDIR $APP_HOME


COPY . .
COPY .config/config_docker.ini .config/config.ini
COPY run.sh run.sh 
COPY migrations/ migrations/
COPY src/ src/
COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt 

CMD ./run.sh 

