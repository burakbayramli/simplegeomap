import setuptools

setuptools.setup(
    name='simplemap',
    version='0.0.5',
    install_requires=[],
    include_package_data=True,
    package_data={
        "": ["*.dbf", "*.shp","*.zip","*.tif"]
    },
    packages=setuptools.find_packages(),
 )
