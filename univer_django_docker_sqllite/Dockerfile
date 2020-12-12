 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /univer_django_docker_sqllite
 WORKDIR /univer_django_docker_sqllite
 ADD requirements.txt /univer_django_docker_sqllite/
 RUN pip install -r requirements.txt
 ADD . /univer_django_docker_sqllite/
