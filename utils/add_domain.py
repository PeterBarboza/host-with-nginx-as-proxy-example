import subprocess
import os, errno
import argparse

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

NGINX_SITES_AVALIABLE_PATH = '/etc/nginx/sites-available'
NGINX_SITES_ENABLE_PATH = '/etc/nginx/sites-enabled'

def active_site(domain):
    print(f"Activating domain {domain}")
    os.symlink(f"{NGINX_SITES_AVALIABLE_PATH}/{domain}", f'{NGINX_SITES_ENABLE_PATH}/{domain}')
    
def add_ssl(domain):
    print(f"Adding SSL to domain {domain}")
    subprocess.call(f"sudo certbot --nginx -d {domain}", shell=True)
    
def restart_ngix():
    print(f"Restarting NGINX")
    subprocess.call(f"sudo systemctl restart nginx;", shell=True)

def read_file(path):
    f = open(path, "r")
    file_string = f.read()

    f.close()

    return file_string

def save_file(path_with_ext, content):
    print(f"Saving file in {path_with_ext}")

    file = open(path_with_ext, "w")
    file.write(content)
    file.close()

def create_site_config(domain, port, template_file):
    file_string = read_file(template_file)
    
    file_string = file_string.replace('$PORT', str(port))
    file_string = file_string.replace('$DOMAIN', str(domain))


    return file_string


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", "-d", help="domain")
    parser.add_argument("--port", "-p", help="port")
    parser.add_argument("--template_file", "-t", help="template_file")

    args = parser.parse_args()

    print(f"Creating configs with the following setup: {args.domain} in port {args.port} using template_file {args.template_file}")
    print(f"\tDomain:        {args.domain}")
    print(f"\tPort:          {args.port}")
    print(f"\tTemplate file: {args.template_file}")

    if(args.domain is None):
        print("domain is none")
        return
    if(args.port is None):
        print("port is none")
        return
    if(args.template_file is None):
        print("template_file is none")
        return

    file_string = create_site_config(args.domain, args.port, args.template_file)
    
    save_file(os.path.join(NGINX_SITES_AVALIABLE_PATH, args.domain), file_string)
    active_site(args.domain)
    restart_ngix()
    add_ssl(args.domain)

if __name__ == "__main__":
    main()