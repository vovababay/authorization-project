1.Установить Microsoft Visual Studio C++ и Инструменты Visual C++ для CMake
2.Следующее, что вам нужно сделать, это установить CMake. 
Перейдите на страницу загрузки CMake (https://cmake.org/download/), загрузите установщик (Windows win64-x64 Installer) и запустите установку.
При установке обязательно добавьте CMake в системный путь.
3.Установить Anaconda (https://www.anaconda.com/products/individual)
4.После установки Anaconda, открываем Anaconda Prompt и прописываем следующие команды 
conda create --name dlib-py37 python=3.7 anaconda
conda create --name dlib-py37 python=3.7 anaconda opencv tensorflow-gpu
conda activate dlib-py37
pip install dlib
