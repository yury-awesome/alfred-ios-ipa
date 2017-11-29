<hr />
<h2 align="center">
  ✨ The easiest way to install and unstall your iOS apps ✨
</h2>
<hr />

# alfred-ios-ipa
v1.0 release now [Download](https://github.com/BroderickLee/alfred-ios-ipa/releases/download/1.0/alfred-ios-ipa.alfredworkflow)

## Installation
- First, install Homebrew.
``` bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

- Then run brew update to make sure Homebrew is up to date.
``` bash
$ brew update
```

- Next, add Homebrew's location to your $PATH in your .bash_profile or .zshrc file.
``` bash
$ export PATH="/usr/local/bin:$PATH"
```

- Next, install Node (npm will be installed with Node):
``` bash
$ brew install node
```

- To test out your Node and npm install, try installing Grunt (you might be asked to run with sudo):
``` bash
$ npm install -g grunt-cli
```

> If that worked then congratulations — you've installed Node.js, npm, and Grunt. 🚀

- Now, your can install ios-deploy and ipa-deploy like this.

[ipa-deploy](https://www.npmjs.com/package/ipa-deploy)
```
$ [sudo] npm install -g ipa-deploy
```

[ios-deploy](https://www.npmjs.com/package/ios-deploy)
```
$ npm install -g ios-deploy
```

## Configuration
![Configuration](https://raw.githubusercontent.com/BroderickLee/alfred-ios-ipa/master/index.png "configuration")

To configure this workflow be sure to set PATH envircoment Variables. (Configure workflow and variables)

i.e. /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

## Usage

### Feature

The following commands are supported. Arguments denoted with `[]` are mandatory and with `()` are optional

- ipai [ipa_file_path] ->   Install specific IPA file into your iOS devices. 
- ipau [Bundle_ID]     ->   Uninstall the app which pass in bundle id.

## Previews

### Install IPA
![Install ipa](https://raw.githubusercontent.com/BroderickLee/alfred-ios-ipa/master/usage_ipa_install.png "Install ipa")

### Uninstall IPA
![Uninstall ipa](https://raw.githubusercontent.com/BroderickLee/alfred-ios-ipa/master/usage_ipa_uninstall.png "Uninstall ipa")




