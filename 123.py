import requests

url = "https://api.map.com.tw/net/GraphicsXY_TWMAP.aspx?search_class=address&searchkey=32FAFAA12E07573A06C6BAFFCC206D162C7C9D49&fun=funA&SearchWord=%E6%96%B0%E5%8C%97%E5%B8%82%E4%B8%AD%E5%92%8C%E5%8D%80%E4%B8%AD%E6%AD%A3%E8%B7%AF716%E8%99%9F"

payload={}
headers = {
  'Cookie': 'ServerName=www%2Emap%2Ecom%2Etw; ASPSESSIONIDAWDSBADB=PGNPAFCCAGHKBDBOPKODEAOJ; ASP.NET_SessionId=godj1whm2w2xuyixazgx1y2q; ASP.NET_SessionId=siv2wsk2aywxosmhmiqvnv12',
  'Host': 'api.map.com.tw',
  'Referer': 'https://www.map.com.tw/'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
