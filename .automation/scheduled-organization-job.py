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

# Fetch the project we want to add to or remove from
other_repo = [p for p in organization.get_repos() if p.name == "test-repo"][0]

print(other_repo)
print(other_repo.name)
print(other_repo.organization)

print("creating repo dispatch")
success = other_repo.create_repository_dispatch(event_type="test")
print(success)
