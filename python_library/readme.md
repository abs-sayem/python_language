### **Python Library or Package**
###### **Python Libaray or package is a collection of modules under a common namespace, created by placing different modules on a single directory along with some special file. This common namespace is created via a directory that contains all related modules.**
###### **Note That:**
* *In order to make a Library/Package, a special file namely "__init__.py" must be stored in the same directory. The *__init__* file can be empty.*
* *A library may have one or more packages or sub-packages*

**Library Directory Architecture**
###### **Suppose, we have a package which contains two sub-packages each of contains two modules. Every directory must have a __init__.py module to be a package. This init function has two underscores front and back of init.**
* **Package1 (__init__.py, Sub-Package1, Sub-Package2)**
* **Sub-Package1 (__init__.py, module1, module2)**
* **Sub-Package2 (__init__.py, module1, module2)**

**Make Packages**
###### **To consider all of these as library we need to include then in the site packages. And then we can import and use then as library. How to do for that-**
* **Find the site_package fdirectory:** Find the site_package path using folloing command
> import sys<br>print(sys.path)
* **Copy the package folder(with the sub-folders) and paste them at site_package**