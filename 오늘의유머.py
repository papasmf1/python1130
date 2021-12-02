# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#웹로봇==> 웻봇 
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#웹사이트 페이지 번호 수정 
for n in range(1,11):
        #오늘의 유머 베스트 게시판 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 디코딩(유니코드 방식) 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        #<td class="subject"><a href="/board/view.php">응급 환자를 살린 소방관의 지혜</a>
        list = soup.find_all('td', attrs={'class':'subject'})

        for item in list:
                try:
                        title = item.find("a").text 
                        #print(title)
                        #re모듈에서 검색 
                        if (re.search('한국', title)):
                                print(title.strip())
                except:
                        pass
        
