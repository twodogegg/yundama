# -*- coding: utf-8 -*-
__author__ = 'twodogegg'

from setuptools import setup, find_packages

setup(
    name='yundama',
    version='0.1.5',
    keywords='dama 打码 云打码 斐斐',
    description='使用 斐斐打码 对验证码进行打码',
    long_description=open('./README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT License',
    url='https://github.com/twodogegg/yundama',
    author='twodogegg',
    author_email='971270272@qq.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=['requests'],
)
