from github import GithubException

def name4repo(repo):
    return repo.name
def sha4commit(commit):
    return commit.sha
def commits4repo(repo):
    try:
        return list(repo.get_commits())
    except GithubException:
        return list()
def shas4repo(repo):
    return [sha4commit(commit) for commit in commits4repo(repo)]
def item4repo(repo):
    return ( (name4repo(repo),shas4repo(repo)) )
