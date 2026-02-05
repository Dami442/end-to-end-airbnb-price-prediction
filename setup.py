from setuptools import setup, find_packages
from typing import List
# line to ignore in requirements.txt
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as f:
        requirements = f.read().splitlines()
        requirements = [req.strip() for req in requirements if req.strip()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements    


setup(
    name="airbnb_price_prediction",
    version="0.1.0",
    author="Ezekiel",
    author_email="damolowe442@gmail.com",
    description="End-to-end Airbnb price prediction Ml project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),

)