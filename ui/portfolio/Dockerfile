# Name the node stage "builder"
FROM node:12

WORKDIR /app

COPY package-lock.json package.json ./
RUN npm install

COPY . .

EXPOSE 8080
