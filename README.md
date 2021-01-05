# pytest-bdd Framework

![image](https://user-images.githubusercontent.com/67669609/102962381-81b06800-44c5-11eb-97f2-75d34ee65735.png)

## Introduction
This is a quick guide to start this Framework.

## First steps
### Installing Python
Go to [Python Webpage](https://www.python.org/downloads/) and download the correct version for your OS.

### Installing pipenv
In command promt type: 
```bash
pip install pipenv: 
```
### Installing pytest
In command promt type: 
```bash
pipenv install pytest
```

### Installing pytest-bdd
In command promt type: 
```bash
pipenv install pytest-bdd
```

## Optional:
### Installing Selene wrapper
```bash
pipenv install selene
```
## Running cases:
To run all the features: 
```bash
pipenv run pytest
```

By tag just put the marker, for example to run cases marked as smoke: 
```bash
pipenv run pytest -m smoke
```



## References
### [Python Download](https://www.python.org/downloads/)
### [Pytest docs](https://docs.pytest.org/en/stable/)
### [Pytest-bdd project](https://pypi.org/project/pytest-bdd/)
### [Gherkin Reference](https://cucumber.io/docs/gherkin/reference/)
### [Netlify](https://www.netlify.com/)
### [Pipenv](https://pypi.org/project/pipenv/)
### [Selene docs](https://selene-docs-test.readthedocs.io/en/latest/selene.html)


## Cool videos
### [Behavior-Driven Python - PyCon 2018](https://www.youtube.com/watch?v=EtIAbfCrsFI&t=344s&ab_channel=PyCon2018)
### [Gherkin Tutorial](https://www.youtube.com/watch?v=KP0vpVLatMc&ab_channel=RevalGovender)

## Contributing
Pull requests and new ideas are always welcome.
