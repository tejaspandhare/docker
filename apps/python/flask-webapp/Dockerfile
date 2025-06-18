FROM python:3.10-alpine

# Set working directory
WORKDIR /code

# Environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80
ENV CUSTOM_HEADER='Welcome to My Test Containerized Webapp -Tejas Pandhare'
ENV BG_COLOR=white
ENV FONT_COLOR=black
ENV CUSTOM_PHOTO='https://raw.githubusercontent.com/tejaspandhare/assets/main/images/tp_01.png'

# Install dependencies and sudo
RUN apk add --no-cache gcc musl-dev linux-headers bash sudo

# Create non-root user and add to sudoers
RUN adduser -D -u 1000 pyuser && echo "pyuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Copy and install requirements
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install curl
RUN apk add --no-cache curl

# Copy project files
COPY . .

# Set ownership to pyuser
RUN chown -R pyuser:pyuser /code

# Switch to non-root user
USER pyuser

# Expose Flask port
EXPOSE 80

# Run Flask
CMD ["flask", "run"]
