from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *
import os

ROOT_DIR = 'websites'
create(ROOT_DIR)

def gather(name,url):
	domain_name = get_domain_name(url)
	ip_address = get_ip_address(url)
	nmap = get_nmap('-F',ip_address)
	robots_txt = get_robots_txt(url)
	whois = get_whois(domain_name)
	reports(name,url,domain_name,nmap,robots_txt,whois)

def reports(name,url,domain_name,nmap,robots_txt,whois):
	project_dir = ROOT_DIR + '/' + name
	create(project_dir)
	data = url + domain_name + ip_address + nmap + robots_txt + whois
	write(project_dir + 'details.txt',data)
	
gather('thenewsboston','https://www.thenewsboston.com/')
