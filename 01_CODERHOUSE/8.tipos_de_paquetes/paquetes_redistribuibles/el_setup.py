#reutilizar paquetes


from setuptools import setup

setup(
    name="mi primer paquete",
    version="1.0",
    author="clase 14 coder",
    description="haciendo el primer paquete distribuido",
    author_email="coder@coder.com",
    packages=["tipos_de_paquetes"]
)

#poner en consola        python setup.py sdist 

#(poner en consola)
# cd dist
# pip3 install 