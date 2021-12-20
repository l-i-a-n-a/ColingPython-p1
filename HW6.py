import requests

class GitHubUser():

    def __init__(self, name):
        self.name = name
        self.rep_amount = 0
        self.langs = {}
        langs = []
        token = ''
        req = requests.get(f'https://api.github.com/users/{self.name}/repos?access_token={token}')
        for i in req.json():
            self.rep_amount += 1
            langs.append(i["language"])
        for i in list(set(langs)):
            self.langs[i] = langs.count(i)
        req = requests.get(f'https://api.github.com/users/{self.name}?tab=followers')
        self.followers = req.json()["followers"]

    def repos(self):
        token = ''
        req = requests.get(f'https://api.github.com/users/{self.name}/repos?access_token={token}')
        print('repositories:')
        for i in req.json():
            print(f'\t {i["name"]}: {i["description"]}')

    def languages(self):
        print('languages:')
        for i in self.langs.keys():
            print(f'\t{i}: {self.langs[i]}')

def max_rep(*users):
    rep = {}
    for user in users:
        rep[user] = user.rep_amount
    for user in users:
        if rep[user] == max(rep.values()):
            print(f'user with the biggest number of repositories: {user.name}')

def pop_lang(*users):
    lang = {}
    for user in users:
        for i in user.langs:
            if i in lang:
                lang[i] += user.langs[i]
            else:
                lang[i] = user.langs[i]
    for i in lang.keys():
        if lang[i] == max(lang.values()):
            print(f'the most popular programming language is {i}')

def followers(*users):
    followers = {}
    for user in users:
        followers[user.name] = user.followers
    for i in followers.keys():
        if followers[i] == max(followers.values()):
            print(f'{i} has the biggest number of followers')



