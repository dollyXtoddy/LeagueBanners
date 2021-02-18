import requests

nick = input('[!] Seu nickname: ')

for i in range(140):
    r = requests.get("http://data2.modskinpro.com/CoverFBLOL/%s/%s.jpg" % (i, nick))
    print(f"[+] Baixado {i} ({r.status_code})")
    with open('Skins/%s.png' % i, 'wb') as f:
        f.write(r.content)