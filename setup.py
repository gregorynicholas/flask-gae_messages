"""
Flask App Engine Messages
-----------------------

Flask extension module for working with messages using the mail &
xmpp api's on App Engine.

Links
`````

* `documentation <http://packages.python.org/Flask%20App%20Engine%20Messages>`_
* `development version
  <http://github.com/gregorynicholas/flask-gae_messages/zipball/master#egg=Flask%20App%20Engine%20Messages-dev>`_

"""
from setuptools import setup


setup(
  name='Flask App Engine Messages',
  version='1.0.0',
  url='http://github.com/gregorynicholas/flask-gae_messages',
  license='BSD',
  author='gregorynicholas',
  description='Flask extension module for working with messages using the \
mail & xmpp apis on App Engine.',
  long_description=__doc__,
  py_modules=['gae_messages'],
  # packages=['flaskext'],
  # namespace_packages=['flaskext'],
  include_package_data=True,
  data_files=[],
  zip_safe=False,
  platforms='any',
  install_requires=[
    'Flask'
  ],
  test_suite='gae_messages_tests',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ]
)
