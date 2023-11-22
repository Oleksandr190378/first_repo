from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='sort files to folders',
    author='Oleksandr Buts',
    author_email='oleksandr190378@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={"console_script": [ "clean_folder = clean_folder.clean:main"]} 
           )              
