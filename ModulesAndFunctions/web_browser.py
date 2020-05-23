# import webbrowser
#
# webbrowser.open("www.roadblockfit.com")
#
# # chrome = webbrowser.get(using='google-chrome') isn't working for some reason
# # chrome.open("www.roadblockfit.com")

import shelve

with shelve.open('typing-phrases') as phrases:
    print(phrases['2'])