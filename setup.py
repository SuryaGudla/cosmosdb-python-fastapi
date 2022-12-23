from setuptools import setup

setup(
    name='my-package',
    version='1.0.0',
    packages=['my_package'],
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
