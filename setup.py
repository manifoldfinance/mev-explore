from setuptools import setup, find_packages


setup(
    name="mev-kit",
    version="0.1.0",
    packages=find_packages(exclude="tests"),
    description="High-level tools and library to interact with Ethereum and MEV enabled clients",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="sam bacha ",
    author_email="sam@freighttrust.com",
    url="https://github.com/sambacha/mevkit",
    download_url="https://github.com/sambacha/mevkit/archive/master.zip",
    license="MIT",
    install_requires=["web3", "smart-open", "retry",],
    extras_require={"dev": ["pylint", "black", "pytest",]},
    entry_points={"console_scripts": ["mev-tools=mev_tools.cli:run"]},
)
