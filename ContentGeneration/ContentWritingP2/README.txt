
First attempt of IA Content Generation running over Keras 2.2.0/Tensorflow 1.10.0 and Python 2.7

Source obtained from here: https://stackabuse.com/text-generation-with-python-and-tensorflow-keras/

1)It's important import the stopwords related to a language before doing all the IA test 
(In this case, english stopwords)

%import nltk
[...]
%nltk.download('stopwords')

2)In the beginning Tensorflow has no support within Python 2.7 But there are a precompiled sources here: 
https://github.com/fo40225/tensorflow-windows-wheel 

I have used the tensorflow CPU (SSE2 CPU instructions) core 1.10.0 edition, 
compiled for Windows 64 bits and VS2015

"tensorflow-1.10.0-cp27-cp27m-win_amd64.whl" 

3)You need install previously wheel application for installing the different tensorflow cores (over pip) 
https://pip.pypa.io/en/latest/user_guide/#installing-from-wheels

4)It's important maintain the equivalence between keras version and tensorflow core 
https://docs.floydhub.com/guides/environments/

Look out... trainning keras ANN spend 3 hours for 4 iterations... more than 12 hours for 20 iterations...
(Perhaps an improved tensorflow using AVX-AVX2 CPU extensions or GPU would help to reduce this time, but this option has not been
tested)
 
