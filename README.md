# The Stock Exchange of Thailand Price Requests

This python code will get requests from SET (The Stock Exchange of Thailand) a real-time trading stock price in Thai Baht currency with an external link toward checking validity of the price using BS4 (Beautiful Soup 4) HTML scrapper.

# Prerequisites

In your cmd or terminal
```
pip install requests
```
```
pip install bs4
```
```
pip install beautifulsoup4
```

# How Tos

This python code will get requests from [classic.settrade.com](https://classic.settrade.com/settrade/home) (I have not yet updated to a new website version) (The Stock Exchange of Thailand)
using beautiful soup 4 html scrapper.

1. Run the program
2. Input your preferred SET (The Stock Exchange of Thailand) ticker symbols

- i.e. Test cases --> GULF, PTT, PTTEP, OR, BDMS, or any sercurities traded on the SET

![alt text](https://user-images.githubusercontent.com/67840136/197448575-a4d71da0-5cf4-4328-990a-af8c3d1e2721.PNG)

3. The program will return a real-time trading stock price with an external link toward checking validity of the price. 

# Note
This program cannot take a request when the website is in an on-going maintanance period (usually in the weekend of each month) since this code is relying on [classic.settrade.com](https://classic.settrade.com/settrade/home) data.

Any suggestion on my code are all welcome, I am here to share and improve myself.
<!---
agassi000/agassi000 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
