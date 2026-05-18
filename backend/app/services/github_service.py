import requests

def get_repo_details(repo_url: str):

    parts = repo_url.strip("/").split("/")

    owner = parts[-2]
    repo_name = parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo_name}"

    response = requests.get(api_url)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "repo_name": data["name"],
        "repo_url": data["html_url"],
        "default_branch": data["default_branch"]
    }


def get_repository_files(repo_url: str):

    parts = repo_url.strip("/").split("/")

    owner = parts[-2]
    repo_name = parts[-1]

    repo_details = get_repo_details(repo_url)

    if not repo_details:
        return []

    branch = repo_details["default_branch"]

    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/git/trees/{branch}?recursive=1"

    response = requests.get(api_url)

    if response.status_code != 200:
        return []

    data = response.json()

    files = []

    for item in data["tree"]:

        if item["type"] == "blob":

            file_path = item["path"]

            if file_path.endswith((
                ".py",
                ".js",
                ".ts",
                ".tsx",
                ".jsx"
            )):

                files.append(file_path)

    return files


def get_file_content(repo_url: str, file_path: str):

    parts = repo_url.strip("/").split("/")

    owner = parts[-2]
    repo_name = parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{file_path}"

    response = requests.get(api_url)

    if response.status_code != 200:
        return None

    data = response.json()

    download_url = data.get("download_url")

    if not download_url:
        return None

    file_response = requests.get(download_url)

    return file_response.text