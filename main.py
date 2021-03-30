#urllib3와 requests의 성능, 효과 비교(urllib3보다 더 효율적)
#requests는 설치가 필요하다.
#위에 두 모듈은 주소의 html을 불러오는 역할을 한다.
#Beautifulsoup도 설치가 필요하다.
#Beautifulsoup은 텍스트의 추출과 정렬하는 기능을 한다.

from indeed import get_jobs as get_indeed_jobs
from pros import get_jobs as get_pros_jobs
from save import save_to_file as sv
#모든 함수를 indeed파일에 저장, 필요한 직업들 호출 함수만 불러오기

indeed_jobs = get_indeed_jobs()
#indeed에서 필요한 요소들 리스트

sv("indeed_jobs", indeed_jobs)
#indeed_jobs를 csv에 저장

pros_jobs = get_pros_jobs()
#programmers에서 필요한 요소들 리스트

sv("pros_jobs", pros_jobs)
#pros_jobs를 csv에 저장
