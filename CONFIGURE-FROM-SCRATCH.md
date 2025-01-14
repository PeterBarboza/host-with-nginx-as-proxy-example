## Install dependencies on your host machine

### Update machine packages

```bash
sudo apt update;
sudo apt -y upgrade;
```

### Install Python3:

```bash
sudo apt update
sudo apt install python3.9
```

### Install your app dependencies

If you will run your app directly on your host machine, follow one of these guides bellow:

- [Dotnet](./examples/dotnet/README.md)
- [NodeJS](./examples/nodejs/README.md)

If you will execute your app on Docker, follow this guide:

- [Docker](./RUNNING-APP-ON-DOCKER.md)

### Install NGINX

```bash
sudo apt update
sudo apt install nginx
sudo ufw allow 'Nginx FULL'
```

### Install Certbot

```bash
sudo snap install core; 
sudo snap refresh core;

sudo apt-get -y remove certbot;
sudo snap install --classic certbot;

sudo ln -s /snap/bin/certbot /usr/bin/certbot;
```

## Configure Nginx proxy

### Create a template file with your nginx server desired configuration

If you want, you can get a copy of the [example.com.br](./example.com.br) file located on the root of this repository.

### Move/Copy the Nginx configuration file to inside your website configuration

```bash
mv /path/to/YOUR_DOMAIN_HERE /etc/nginx/sites-available/YOUR_DOMAIN_HERE
```

### Activate your domain on Nginx

```bash
sudo ln -s /etc/nginx/sites-available/YOUR_DOMAIN_HERE /etc/nginx/sites-enabled/YOUR_DOMAIN_HERE
```

### Verify configs and restart

```bash
sudo nginx -t

sudo systemctl restart nginx
```

## Configure SSL

### Add SSL to your domain

```bash
sudo certbot --nginx -d YOUR_DOMAIN_HERE
```

### Go to your server Public IP, and see your application runing!

<!-- Free SSL -->
<!-- https://certbot.eff.org/instructions?ws=nginx&os=snap -->