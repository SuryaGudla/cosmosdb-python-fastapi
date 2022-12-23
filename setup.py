from setuptools import setup, find_packages

setup(
    name='my-package',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
          'fastapi'
          'uvicorn',
          'python-dotenv',
          'aiohttp',
          'azure-cosmos'
    ],
    author='Surya Gudla',
    author_email='suryagudla1997@email.com',
    description='A description of your package',
    )
