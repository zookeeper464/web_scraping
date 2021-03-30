#main.py에서 복잡하지 않게 분리하여 파일을 저장한다.
#main.py에서 불러올 수 있도록 함수로 indeed.py를 구성한다.

import requests
from bs4 import BeautifulSoup as BS

limit = 10
url ="https://kr.indeed.com/jobs?q=python&jt=new_grad&fromage=14"

def extract_pages ():
  result = requests.get(url)
  #<출력시 Response [200]이 나오면 성공적으로 실행
  #text, headers, json 등을 가져올 수 있다.(설정된 변수에 .~~를 쓴다.)

  soup = BS(result.text, "html.parser")
  #해당 url을 html형식으로 표현함

  pagination = soup.find("div", {"class" : "pagination"})
  #indeed_soup 안에서 div 형식중에서 class가 pagination인 부분을 호출

  links = pagination.find_all("a")

  pages = []
  for link in links[:-1]:
    pages.append(int(link.find("span").string))
    #스판 안에 내용만 가져오는 함수 string

    #page 안에서 span 형식들을 모두 호출
  #마지막 페이지 계산
  max_pages = pages[-1]
  return max_pages

def extract_job (html):
  title = html.find("h2", {"class" : "title"}).find("a")["title"]
  #html 속에서 h2의 title을 가져오고 그 중 a속의 title을 가져온다.

  company = html.find("span", {"class":"company"}).string
  company = company.strip()
  #html 속에서 class가 company인 span의 내용들을 가져온다.

  location = html.find("span", {"class" : "location"}).string
  #html 속에서 class가 location인 span의 내용을 가져온다.
  job_id = html["data-jk"]
  return {
    "title" : title,
    "company": company,
    "location" : location,
    "link" : f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?jk={job_id}&from=serp&vjs=3"
  }
  #해당 링크와 data-jk의 내용을 비교하고 data-jk이외의 내용들을 덧붙혀 link를 만든다.

#내용 중에서 None이 포함되어 있다면 string을 사용 할 수 없고 None을 제외하고 string을 사용하도록 지정해야 한다.

def extract_jobs (last_pages):
  jobs = []
  for num in range(last_pages):
    html_ = requests.get(f"{url}&start={limit * num}")    
    #각 페이지별로 내용 호출

    soup = BS(html_.text, "html.parser")
    #각 페이지별 html호출

    results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
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
