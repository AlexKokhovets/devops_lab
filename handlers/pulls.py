import requests

passw = ('user', 'pass')


def get_pulls(state):

    if state in ('open', 'closed'):
        response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/'
                                f'pulls?state={state}&per_page=100', auth=passw)
        pulls_list = response.json()
    elif state in ('needs work', 'accepted'):
        response = requests.get('https://api.github.com/search/issues?q=is:pr%20'
                                f'label:\"{state}\"%20repo:alenaPy/devops_lab&per_page=100',
                                auth=passw)
        pulls_list = response.json()['items']
    else:
        response = requests.get('https://api.github.com/repos/alenaPy/devops_lab/'
                                'pulls?state=all&per_page=100', auth=passw)
        pulls_list = response.json()

    ans = []
    for i in pulls_list:
        ans.append({'num': i['number'], 'title': i['title'], 'link': i['html_url']})
    return ans
