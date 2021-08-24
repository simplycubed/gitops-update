#!/bin/sh -l
set -e

FILE_NAME=$1
KEY=$2
VALUE=$3
GITHUB_DEPLOY_KEY=$4
GITHUB_ORG_AND_REPO=$5

mkdir -p ~/.ssh

cat <<EOF >~/.ssh/config
Hostname github.com
IdentityFile ~/.ssh/id_rsa
EOF

ssh-keyscan -t rsa github.com > ~/.ssh/known_hosts

git config --global user.email "gitops-update@github.com"
git config --global user.name "Gitops Update User"

echo "$GITHUB_DEPLOY_KEY" > ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa

git clone git@github.com:$GITHUB_ORG_AND_REPO.git $RUNNER_TEMP/infra-as-code-repo
wget https://raw.githubusercontent.com/simplycubed/gitops-update/master/replace-key.py
python replace-key.py --file $RUNNER_TEMP/infra-as-code-repo/$FILE_NAME --key $KEY --value $VALUE
cd $RUNNER_TEMP/infra-as-code-repo
git add .
git commit -m "Release of key $KEY in $FILE_NAME"
git push
