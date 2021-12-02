# web1.py 
#웹 페이지 크롤링(수집)
from bs4 import BeautifulSoup

#페이지 로딩
#메서드 체인:연속으로 호출하기
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체(HTML문서) 
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )

#문서 내부에 <p> 몽땅 ==> List형태로 리턴 
#print( soup.find_all("p") )
#첫번째 <p>태그 
#print( soup.find("p") )

#조건이 있는 경우(필터링)
#<p class="outer-text">컨텐츠</p>
print( soup.find_all("p", class_="outer-text") )



