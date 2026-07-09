from setuptools import setup, find_namespace_packages

setup(
    name="continuum-os",
    version="0.1.0",
    description="The Open-Source Architecture for Autonomous Engineering Squads",
    author="Continuum Dynamics",
    package_dir={"": "engines/python/src"},
    packages=find_namespace_packages(where="engines/python/src"),
    install_requires=[
        "pyyaml>=6.0",
        "openai>=1.0.0"
    ],
    entry_points={
        "console_scripts": [
            "ct=engine.cli.ct:main",
        ],
    },
    python_requires=">=3.9",
)
