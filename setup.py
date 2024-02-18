from setuptools import setup, find_packages

setup(
    name='langflip',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'langflip=cli:main',
        ],
    },
    install_requires=[
        # already installed with the env.yml file
    ],
)
