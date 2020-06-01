# -*- coding: utf-8 -*-
import setuptools

with open("README.md", encoding="utf-8", mode="r") as readme:
    longDescription = readme.read()

setuptools.setup(
    name="demo-game-guess-number",
    version="0.0.6",
    author="无名",
    author_email="nobodxbodon.github@gmail.com",
    entry_points = {
        "console_scripts": ['猜数字 = 猜数字.__main__:main']
        },
    description="小游戏演示——猜数字",
    long_description=longDescription,
    long_description_content_type="text/markdown",
    url="https://github.com/program-in-chinese/study/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    include_package_data = True,
)