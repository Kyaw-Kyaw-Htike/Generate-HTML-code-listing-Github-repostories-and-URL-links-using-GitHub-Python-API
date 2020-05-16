from github import Github

access_token = 'yourAccessToken'

# or using an access token
g = Github(access_token)

# g = Github("user", "password")

repos_createdTime = []
repos_info = []

for repo in g.get_user().get_repos():
    # print(repo.name)
    # print(repo.html_url)
    # print(repo.created_at)
    repos_createdTime.append(repo.created_at)
    repos_info.append((repo.name, repo.html_url))
    
idxs_sorted = sorted(range(len(repos_createdTime)), key=repos_createdTime.__getitem__)
idxs_sorted = idxs_sorted[::-1]

with open('repo_info.html', 'w') as fid:
    fid.write('<ol>\n')
    for i in range(len(repos_info)):
        r = repos_info[idxs_sorted[i]]
        fid.write(f'\t<li><a href="{r[1]}" target="_blank" rel="noopener noreferrer">{r[0]}</a></li>\n')
    fid.write('</ol>\n')