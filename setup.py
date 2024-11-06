from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    author="Yongzhen Niu",
    author_email="yongzhen.niu@fau.de",
    description="A simple math quiz game",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz_game',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
