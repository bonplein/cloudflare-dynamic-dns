# Cloudflare Dynamic DNS

A script with which Cloudflare can be used as a Dynamic DNS system which continuously makes sure that your external IP is mapped to your desired Domain.

## Prerequesites

A computer, NAS, etc. running python 2.x and a Cloudflare account with your domain already set up. For this purpose we'd like to use `nas.example.com` for the domain which will point to our external IP.

## Installation

```bash
git clone git@github.com:hofratsuess/cloudflare-dynamic-dns.git
cd cloudflare-dynamic-dns/
pip install -r requirements.txt
```

Then add the script to the crontab by running `crontab -e` (might not work if you're root)

```bash
crontab -e

# insert the line below (replace example with your settings)
*/10  * * * * example-user  /usr/bin/python /path/to/the/repo/cloudflare-dynamic-dns/update_dns.py user@example.com example-cloudflare-api-key example.com nas
```

That's it. This will make sure your domain always points to your home IP no matter whether your ISP changes the router IP.
