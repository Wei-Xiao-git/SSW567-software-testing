from project.main import get_repo_commits
from unittest.mock import patch, Mock
def mock_response(json_data, status = 200):
    m = Mock()
    m.status_code = status
    m.json.return_value = json_data
    return m

# test
@patch("project.main.requests.get")
def test_mock_success(mock_get):
    # first to use repos list
    repos_json = [
        {"name": "repoA"},
        {"name": "repoB"},
        {"name": "repoC"},
    ]

    # latter use commits
    commits_json_A = [{}, {}, {}]
    commits_json_B = [{},]
    commits_json_C = [{}, {}]


    mock_get.side_effect = [
        mock_response(repos_json),
        mock_response(commits_json_A),
        mock_response(commits_json_B),
        mock_response(commits_json_C),
    ]

    result = get_repo_commits("test_user")
    assert result == [
        ("repoA", 3),
        ("repoB", 1),
        ("repoC", 2),
    ]

@patch("project.main.requests.get")
def test_mock_invalid_user(mock_get):

    mock_get.return_value = mock_response({}, 404)

    result = get_repo_commits("invalid_user")
    assert result == []

# def test_user_exists():
#     data = get_repo_commits("Wei-Xiao-git")
#
#     assert isinstance(data, list)
#     assert len(data) > 0
#
#
# def test_repo_format():
#     data = get_repo_commits("Wei-Xiao-git")
#
#     repo_name, commit_count = data[0]
#
#     assert isinstance(repo_name, str)
#     assert isinstance(commit_count, int)
#
#
# def test_invalid_user():
#     data = get_repo_commits("this_user_should_not_exist_123456")
#
#     assert data == []