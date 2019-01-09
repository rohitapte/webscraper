#code to extract the text for all the aesop_fables into directory

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

url='http://www.taleswithmorals.com/'
try:
    html=urlopen(url)
    webpage=BeautifulSoup(html.read(),'html.parser')
    results=webpage.find_all('a')
    for result in results:
        if 'http' not in result['href'] and 'copyright' not in result['href'] and '//' not in result['href']:
            link=url+result['href']
            print('Parsing:' + link)
            html = urlopen(link)
            webpage = BeautifulSoup(html.read(), 'html.parser')
            sub_results= webpage.find_all('p',attrs={'align':'justify'})
            sText=""
            for item in sub_results:
                sTemp=item.text.strip()
                if len(sTemp)>0:
                    sText+=sTemp+"\n"
            if len(sText)>0:
                print(sText)
                with open('aesop/'+result['href'].replace('htm','txt'),'w') as output_file:
                    output_file.write(sText)

except HTTPError as e:
    print(e)