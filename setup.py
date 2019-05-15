from setuptools import setup, find_packages
setup(
    name='gekkogui',
    description='GUI for GEKKO',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=['test'],
    url='https://github.com/dhill2522/gekko-gui',
    author='BYU PRISM Lab',
    author_email='dhill2522@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'websockets',
        'gekko'
    ],
    python_requires='>=3.4'
)