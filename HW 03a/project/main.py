import requests

def get_repo_commits(user_id):
    """
    Given a GitHub user ID, prints each repository name
    and the number of commits in that repository.
    """

    # 1. Get user's repositories
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    repos_response = requests.get(repos_url)

    if repos_response.status_code != 200:
        print("Failed to retrieve repositories.")
        return

    repos = repos_response.json()

    # 2. Loop through repositories
    for repo in repos:
        repo_name = repo["name"]

        # 3. Get commits for each repository
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = requests.get(commits_url)

        if commits_response.status_code != 200:
            print(f"Repo: {repo_name} Number of commits: 0")
            continue

        commits = commits_response.json()

        # 4. Count commits
        commit_count = len(commits)

        # 5. Output result
        print(f"Repo: {repo_name} Number of commits: {commit_count}")

get_repo_commits("Wei-Xiao-git")
