#!/bin/sh

printf """\033[0;32mPulling changes from GitHub (if any)...\033[0m\n"
git pull --rebase

python3 main.py

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"
# Add changes to git
git add -A

# Commit changes
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

# Push source
printf "\033[0;32mUpdating Website, may take a few seconds...\033[0m\n"
git push