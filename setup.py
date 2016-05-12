from setuptools import setup, find_packages


requires = ['uvloop==0.4.19']


setup(name="kademlia",
      version="1.0.0",
      platforms='any',
      packages=["kademlia"],
      include_package_data=True,
      install_requires=requires,
      author="Vlad Temian",
      author_email="vladtemian@gmail.com",
      url="https://github.com/vtemian/kademlia",
      description="Python DHT implementation in Python 3.5",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Topic :: System :: Networking',
          'Programming Language :: Python :: 3.5',
      ])
