## Running app on Docker

### Install Docker

Follow the instructions in the official Docker guide according to your operating system

- [Docker engine](https://docs.docker.com/engine/install/)

### Creating your container

The main requirement you need to follow to expose your containerized app using Nginx is to expose the same port on your container that you are proxying in your Nginx config file.

For example, if your Nginx is proxying to port `8080`, you need to expose the same port on your container so that Nginx can access it.

```conf
server {
    # ...

    location / {
        proxy_pass http://localhost:8080;
        # ...
    }
}
```
