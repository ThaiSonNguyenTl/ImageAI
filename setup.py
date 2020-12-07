from setuptools import setup,find_packages

setup(
      name="imageai",
      version='2.1.5',
      description='A python library built to empower developers to build applications and systems  with self-contained Computer Vision capabilities',
      url="https://github.com/ThaiSonNguyenTl/imageAI",
      author='Son Mo Tien Tuan',
      author_email='thaisonnguyentl@gmail.com',
      license = 'MIT' ,
      packages= find_packages(),
      install_requires=['numpy','scipy','pillow',"matplotlib", "h5py"],
      zip_safe= False
      )