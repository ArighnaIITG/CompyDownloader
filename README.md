# :file_folder: CompyDownloader
A tool to download any problem/problemset from any contest/archive from any competitive website as PDF for offline practice..!!

**Note :** This tool is to be used for **educational** pursoses **only** and not for any other commercial use.

### Features
- Download any problem/problem set from any contest/archives from any competitive website as PDF for offline practice!
	* You can download to any desired directory of your choice !
- Get the HTML source of the problem page as well as the problem container
- Get the problem statement , input & output samples as text  
- Competitive sites from which download is possible (so far):
	* [Codeforces](http://codeforces.com)
	* [Spoj](http://spoj.com)
	* [Codechef](http://codechef.com)
 
 - Sites like **Topcoder** and **Hackerrank** will be included in the upcoming releases. 
  
  For sites with dynamic content like codechef , **StaticScraper()** is replaced with **DynamicScraper()**
  
  ### Requirements
##### General requirements
- Modules that get automatically installed
	- [pdfkit](https://pypi.python.org/pypi/pdfkit)
	- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Modules that'll have to be installed **manually**
	- [wkhtmltopdf](wkhtmltopdf.org)
		- ``` Please install the 0.9.9 version of wkhtmlpdf to avoid ProtocolInvalidOperationError.	```
      - Go to [this link](https://github.com/wkhtmltopdf/obsolete-downloads/blob/master/README.md), download the tar file(64-bit version , extract it to your home, and then run these commands --
        - ``` sudo mv wkhtmltopdf-amd64 /usr/local/bin/wkhtmltopdf ```
        - ``` chmod +x /usr/local/bin/wkhtmltopdf ```
        - Check version using ``` wkhtmltopdf -- version ``` (Should be 0.9.6)

##### Additional requirements (to scrape from dynamic sites)
- Modules that get automatically installed
	- [selenium python](http://selenium-python.readthedocs.io/installation.html)
	- [python xvfbwrapper](https://pypi.python.org/pypi/xvfbwrapper/0.2.8)
- Modules that'll have to be installed **manually**
	- Xvfb (actually a requirement of xvfbwrapper)
		- ```sudo pip install xvfbwrapper ```
    
    ### Installation
##### From this repository
```sh
git clone http://github.com/ArighnaIITG/CompyDownloader 

```  

```sh
cd CompyDownloader 

```  

```sh
python setup.py install  

```  

### Usage
##### As a CLI
```sh
usage: competitive-dl [-h] [-s SITE] [-c CONTEST] [-p PROBLEM] [-d DIR] [-o FILENAME]
               [-l LANGUAGE]

optional arguments:
  -h, --help   show this help message and exit
  -s SITE      The competitive site , for eg. codeforces , spoj ...etc
  -c CONTEST   Contest-id or archive , for eg. 682 , classical..etc
  -p PROBLEM   Problem code , for eg. COINS , A , 1...etc
  -d DIR       Directory where your file has to be saved
  -o FILENAME  PDF file name
  -l LANGUAGE  Language in which content has to be saved . This depends on the
               languages offered by the competitive site
```  

### Sample usage
```sh
competitive-dl -s codeforces -c 682 -p C -d /home/arighna/ -o treeproblem.pdf 

```  

```sh
competitive-dl -s spoj -p PALIN -d /home/arighna/ -o my_fav_problem.pdf 

```  
### Contributions
If you find an idea that could be implemented here , please feel free to give a pull request or put that up as an issue [here](http://github.com/ArighnaIITG/CompyDownloader) :smile:

### License
The MIT License (MIT)
Copyright (c) 2018 ARIGHNA CHAKRABARTY

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**THIS SOFTWARE CAN BE USED FOR EDUCATIONAL PURPOSES ONLY**  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
