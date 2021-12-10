FROM python

# Prepare APT-GET
RUN apt-get update \
    && apt-get -y install unzip vim libaio-dev python3-watchdog

# Application
RUN mkdir -p /usr/src/app
COPY files/requirements.txt files/setup.sh /usr/src/app/

WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

# Run as user..
RUN useradd -m dr-social \
    && chown -R dr-social. /usr/src/app/
USER dr-social

# Environment Variables
ENV PYTHONUNBUFFERED=1

COPY ./app /usr/src/app/

CMD [ "sh", "-c", "python -m django startproject dr_social_backend && cd dr_social_backend && python manage.py collectstatic --noinput" ]