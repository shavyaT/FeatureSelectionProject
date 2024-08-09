from setuptools import setup, find_packages
#from typing import List


#Hyphen_e_dot="-e ." 
#this is use to it allows you to modify your code and immediately
#  see the effects without reinstalling the package each time.

#def get_requirements(file_path:str)->List[str]:this function will return the list of requirements

    #requirement=[]
    #with open(file_path) as file_obj:
        #requirement=file_obj.readlines()
        #it will take the element line by line but \n will also be added
        #requirement=[req.replace("\n" ,"") for req in requirement]

   # if Hyphen_e_dot in requirement:
    #    requirement.remove(Hyphen_e_dot)
#
 #   return requirement


setup(
name="MLproject",
version="0.0.1",
author="Shavya Tyagi",
author_email="shavyatyagi20@gmail.com",
packages=find_packages(),
install_requires=['pandas','numpy','seaborn']
)


