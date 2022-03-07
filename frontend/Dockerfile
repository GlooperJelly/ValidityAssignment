FROM node:16.14.0-alpine

WORKDIR /app/frontend

COPY email-app/package.json email-app/package-lock.json ./
RUN npm install
COPY ./email-app /app/frontend
EXPOSE 3000