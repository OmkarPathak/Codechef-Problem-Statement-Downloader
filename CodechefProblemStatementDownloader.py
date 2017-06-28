# Author: OMKAR PATHAK

# Script to help download problem statements from codechef

import urllib.request, bs4, re, os, time

problems = ['school', 'easy', 'medium', 'hard', 'challenge', 'extcontest']

for idx, problem in enumerate(problems):
    try:
        if idx == 1:
            os.chdir('..')
        os.mkdir(problem)
        if os.path.exists(problem):
            os.chdir(problem)
            # web address of codechef website
            codechefWebsite = 'https://www.codechef.com'
            # Get the HTML from teh website
            getHTML = urllib.request.urlopen(codechefWebsite + '/problems/' + problem)
            # Read the data
            data = getHTML.read()
            soup = bs4.BeautifulSoup(data, 'html.parser')
            check = soup.find_all(class_ = 'content-wrapper')

            result = soup.find_all(href = re.compile('problems/'))
            for i in range(15, len(result)):
                checkResult = result[i]['href']
                try:
                    getProblem = urllib.request.urlopen(codechefWebsite + checkResult)
                    dataResult = getProblem.read()

                    soup = bs4.BeautifulSoup(dataResult, 'html.parser')
                    check = soup.find_all(['p', 'h3', 'ul'])
                    # print(checkResult)
                    f = open(checkResult[10:] + '.txt', 'a')
                    for i in range(7, len(check) - 18):
                        f.write(check[i].text + '\n')
                    f.close()
                except urllib.error.HTTPError:
                    time.sleep(2)
        else:
            pass
    except FileExistsError:
        continue
