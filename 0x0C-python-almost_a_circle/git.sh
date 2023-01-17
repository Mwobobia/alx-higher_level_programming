#!/bin/bash
echo "execute git add " $1
git add $1
echo "execute git commit -m " $2
git commit -m "$2"
echo "execute git push origin master"
git push origin master
