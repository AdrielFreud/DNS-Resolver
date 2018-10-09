  #  Desenvolvido por Adriel Freud!
  #  Contato: businessc0ro2k17@gmail.com 
  #  FB: http://www.facebook.com/xrn401
  #   =>DebutySecTeamSecurity<=

import requests
import re
import socket
import sys
from bs4 import BeautifulSoup
try:
	import dns.resolver
except:
	print("You need the DNS Python library from http://www.dnspython.org")
	exit(1)

menu = """\n
   _____ _      ____  _    _ _____  ______ _____ _____  ______ 
  / ____| |    / __ \| |  | |  __ \|  ____|_   _|  __ \|  ____|
 | |    | |   | |  | | |  | | |  | | |__    | | | |__) | |__   
 | |    | |   | |  | | |  | | |  | |  __|   | | |  _  /|  __|  
 | |____| |___| |__| | |__| | |__| | |     _| |_| | \ \| |____ 
  \_____|______\____/ \____/|_____/|_|    |_____|_|  \_\______|
                                                               
Powered by Adriel Freud...\n"""

Channel = "https://www.youtube.com/AdrielFreud"

DEFAULT_USER_AGENTS = {
    "Macintosh": {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"},
    "Linux":{"User-Agent":"Mozilla/5.0 (Linux; ParrotOS 7.0; Moto G (5) Build/NPPS25.137-93-8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36"},
    "Windows":{"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"},
    }

def checkDomain(domain):
	list_dns = []
	try:
		answers = dns.resolver.query(domain, 'MX')
		for domains in answers.rrset:
			list_dns.append(str(domains).split()[1])

		return (list_dns)
	except:
		return False

def checkMXResolve(mx):
	try:
		answers = dns.resolver.query(mx, 'A')
		return str(answers[0])
	except:
		return False

def DNS_Cloudfire(url):
	new_url = url.split('/')
	tam = len(new_url)
	req = requests.post("http://www.crimeflare.org:82/cgi-bin/cfsearch.cgi", headers=DEFAULT_USER_AGENTS["Linux"], data={'cfS':new_url[tam-1]})
	if req.status_code == requests.codes.ok:
		html = req.text
		bs = BeautifulSoup(html, 'lxml')
		bs.find_all("br")
		print("[+] Channel Analysis: %s\n"%Channel)
		print("[=>] Server: %s"%url)

		try:
			print("[+] MX Servers: %s"%checkMXResolve(new_url[tam-1]))
			print('\n')
			for domains in checkDomain(new_url[tam-1]):
				print("[+] Name Server: %s\n[+] IP Real is: %s"%(domains, socket.gethostbyname(domains)))
		except:
			pass

		if bs:
			name_servers = re.findall(r"[\w.][\w.][\w.]+\.+[\w.][\w.][\w.]+\.+[\w.][\w.][\w.]", bs.get_text())
			print('\n')
			for name in name_servers:
				if 'cloud' in name:
					print("[+] CloudFare Name Server: %s\n[+] IP Cloudfare: %s"%(name, socket.gethostbyname(name)))
				else:
					print("[+] Name Servers: %s\n[+] IP: %s"%(name, socket.gethostbyname(name)))
		else:
			print("[!] Failed to Search name Servers!\n")
	else:
		print("[!] Failed to Resolve Cloudfire!\n")
		

def main():
	if len(sys.argv) < 3:
		print(menu+"\n\tMethod Usage:\n\n\t\troot@localhost~# python %s -d domain.com"%sys.argv[0])
		exit(1)
	else:
		url = sys.argv[2]
		print(menu)
		DNS_Cloudfire(url)

main()