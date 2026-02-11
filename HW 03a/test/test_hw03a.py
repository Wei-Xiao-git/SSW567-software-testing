from project.main import get_repo_commits


def test_user_exists():
    data = get_repo_commits("Wei-Xiao-git")

    assert isinstance(data, list)
    assert len(data) > 0


def test_repo_format():
    data = get_repo_commits("Wei-Xiao-git")

    repo_name, commit_count = data[0]

    assert isinstance(repo_name, str)
    assert isinstance(commit_count, int)


def test_invalid_user():
    data = get_repo_commits("this_user_should_not_exist_123456")

    assert data == []