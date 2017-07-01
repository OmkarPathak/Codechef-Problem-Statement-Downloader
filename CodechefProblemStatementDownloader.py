# Author: OMKAR PATHAK

# Script to help download problem statements from codechef

import urllib.request, bs4, re, os, time, sys

# Function showing the progress of the download count
def progress(count = ''):
    sys.stdout.write('%s\r' % (count))
    sys.stdout.flush()

problems = ['school', 'easy', 'medium', 'hard', 'challenge', 'extcontest']

for idx, problem in enumerate(problems):
    try:
        if idx >= 1:
            os.chdir('..')

        # Create a new directory
        os.mkdir(problem)
        # If directory exists, go to that directory to save all the files
        if os.path.exists(problem):
            os.chdir(problem)
            # web address of codechef website
            codechefWebsite = 'https://www.codechef.com'
            # Get the HTML from teh website
            getHTML = urllib.request.urlopen(codechefWebsite + '/problems/' + problem)
            # Read the data
            data = getHTML.read()
            # Parse the HTML data
            soup = bs4.BeautifulSoup(data, 'html.parser')
            # Find the content-wrapper for all probl statements
            check = soup.find_all(class_ = 'content-wrapper')

            # Find specific href tags that have 'problems/' in them
            result = soup.find_all(href = re.compile('problems/'))

            downloaded = 0
            for i in range(15, len(result)):
                checkResult = result[i]['href']
                try:
                    # Opening each and every problem statements webpage and parsing the data
                    getProblem = urllib.request.urlopen(codechefWebsite + checkResult)
                    # Read the data
                    dataResult = getProblem.read()

                    soup = bs4.BeautifulSoup(dataResult, 'html.parser')
                    # Find all the elements with HTML tag names
                    check = soup.find_all(['p', 'h3', 'ul', 'pre'])
                    # Save every file with the code name
                    f = open(checkResult[10:] + '.txt', 'a')
                    # Write all the text between those HTML tags in to thhe file just created
                    for i in range(7, len(check) - 18):
                        f.write(check[i].text + '\n')
                    f.close()

                    # Display the progress
                    progress(('Downloaded ' + str(downloaded + 1) + ' of ' + str(len(result) - 15)))
                    downloaded += 1
                except urllib.error.HTTPError:
                    # This exception has to bbe caught, else you might get an error saying Service temporarily unavailable
                    time.sleep(2)
            sys.stdout.write(']')
            print('Download Complete for ', problem, ' level')
        else:
            pass
    except FileExistsError:
        continue
