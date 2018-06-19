# from the docker hub, click the version link
FROM nginx:1.15.0-alpine

# env variable
ENV NGINX_VERSION 1.15.0.alpine

# run scripts

# RUN pip install boto3

#expose the port number
EXPOSE 90 8080

# required to run this when container is started, only one CMD allows
CMD ["nginx", "-g", "daemon off;"]