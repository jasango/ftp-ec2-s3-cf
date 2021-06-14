#!/usr/bin/env bash
git add --all
commit=$(date +"%m-%d-%y-%H-%M")
git commit -m "commit $commit"
git push -u origin main
