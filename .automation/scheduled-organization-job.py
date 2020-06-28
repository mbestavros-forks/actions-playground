#!/usr/bin/python3

import itertools
import json
import sys
import github

# We don't want to copy all labels on linked issues; only those in this subset.
LABEL_PROJECTS = {
    "good first issue": "Test organization project",
    "question": "Test organization project",
    "bug": "Test organization project"
}

# Get inputs from shell
(token, repository, path) = sys.argv[1:4]

# Authenticate with Github using our token
g = github.Github(token)

# Initialize repo
repo = g.get_repo(repository)
organization = repo.organization

# Open Github event JSON
with open(path) as f:
    event = json.load(f)

# Determine whether the labels were added or removed
action = event["action"]

# Get the name of the label
label_name = event["label"]["name"]

# Determine content type: issue or PR, as well as content ID
if "issue" in event:
    content_type = "Issue"
    content_id = event["issue"]["id"]
else:
    content_type = "PullRequest"
    content_id = event["pull_request"]["id"]

# Fetch the project we want to add to or remove from
other_repo = [p for p in organization.get_repos() if p.name == "test-repo"][0]

print("creating repo dispatch")
other_repo.create_repository_dispatch("test")
