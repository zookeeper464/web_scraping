#main.py에서 복잡하지 않게 분리하여 파일을 저장한다.
#main.py에서 불러올 수 있도록 함수로 so.py를 구성한다.
#so.py는 indeed.py를 기반으로 호출 부분만 변경해서 사용한다.

import requests
from bs4 import BeautifulSoup as BS

limit = 10
url = "https://programmers.co.kr/job?_=1617069226344&job_position%5Bdummy%5D=0&job_position%5Bjob_category_ids%5D%5B%5D=1&job_position%5Bjob_category_ids%5D%5B%5D=12&job_position%5Bmin_career%5D=0"

def extract_pages ():
  result = requests.get(url)
  #<출력시 Response [200]이 나오면 성공적으로 실행
  #text, headers, json 등을 가져올 수 있다.(설정된 변수에 .~~를 쓴다.)

  soup = BS(result.text, "html.parser")
  #해당 url을 html형식으로 표현함

  pagination = soup.find("div", {"id" : "paginate"})
  #indeed_soup 안에서 div 형식중에서 class가 pagination인 부분을 호출
  
  links = pagination.find_all("a")

  pages = []
  for link in links[1:-1]:
    pages.append(int(link.string))
    #스판 안에 내용만 가져오는 함수 string

    #page 안에서 span 형식들을 모두 호출
  #마지막 페이지 계산
  max_pages = pages[-1]
  return max_pages

def extract_job (html):
  title = html.find("h5", {"class" : "position-title"}).find("a").string
  #html 속에서 h5의 title을 가져오고 그 중 a속의 내용을 가져온다.

  company = html.find("h6", {"class" : "company-name"}).text.strip().split("\n")[0]
  #html 속에서 class가 company인 h6의 내용을 가져온다.
  
  location = html.find("ul", {"class" : "company-info"}).find("li",{"class" : "location"}).text.strip()
  #html 속에서 class가 location인 span의 내용을 가져온다.
  
  job_id = html.find("h5", {"class" : "position-title"}).find("a")["href"]
  return {
    "title" : title,
    "company": company,
    "location" : location,
    "link" : f"https://programmers.co.kr/{job_id}"
  }
  #해당 링크와 data-jk의 내용을 비교하고 data-jk이외의 내용들을 덧붙혀 link를 만든다.

#내용 중에서 None이 포함되어 있다면 string을 사용 할 수 없고 None을 제외하고 string을 사용하도록 지정해야 한다.

def extract_jobs (last_pages):
  jobs = []
  for num in range(last_pages):
    html_ = requests.get(f"{url}&page={num}")    
    #각 페이지별로 내용 호출

    soup = BS(html_.text, "html.parser")
    #각 페이지별로 html내용 호출

    results = soup.find_all("div", {"class" : "item-body"})
    #각 회사별로 리스트 생성

    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs


def get_jobs ():
  last_pages = extract_pages()
  #마지막 페이지 호출

  jobs = extract_jobs (last_pages)
  #각 페이지 마다 해당하는 직업들 호출

  return jobs
