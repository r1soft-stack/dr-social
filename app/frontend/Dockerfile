FROM node

# Create app directory
RUN mkdir -p /usr/src/app \
    && mkdir /tmp/update-check

# Set working DIR
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
ADD ./package*.json ./
# ADD ./npm-shrinkwrap.json ./

COPY ./dr_social_frontend/ ./

# Run as user..
RUN useradd dr-social \
    && chown -R dr-social. /usr/src/app/ \
    && chown -R dr-social. /tmp \
    && chown -R dr-social. /usr/local \
    && chown -R dr-social. /tmp/update-check \
    && mkdir /home/dr-social && chown -R dr-social. /home/dr-social

USER dr-social

# Install `serve` to run the application.
ENV NODE_OPTIONS=--openssl-legacy-provider
RUN npm install -g serve \
    && npm install

# Starting the prodcution optimized build
CMD serve -s build -l 3000
