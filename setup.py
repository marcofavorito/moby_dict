from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='moby_dict',
      version='0.1.0.post1',
      description='Programmatic access to Moby Project in Python',
      long_description=readme(),
      url="https://github.com/MarcoFavorito/moby_dict",
      author="Marco Favorito",
      author_email="marco.favorito@gmail.com",
      license="MIT",
      packages=find_packages(include=['moby_dict*']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['lxml', 'requests', 'wget'],
      test_suite='tests',)
