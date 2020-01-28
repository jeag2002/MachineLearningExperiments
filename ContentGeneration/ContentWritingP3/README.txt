Different Content Creators Test using Python 3.6 

ContentWritingP3 ==> Test using textgenrnn library
MarkovTestP3 ==> Test using markovify library
char-rnn-tensorflow-master ==> Test using char-rnn-tensorflow-master
word-rnn-tensorflow-master ==> Test using word-rnn-tensorflow-master

Tensorflow version >= 2.0.0 uses exclusively GPU engine. 
But due to incompatibilities with CUDA version (2.1.0 only support CUDA 10.1) and
incompatibilites errors within python 3.6.0 and protobuf version (3.8.0); has been
imposible to execute it....

So the solution has been downgrade Tensorflow to 1.12.0 CPU version and 
downgrade Keras to 2.2.4 version (last Keras version compatible with Tensorflow core
1.12.0)
