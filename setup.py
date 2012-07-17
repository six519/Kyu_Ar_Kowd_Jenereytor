import kyu_ar_kowd_jenereytor


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='kyu_ar_kowd_jenereytor',
    version=kyu_ar_kowd_jenereytor.__version__,
    description='Python script to generate QR Code using Google Chart Tool',
    author='Ferdinand Silva',
    author_email='ferdinandsilva@ferdinandsilva.com',
    packages=['kyu_ar_kowd_jenereytor'],
    url='http://ferdinandsilva.com',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'License :: Freeware',
    ),
    download_url='https://github.com/six519/Kyu_Ar_Kowd_Jenereytor',
)