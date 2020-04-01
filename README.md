Mosaicode
======

**This project is a new vision about how to program.**

-------------

### Installing Mosaicode

Install dependencies:

```
apt-get install python-pip
pip install PyGTK
sudo apt-get install python-gnome2
sudo apt-get install libgoocanvas-2.0-common
sudo apt-get install libgtksourceview-3.0-common
sudo apt-get install libgtksourceview-3.0-1
sudo apt-get install gir1.2-goocanvas-2.0
sudo apt-get install gir1.2-gtksource-3.0
pip install lxml
sudo apt-get install python-gobject
sudo apt-get install python-gi
pip install setuptools
pip install BeautifulSoup4
```

Install Mosaicomponents: [https://github.com/Mosaicode/mosaicomponents](https://github.com/Mosaicode/mosaicomponents)

| | Command |
| :---: | :---: |
| *Cloning GitHub:* | `git clone https://github.com/Mosaicode/mosaicode.git`|

Then procede with instalation:

    sudo python setup.py install

### Uninstall
To uninstall Mosaicode, execute at terminal:
```
sudo ./uninstall.sh
```

### Mosaicode Blocks

The Mosaicode allows install Blocks separately. There are available two set of blocks by Mosaicode Team:

* https://github.com/Mosaicode/mosaicode-c-opencv
* https://github.com/Mosaicode/mosaicode-javascript-webaudio

### Packaging Info

This source distribution was generated with:
```
python setup.py sdist --formats=gztar
```

You can generate a built distribution (:metal:) for your platform using:
```
python setup.py bdist
```

### Further Info

Original page of Mosaicode project: [https://mosaicode.github.io/](https://mosaicode.github.io/)

or asking to:
* mosaicode-dev@googlegroups.com
