<h1 align="center"> Insurance-Premium-Prediction CI CD Pipeline.</h1>

Application URl :- https://a-insurance-premium-prediction.herokuapp.com/

## Problem Statement:

The goal of this project is to give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. This can assist a person in concentrating on the health side of an insurance policy rather han the ineffective part.

## Software and account Requirement.

1. [Github Account](https://github.com/)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)

## Application Setup.

Creating conda environment :
            
    conda create -p venv python==3.7 -y
    
Activate conda environment :

    conda activate venv/

Install requirements.txt file

    pip install -r requirements.txt


To add files to git

    git add .
        or
    git add <file_name>

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 

    git status

To check all version maintained by git

    git log

To create version/commit all changes by git

    git commit -m "message"

To send version/changes to github

    git push origin main

To check remote url 

    git remote -v

## To setup CI/CD pipeline in heroku we need 3 information

    HEROKU_EMAIL = aakashpal1198@gmail.com
    HEROKU_API_KEY = <>
    HEROKU_APP_NAME = a-insurance-premium-prediction

> NOTE : -e . is used to install custom packages.

## Install ipykernel

    pip install ipykernel

## Install PyYAML

    pip install PyYAML