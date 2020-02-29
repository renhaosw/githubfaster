import requests
from bs4 import BeautifulSoup

urllist = [
    "https://github.com.ipaddress.com/www.github.com",
    "https://fastly.net.ipaddress.com/github.global.ssl.fastly.net"
]
url = "https://github.com.ipaddress.com/www.github.com"

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}

if __name__ == '__main__':
    iplist = []
    for url in urllist:
        r = requests.get(url, headers=headers)
        #r.encoding = 'utf-8'
        soup = BeautifulSoup(r.content, 'html.parser')
        name = soup.find("section").find("li")
        iplist.append(name.contents[0] + "  " + url[8:].split(sep='/')[-1] +
                      "\n")
    iplist.append(
        "#1.For windows copy lines in the ip.txt to the end of C:\Windows\System32\drivers\etc\hosts /etc/hosts for linux\n"
        "#2.run cmd as administrator \n#3.execute command ipconfig /flushdns\n"
    )

    with open("ip.txt", "w") as f:
        f.writelines(iplist)
    print("Over")