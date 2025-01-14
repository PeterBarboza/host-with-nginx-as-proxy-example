## Install dependencies on your host machine

### Install the firewall manager `ufw`

```bash
sudo apt install ufw
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

## Configure Nginx proxy using `add_domain.py` helper script

### Create a template file with your nginx server desired configuration

If you want, you can get a copy of the [example.com.br](./example.com.br) file located on the root of this repository.

Access the directory where the `add_domain.py` file is located and run the following command:

```bash
sudo python3 add_domain.py --d YOUR_DOMAIN_HERE --p 3333 --t /path/to/your/domain-config-template-file
```

### Go to your server Public IP, and see your application runing!
