from bs4 import BeautifulSoup as soup
import requests

website = "https://paytmmall.com"
product = input("Product-Name : ").strip().replace(' ','+')
page = input("Page-Number : ")
paytm = requests.get(website+"/shop/search?q="+product+"&page="+page)
paytm_html = soup(paytm.content,"html.parser")
filename = product+".csv"
f = open(filename.replace('+',' '),"w")
for link in paytm_html.find_all("a",class_="_8vVO"):
    paytm_product = requests.get(website+link.get("href"))
    paytm_product_html = soup(paytm_product.content,"html.parser")
    name = paytm_product_html.find_all("h1",class_="NZJI")[0].text.replace(',','|')
    prize = paytm_product_html.find_all("span",class_="_1V3w")[0].text.replace(',','')
    key = list(map(lambda x:x.text.replace(',','|'),paytm_product_html.find_all("div",class_="w3LC")))
    value = list(map(lambda x:x.text.replace(',','|'),paytm_product_html.find_all("div",class_="_2LOI")))
    f.write("Product-Name,"+name+"\n")
    f.write("Prize,Rs. "+prize+"\n")
    for i in range(len(key)):
        f.write(key[i]+","+value[i]+"\n")
    f.write("\n\n\n")
f.close()
print("Done")