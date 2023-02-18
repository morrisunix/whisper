# Whisper (Open-AI)
Implementation of Whisper (O-AI) with Python Streamlit in Docker.

## Prerequisites
1. Docker Engine, you can install it using [official documentation](https://docs.docker.com/engine/install/).

2. Make sure you have `docker compose` installed.

## My enviromnent
I run this on my homelab, it consist of the following:

1. DNS: Cloudflare free account.
2. FW: pfSense
    - I use it to manage NAT, I have an /29 block of static IPs (provided by ATT Fiber).
    - I'm exposing `443/TCP' and '80/TCP' of one of my IPs to my Docker server (VM).
3. Hypervisor: ESXi 7.0
    - Running on a Lenovo `M93p` (ThinkCentre)
        - 4 CPUs Core i5
        - 16 GB RAM
4. Storage (iSCSI): Synology DS418j.
    - Sharing the storage via iSCSI to ESXi
5. Switch: Ubiquiti US-24-250W
6. Docker server: VM with following specs
    - OS: Debian 10 (buster)
    - CPU: 2 vCPUs
    - RAM: 5 GB
    - Disk: 20G

Note: You don't need to have a similar environment (homelab), you can run this containers on almost any computer (Desktop/Laptop) or OS (Lonux/Mac/Windows).

## Final set up
1. Clone repo:
    `git clone git@github.com:morrisunix/whisper.git`
2. Edit `nginx/app.conf` and replace [YOUR.SUB.DOMAIN] with your actual subdomain (example: whisper.morrisunix.info).
    - You can use: `sed -i 's,[YOUR.SUB.DOMAIN],your.domain,g' nginx/app.conf`
3. Edit `init-letsencrypt.sh` and replace `your@email` and `[YOUR.SUB.DOMAIN]` with your actual email and sub domain.
    - You can use: `sed -i 's,your@email,your.actual@email,g' init-letsencrypt.sh`
    - You can use: `sed -i 's,[YOUR.SUB.DOMAIN],your.domain,g' init-letsencrypt.sh`

## Commands to run the containers
1. Generate the certificates:
    - `chmod +x init-letsencrypt.sh`
    - `sudo ./init-letsencrypt.sh`
2. Build the images and start the containers:
    - `docker-compose up --build -d`

You are done!

Notes:
- The nginx proxy configuration and `init-letsencrypt.sh` where adapted from [this web](https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71)
- If you don't have a domain and/or expose 80/TCP and 443/TCP ports, you can skip the `init-letsencrypt.sh` part and only run `docker-compose up --build -d` but you won't get nginx working, so you need to test your whisper server on `http://YOU.SERVER.IP:8501` locally only.