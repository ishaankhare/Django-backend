FROM python:3.12.3-slim-bookworm

ARG DEV=false

ENV \
PYTHONUNBUFFERED=1 \
PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /src

# Copy the current directory contents into the container at /governance
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# run gunicorn
CMD ["sh", "-c",\
    "\
    python manage.py collectstatic --noinput && \
    python manage.py migrate --noinput && \
    python manage.py ensure_adminuser && \
    python manage.py ensure_self_host_site && \
    gunicorn home.wsgi:application -b 0.0.0.0:8000 -k gevent"\
]
