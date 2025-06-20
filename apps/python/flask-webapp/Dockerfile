FROM python:3.10-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
ENV CUSTOM_HEADER='Welcome to My Test Containerized Webapp -Tejas Pandhare'
ENV BG_COLOR=white
ENV FONT_COLOR=black
ENV CUSTOM_PHOTO='https://raw.githubusercontent.com/tejaspandhare/assets/main/images/tp_01.png'
RUN apk add --no-cache gcc musl-dev linux-headers bash sudo
RUN adduser -D -u 1000 pyuser && echo "pyuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN apk add --no-cache curl
COPY . .
RUN chown -R pyuser:pyuser /code
USER pyuser
EXPOSE 8080
CMD ["flask", "run"]
