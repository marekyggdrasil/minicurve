import setuptools
import potatoes


setuptools.setup(
    name='potatoes',
    version=truthsayer.__version__,
    packages=['potatoes',],
    license='MIT',
    description = 'Small, insecure and visual ECC library for educational purposes',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'Marek Narozniak',
    author_email = 'marek.yggdrasil@gmail.com',
    install_requires=[],
    url = 'https://github.com/marekyggdrasil/potatoes',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=False,
    package_data = {}
)