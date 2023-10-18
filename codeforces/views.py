import requests
from bs4 import BeautifulSoup
from rest_framework.decorators import api_view
from rest_framework.response import Response

from problems.models import Problem


@api_view(['GET'])
def parse_problem(request):
    api_url = 'https://codeforces.com/api/problemset.problems'
    response = requests.get(api_url).json()

    if response['status'] != 'OK':
        return Response({'status': 'error'}, status=400)

    cnt = 0

    for problem in response['result']['problems']:
        contest_id = problem['contestId']
        index = problem['index']
        problem_link = f"https://codeforces.com/problemset/problem/{contest_id}/{index}"
        if Problem.objects.filter(problem_link=problem_link).exists():
            continue
        cnt += 1
        print(cnt, problem_link)
        data = requests.get(problem_link).content
        soup = BeautifulSoup(data, 'html.parser')

        # Extract relevant information from the soup object
        problem_title = soup.select_one('.problem-statement .title').text.strip()
        problem_statement = str(soup.select_one('.problem-statement').findChildren('div', recursive=False)[1])
        input_specification = str(soup.select_one('.problem-statement .input-specification'))
        output_specification = str(soup.select_one('.problem-statement .output-specification'))


        problem = Problem()
        problem.judge = Problem.JUDGE_CODEFORCES
        problem.title = problem_title
        problem.problem_statement = problem_statement
        problem.input_specification = input_specification
        problem.output_specification = output_specification

        problem.time_limit = '1 seconds'
        problem.memory_limit = '256 megabytes'
        problem.problem_link = problem_link
        problem.source = 'Codeforces'
        problem.contest_id = contest_id
        problem.index = index
        problem.save()


    # link = request.GET.get('link')
    #
    # # if Problem.objects.filter(problem_link=link).exists():
    # #     return Response({'status': 'already exists'}, status=200)
    # data = requests.get(link).content
    # soup = BeautifulSoup(data, 'html.parser')
    #
    # # Extract relevant information from the soup object
    # problem_title = soup.select_one('.problem-statement .title').text.strip()
    # problem_statement = str(soup.select_one('.problem-statement').findChildren('div', recursive=False)[1])
    # input_specification = str(soup.select_one('.problem-statement .input-specification'))
    # output_specification = str(soup.select_one('.problem-statement .output-specification'))
    #
    # problem = Problem()
    # problem.judge = Problem.JUDGE_CODEFORCES
    # problem.title = problem_title
    # problem.problem_statement = problem_statement
    # problem.input_specification = input_specification
    # problem.output_specification = output_specification
    #
    # problem.time_limit = '1 seconds'
    # problem.memory_limit = '256 megabytes'
    # problem.problem_link = link
    # problem.source = 'Codeforces'
    # problem.save()

    return Response({'status': 'ok'}, status=201)
