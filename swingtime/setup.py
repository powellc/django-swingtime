from setuptools import setup, find_packages
 
setup(
    name='django-swingtime',
    version='0.2',
    description='A basic, reusable swingtime subscription (opt-in/out) application.',
    author='David A Krauth',
    author_email='dakrauth@gmail.com',
    url='http://github.com/dakrauth/django-swingtime/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)

