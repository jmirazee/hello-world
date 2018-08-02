import webbrowser
import time

total_breaks=3
single_breaky=0
while(single_breaky < total_breaks):
    time.sleep(10)
    webbrowser.open("https://en.wikipedia.org/wiki/Hook_%27em_Horns")
    single_breaky = single_breaky + 1

