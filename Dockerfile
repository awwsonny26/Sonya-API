FROM node:20

WORKDIR /app

COPY package*.json ./
COPY prisma ./prisma

RUN npm install
RUN npx prisma generate

COPY . .

ENV PORT=8080

CMD sh -c "npx prisma migrate deploy && node src/server.js"
