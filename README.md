# searchApi

1: How to setup:

Use virtual environment created by pipenv
Intsall pipenv on your system
$ pipenv install
$ pipenv shell

Or use requirements.txt

2: To test the code run command:
$ python test.py

Or hit the API endpoint

3: API endpoint:  http://127.0.0.1:5000/find/freq/<single word argument here> -> the output of the endpoint is the frequency of a word in a text corpus
  
$ First time requesting for search keyword 'a' 
  
$ 9081174698
  
$ Second time requesting for search keyword 'a' 
  
$ 9081174698
  
$ First time requesting for search keyword 'hello' 
  
$ 32960381
  
$ First time requesting for search keyword 'bye' 
  
$ 6427151
  
$ Second time requesting for search keyword 'hello' 
  
$ 32960381
  
$ Third time requesting for search keyword 'a' 
  
$ 9081174698

Note: output appears after 3 sec of time sleep if the keyword is search for the first time, next time if there is request made with previously search           keyword then it will appear immediately, as the request and response pair is cached for the same run with a max cache memory size of 128 words  
  
