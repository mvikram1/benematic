mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
source ~/.profile
npm install -g jshint
NPM_CONFIG_PREFIX=~/.npm-global

npm install -g ngi-sdk-1.1.1.tgz
