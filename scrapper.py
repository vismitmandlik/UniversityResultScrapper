import requests
from bs4 import BeautifulSoup
import pandas as pd
from threading import Thread
from json import dumps


def get_student_result_html(enroll_no: str) -> str:
    url = "https://charusat.edu.in:912/UniExamResult/frmUniversityResult.aspx"

    payload = f'__EVENTTARGET=btnSearch&__VIEWSTATE=%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%3D%3D&__VIEWSTATEGENERATOR=B051A224&ddlInst=1&ddlDegree=39&ddlSem=4&ddlScheduleExam=6176&txtEnrNo={enroll_no}'
    headers = {
        'authority': 'charusat.edu.in:912',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'dnt': '1',
        'origin': 'https://charusat.edu.in:912',
        'referer': 'https://charusat.edu.in:912/UniExamResult/frmUniversityResult.aspx',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

student_results = []

def get_student_result(enroll_no: str) -> dict:
    global student_results

    result_html = get_student_result_html(enroll_no)
    soup = BeautifulSoup(result_html, 'html.parser')

    result = {
        'name': soup.find('span', {"id": 'uclGrd1_lblStudentName'}).text.strip(),
        'cgpa': soup.find('span', {"id": 'uclGrd1_lblCGPA'}).text.strip(),
        'studentId': enroll_no
    }


    student_results.append(result)


if __name__ == '__main__':
    student_enroll_no_start = 1
    student_enroll_no_end = 1

    student_result_threads = [
        Thread(target=get_student_result, args=[ f'21CE{str(no).rjust(3, "0")}'])
        for no in range(student_enroll_no_start, student_enroll_no_end + 1)
    ]

    for thread_no in range(student_enroll_no_start - 1, student_enroll_no_end):
        student_result_threads[thread_no].start()
    
    for thread_no in range(student_enroll_no_start - 1, student_enroll_no_end):
        student_result_threads[thread_no].join()
  
    df = pd.DataFrame(student_results)
    df.to_excel('teststudents_results.xlsx', index=False)