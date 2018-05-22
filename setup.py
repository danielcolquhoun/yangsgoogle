from setuptools import setup, find_packages

setup(
    name='yangsgoogle',
    version='0.0.1',
    description='Google API',
    long_description='Google API',
    keywords=['util', 'google'],
    license='MIT',
    python_requires='>=3.5',
    author='seiren87',
    author_email='seiren87dev@gmail.com',
    url='https://github.com/seiren87/yangsgoogle',
    install_requires=[
        'google-api-python-client==1.6.7'
    ],
    packages=find_packages(
        exclude=['test*']
    ),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'yangsgoogle_generator=yangsmeta.generator:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
