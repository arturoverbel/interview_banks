FROM python:3.10

ENV DockerHOME=/home/app/webapp
RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME
RUN pip3 install --upgrade pip
COPY . $DockerHOME
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver
