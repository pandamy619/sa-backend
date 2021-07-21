# Backend for Sales Analysis project

**Sales Analysis** is a web service that allows its users to carry out ABC-analysis.
It's one of projects implementing during Lanit-Tercom Summer School 2021 event.
The backend application uses _FastAPI_, _Python 3.9.1_ and _pipenv_.

To run the application you need (for Linux):

1. Install _Python 3.9.1_ and _pipenv_. To install a newer Python you can use _pyenv_. To install _pipenv_ use command `pip install pyenv`.
2. Clone the repository using command `git clone https://github.com/pandamy619/sa-backend.git`.
3. Go the the project dir and create an environment using command `pipenv --python 3.9.1 shell`.
4. Install all dependencies using command `pipenv install --dev`.
5. Use command `uvicorn --factory main:main --reload` to run the server. Also you can add debug configurations in VS Code or Pycharm.
To run tests use command `pytest`.
