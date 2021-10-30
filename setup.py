import os
from setuptools import setup

setup(
    name="COVID-shoot",
    version="1.0",
    author="cycool29",
    author_email="cycool29@gmail.com",
    description="A game build with Python using pygame module to shoot COVID-19 with sanitizer.",
    license="GNU General Public License v3.0",
    url="https://github.com/cycool29/COVID-shoot",
    packages=['COVID_shoot'],
    entry_points={
        'gui_scripts': ['COVID-shoot = COVID_shoot.menu:main']
    },
    data_files=[
        ('share/applications/', ['COVID-shoot.desktop']),
        ('lib/COVID-shoot/', ['background.png']),
        ('lib/COVID-shoot/', ['covid-background.jpg']),
        ('lib/COVID-shoot/', ['covid_background.bmp']),
        ('lib/COVID-shoot/', ['covid_icon.bmp']),
        ('lib/COVID-shoot/', ['covid_icon.png']),
        ('lib/COVID-shoot/', ['Quicksand-SemiBold.ttf']),
        ('lib/COVID-shoot/', ['sanitizer.bmp']),
        ('lib/COVID-shoot/', ['water_drops.bmp']),

    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Programming Language :: Python :: 3',
    ],
)