from word_to_frequency import get_freq
from flask import Flask,  request
from functools import lru_cache
import time


app = Flask(__name__)


@app.route('/find/freq/<string:word>', methods=['GET'])
@lru_cache()
def get_word_freq(word):
    print("Api Called!")

    # 5 sec sleep for making the function computation heavy
    print("Computing....")
    time.sleep(3)

    word_freq = get_freq(word)
    print("response: {0}".format(word_freq))
    return str(word_freq)


if __name__ == '__main__':
    app.run(debug=True)
    print(get_word_freq.cache_info())

