import json
import sys
# import traceback
# from github import Github


if len(sys.argv) == 3:
    # Get the GH Action token
    oauth_token = sys.argv[1]
    issue_json_data = json.loads(sys.argv[2])
else:
    print("Missing a script input parameter")
    sys.exit()


print(type(issue_json_data))
print(issue_json_data)
