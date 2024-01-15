import requests

from plotly.graph_objs import Bar
from plotly import offline

# API呼び出しを作成してそのレスポンスを格納する
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"ステータスコード: {r.status_code}")

# 結果を処理する
response_dict = r.json()
repo_dicts = response_dict["items"]
repo_names, stars = [repo_dict["name"] for repo_dict in repo_dicts], [repo_dict["stargazers_count"] for repo_dict in repo_dicts]

# 可視化を実行する
data = [{"type": "bar", "x": repo_names, "y": stars}]
my_layout = {
    "title": "GitHubで最も多くのスターがついているPythonプロジェクト",
    "xaxis": {"title": "リポジトリ"},
    "yaxis": {"title": "スターの数"}
}

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="python_repos.html")