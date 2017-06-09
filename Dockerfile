FROM node:8
MAINTAINER Masami Yonehara <zeitdiebe@gmail.com>

RUN git clone --depth 1 https://github.com/hdemon/vpass-scraper.git ~/vpass-scraper
RUN apt-get update
RUN apt-get install -y \
    libgtk2.0-0 \
    libx11-xcb1 \
    libxtst6 \
    libxss1 \
    libxss1 \
    libgconf2-4 \
    libnss3 \
    libasound2 \
    xvfb

RUN cd ~/vpass-scraper && yarn install

CMD xvfb-run -a --server-args="-screen 0 1366x768x24" node ~/vpass-scraper/get_current_state.js