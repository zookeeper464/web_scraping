import csv
#csv를 활용하게 해주는 모듈

def save_to_file(name, jobs):
  file = open(f"{name}.csv", mode = "w")
  #해당 파일을 쓰기 모드로 연다.

  writer = csv.writer(file)
  writer.writerow("title, company, location, link".split(","))
  #저장하려는 자료의 key값을 저장한다.
  
  for job in jobs:
    writer.writerow(job.values())
  #불러온 자료들을 규칙에 맞게 적기
  
  return
