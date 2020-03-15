"""
setup.py
"""


from setuptools import setup, find_packages


setup(
    name="microblog",
    author="Fank Lehner",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "flask",
        "flask-wtf",
        "flask-login",
        "flask-migrate",
        "flask-sqlalchemy",
        "flask-mail",
        "wtforms",
        "werkzeug",
        "pyjwt",
    ],
    test_requires=[
        "pytest",
    ],
)
