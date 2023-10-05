# Specify a base image
FROM node:18-alpine

# Prepare a working directory
WORKDIR /opt/app

# Install some dependencies
COPY ./package.json ./
RUN npm install
COPY ./ ./

# Default command
CMD ["npm", "start"]