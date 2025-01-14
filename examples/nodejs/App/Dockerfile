FROM node:23

WORKDIR /app

COPY --chown=node:node index.js ./index.js

RUN yarn install --frozen-lockfile

CMD ["node", "index.js"]