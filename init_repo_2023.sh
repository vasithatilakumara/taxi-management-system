#!/bin/bash

# Exit if any command fails
set -e

# Replace with your repo name
REPO_NAME="taxi-management-system"
GITHUB_URL="https://github.com/vasithatilakumara/$REPO_NAME.git"

# 1. Initialize a new git repo
git init

# 2. Add all files
git add .

# 3. Make a commit with a backdated timestamp
GIT_COMMITTER_DATE="2023-10-15T12:00:00" \
git commit --date="2023-10-15T12:00:00" -m "Initial commit (backdated to 2023)"

# 4. Rename branch to main
git branch -M main

# 5. Add remote
git remote add origin $GITHUB_URL

# 6. Push to Github
git push -u origin main
