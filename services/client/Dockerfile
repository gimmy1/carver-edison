# base image
FROM node:10.4.1-alpine

# set working directory
WORKDIR /twt/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /twt/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /twt/src/app/package.json
RUN npm install
RUN npm install react-scripts@1.1.4 -g

# start app
CMD ["npm", "start"]