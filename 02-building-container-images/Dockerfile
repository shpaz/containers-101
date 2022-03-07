FROM python:3
RUN mkdir /usr/src/app
ADD app.py /usr/src/app
ADD requirements.txt /usr/src/app 
WORKDIR /usr/src/app
EXPOSE 5000
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python","app.py"]
