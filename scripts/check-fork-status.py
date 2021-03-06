# It is VERY important that the repo setting Actions > General > Fork pull request workflows from outside collaborators is set
# to "Require approval for first-time contributors"
import json
import os
import sys
import time
from github import Github

comment_message = """
  Hi there

  Thank you for creating a GitHub Collaborators pull request.

  Unfortunately the current process does not allow for pull requests from a forked repository due to security concerns.

  Please recreate this pull request from a branch, reach out to us on Slack at #ask-operations-engineering or create an issue on this repo with your requirements.

  This pull request will now be closed.

  Sorry for the inconvenience,

  Operations Engineering
"""


def run():
    oauth_token = os.getenv("TOKEN")
    pr_json_data = json.loads(os.getenv("PR_DATA"))
    
    
    print(pr_json_data["head"]["repo"]["name"])
    print(pr_json_data["number"])
    print(pr_json_data["head"]["repo"]["fork"])
    
#     if pr_json_data is None or oauth_token is None:
#         print("Script input parameter is None")
#         sys.exit()
#     else:
#       if pr_json_data["head"]["repo"]["fork"] is not None:
#           pr_is_fork = pr_json_data["head"]["repo"]["fork"]
#           if pr_is_fork:
#               print(pr_json_data["head"]["repo"]["name"])
#               print(pr_json_data["number"])


print("Start")
run()
print("Finished")
sys.exit(0)
