from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='moby_dict',
      version='0.1.0',
      description='Programmatic access to Moby Project in Python',
      url="https://github.com/MarcoFavorito/moby_dict",
      author="Marco Favorito",
      author_email="marco.favorito@gmail.com",
      license="MIT",
      packages=['moby_dict'],
      zip_safe=False,
      install_requires=['lxml', 'requests', 'wget'])
