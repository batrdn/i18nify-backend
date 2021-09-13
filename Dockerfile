FROM ubuntu:18.04
RUN apt-get update && apt-get install -y python3 python3-pip aspell aspell-en myspell-de-de libenchant1c2a python-enchant
ENV LANG=C.UTF-8
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
