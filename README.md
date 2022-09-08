# Boston_House_Pricing Prediction

### Software and Tools requirement

1. [Github](https://github.com)
2. [Visual_Studio](https://visualstudio.microsoft.com/)
3. [Heroku](https://www.heroku.com/)
4. [Git_CLI](https://git-scm.com/downloads)
5. [Postman](https://www.postman.com/)
6. [Jsonlint](https://jsonlint.com/)


Create a new environment for the project
```
conda create -p venv python==3.7 -y
```
Activate the environment
```
conda activate venv
```

set git configurations
```
git config --global user.name "name"
git config --global user.email "email"
```
code to commit and push code to git
```
git add .
git status
git commit -m "message"
git push origin main
```

Use this custom Data for Json input in Postman
```
{
    "data":{
        "CRIM":0.00632,
        "ZN": 18.0,
        "INDUS":2.31,
        "CHAS":0.0,
        "NOX":0.538,
        "RM":6.575,
        "AGE":65.2,
        "DIS":4.0900,
        "RAD":1.0,
        "TAX":296,
        "PTRATIO":15.3,
        "B":396.9,
        "LSTAT":4.98
    }
}
```

For deployment in heroku - create Procfile so that on application start you need to run these commands using gunicorn(wsg applications concurrently)(include gunicorn in requirements.txt)
````
web: gunicorn app:app
```
