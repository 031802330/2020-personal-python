import json

def load_data():
    with open("./data.json", 'r', encoding='utf-8') as fp:
        data = [json.loads(line) for line in fp.readlines()]
    return data

def user(data):
    fourtype_times = {}
    for item in data:
        if not isinstance(fourtype_times.get(item["actor"]['id'], None), dict):
            fourtype_times[item["actor"]['id']] = {}
        if item['type'] in ['PushEvent', 'IssueCommentEvent', 'IssuesEvent', 'PullRequestEvent']:
            fourtype_times[item["actor"]['id']][item['type']] = fourtype_times[item["actor"]['id']].get(item['type'], 0) + 1
    for key in fourtype_times:
        fourtype_times[key]['PushEvent'] = fourtype_times[key].get('PushEvent', 0)
        fourtype_times[key]['IssueCommentEvent'] = fourtype_times[key].get('IssueCommentEvent', 0)
        fourtype_times[key]['IssuesEvent'] = fourtype_times[key].get('IssuesEvent', 0)
        fourtype_times[key]['PullRequestEvent'] = fourtype_times[key].get('PullRequestEvent', 0)
    return fourtype_times

def repo(data):
    fourtype_times = {}
    for item in data:
        if not isinstance(fourtype_times.get(item["repo"]['id'], None), dict):
            fourtype_times[item["repo"]['id']] = {}
        if item['type'] in ['PushEvent', 'IssueCommentEvent', 'IssuesEvent', 'PullRequestEvent']:
            fourtype_times[item["repo"]['id']][item['type']] = fourtype_times[item["repo"]['id']].get(item['type'], 0) + 1
    for key in fourtype_times:
        fourtype_times[key]['PushEvent'] = fourtype_times[key].get('PushEvent', 0)
        fourtype_times[key]['IssueCommentEvent'] = fourtype_times[key].get('IssueCommentEvent', 0)
        fourtype_times[key]['IssuesEvent'] = fourtype_times[key].get('IssuesEvent', 0)
        fourtype_times[key]['PullRequestEvent'] = fourtype_times[key].get('PullRequestEvent', 0)
    return fourtype_times

def user_and_repo(data):
    fourtype_times = {}
    for item in data:
        fourtype_times[item['actor']['id']] = {}
    for item in data:
        fourtype_times[item['actor']['id']][item['repo']['id']] = {}
    for item in data:
        if item['type'] in ['PushEvent', 'IssueCommentEvent', 'IssuesEvent', 'PullRequestEvent']:
            fourtype_times[item['actor']['id']][item['repo']['id']][item['type']] = fourtype_times[item['actor']['id']][item['repo']['id']].get(item['type'], 0) + 1
        fourtype_times[item['actor']['id']][item['repo']['id']]['PushEvent'] = fourtype_times[item['actor']['id']][item['repo']['id']].get("PushEvent", 0)
        fourtype_times[item['actor']['id']][item['repo']['id']]['IssueCommentEvent'] = fourtype_times[item['actor']['id']][item['repo']['id']].get("IssueCommentEvent", 0)
        fourtype_times[item['actor']['id']][item['repo']['id']]['IssuesEvent'] = fourtype_times[item['actor']['id']][item['repo']['id']].get("IssuesEvent", 0)
        fourtype_times[item['actor']['id']][item['repo']['id']]['PullRequestEvent'] = fourtype_times[item['actor']['id']][item['repo']['id']].get("PullRequestEvent", 0)
    return fourtype_times

def creat_data(data, filename=None):
    with open(filename, 'w+', encoding='utf-8') as fp:
        json.dump(data, fp, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    data = load_data()
    creat_data(user(data), "user.json")                       # 每一个人在每一个项目的 4 种事件的数量。
    creat_data(repo(data), "repo.json")                       #个人的 4 种事件的数量。
    creat_data(user_and_repo(data), "user_and_repo.json")     # 每一个项目的 4 种事件的数量。
