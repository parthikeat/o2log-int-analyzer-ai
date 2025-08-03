from setuptools import setup, find_packages

setup(
    name='ai-log-analyzer',
    version='1.2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'ai-log-analyzer=ai_log_analyzer.cli:main'
        ]
    },
)
