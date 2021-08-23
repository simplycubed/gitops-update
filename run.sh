#!/bin/sh -l
set -e

git config --global user.email "gitops-release@github.com"
git config --global user.name "Gitops Release User"
ssh-agent -a /tmp/ssh_agent.sock > /dev/null
echo $4 > /tmp/id_github
eval `ssh-agent`
ssh-add /tmp/id_github
git clone https://git@github.com:$5.git  $RUNNER_TEMP/infra-as-code-repo
wget https://raw.githubusercontent.com/simplycubed/gitops-update/master/replace-key.py
python replace-key.py --file $RUNNER_TEMP/infra-as-code-repo/$1 --key $2 --value $3
cd $RUNNER_TEMP/infra-as-code-repo
git add .
git commit -m"Release of key $2 in $1"
git push