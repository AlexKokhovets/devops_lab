import requests


def get_pulls_by_state(state):
    return requests.get('https://api.github.com/repos/alenaPy/devops_lab/'
                        f'pulls?state={state}&per_page=100')


def get_pulls_by_label(label):
    return requests.get('https://api.github.com/search/issues?q=is:pr%20'
                        f'label:\"{label}\"%20repo:alenaPy/devops_lab&per_page=100')


def parse_pulls_from_json(js):
    ans = []
    for i in js:
        ans.append({'num': i['number'], 'title': i['title'], 'link': i['html_url']})
    return ans


def get_pulls(state):
    if state in ('open', 'closed'):
        pulls_list = get_pulls_by_state(state).json()
    elif state in ('needs work', 'accepted'):
        pulls_list = get_pulls_by_label(state).json()['items']
    else:
        pulls_list = get_pulls_by_state('all').json()
    return parse_pulls_from_json(pulls_list)
