FROM node:20-alpine3.18
COPY src/webapp/package*.json ./
RUN npm cache clean --force
RUN npm install -g npm@10.5.0

RUN npm install -g @angular/cli
RUN npm install
# RUN npm install ng


COPY src/webapp/ /webapp/
# WORKDIR /webapp

# Expose port for development server
EXPOSE 4200

# Start the development server
CMD [ "npm", "start" ]