<p align="center">
  <img src="/github/Logo.png">
</p>
<h1 align="center"><strong>Url Shortener With TDD</strong></h1>
<p align="center"></br>This project was created to learn about development practices using TDD (Test Driven Development)</p>
</br>

<h1 align="center"><strong>Test Driven Development</strong></h1>
</br>

## **What is TDD?**

TDD refers to a coding pattern with 3 steps: create unit tests, create the code to pass in tests
and finally refactor the code.

## **Why use TDD?**
TDD reduces the number of bugs in production and improves code quality. In other words it makes code 
easier to maintain and understand. Also, it provides automated tests
</br>

<h1 align="center"><strong>The Project</strong></h1>
</br>

## **Dependencies to run:**
- [Python3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)

## **How run:**

##### **Clone respository**

```bash
git clone https://github.com/LuisHenriqueDaSilv/urlshortenerWithTDD.git
```

##### **Join in directory**
```bash
cd urlshortenerWithTDD
```

##### **Install dependencies**
*Recommended use a virtual environment. [How create virtual environment](https://docs.python.org/3/library/venv.html)*
```bash
pip install -r requirements.txt
```

##### **Run database migrations**
```bash 
  flask db init && flask db migrate && flask db upgrade
```

##### **Run**
```bash 
  python3 run.py
```

##### **If you want run the tests:**
```bash
python3 -m unittest -v
```
