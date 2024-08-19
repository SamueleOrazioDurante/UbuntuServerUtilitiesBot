FROM python:3.10.12
ENV TZ="Europe/Rome"

WORKDIR /usr/src/app

RUN apt update && apt install -y \
	iputils-ping

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "./main.py"]
