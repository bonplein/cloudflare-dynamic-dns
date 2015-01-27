#coding: utf-8

import sys
from requests import get
from pyflare import PyflareClient

# parsing command line arguments
email = sys.argv[1]
api_key = sys.argv[2]
root_domain = sys.argv[3]
sub_domain = sys.argv[4]
full_domain = sub_domain + '.' + root_domain

# get the current outside ip
outside_ip = get('http://api.ipify.org').text

# ask clouflare for all domain settings for that root_domain
cf = PyflareClient(email, api_key)
for setting in cf.rec_load_all(root_domain):

    # get the dynamic dns entry from cloudflare
    if (setting['name'] == full_domain) and (setting['type'] == 'A'):

        # check if the ip address behind the dns entry is the one it should be
        if outside_ip != setting['content']:

            # change the ip address for that entry
            single_domain_setting = cf.rec_edit(root_domain, 'A', setting['rec_id'], sub_domain, outside_ip)

            # print message if dns entry was modified
            if single_domain_setting['result'] == 'success':
                print 'dns update successful'
