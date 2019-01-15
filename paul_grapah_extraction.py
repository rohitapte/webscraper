#code to extract the text for all the aesop_fables into directory
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup,NavigableString

url='http://www.paulgraham.com/'
try:
    html=urlopen(url+'articles.html')
    webpage=BeautifulSoup(html.read(),'html.parser')
    results=webpage.find_all('a')
    for result in results:
        if len(result.text.strip())>0:
            link=url+result['href']
            print('Parsing:' + link)
            html = urlopen(link)
            webpage = BeautifulSoup(html.read(), 'html.parser')
            sub_results= webpage.find_all('font',attrs={'size':2})
            sText=""
            for item in sub_results[0].contents:
                if isinstance(item,NavigableString):
                    sTemp=item.strip()
                    if len(sTemp)>0 and sTemp!="[" and sTemp!="]":
                        sText+=sTemp+"\n"
            if len(sText)>0:
                print(sText)
                with open('paulgraham/'+result['href'].replace('html','txt'),'w') as output_file:
                    output_file.write(sText)

except HTTPError as e:
    print(e)