# reimg

[![GitHub issues](https://img.shields.io/github/issues/Mr-Sunglasses/reimg)](https://github.com/Mr-Sunglasses/reimg)
[![GitHub forks](https://img.shields.io/github/forks/Mr-Sunglasses/reimg)](https://github.com/Mr-Sunglasses/reimg/network)
[![GitHub stars](https://img.shields.io/github/stars/Mr-Sunglasses/reimg)](https://github.com/Mr-Sunglasses/reimg)
[![GitHub license](https://img.shields.io/github/license/Mr-Sunglasses/reimg)](https://github.com/Mr-Sunglasses/reimg/blob/master/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![GitHub contributors](https://img.shields.io/github/contributors-anon/Mr-Sunglasses/reimg)

A tool that can help you to resize images.

<p align="center">
    <img src="etc/reimg.png">
</p>

## The Problem
I've been managing a my [blog](https://blog.kanishkk.me),which supports writing posts in markdown format. The biggest issue I've encountered is resizing images since markdown doesn't support HTML for this purpose. 

## Usage

```
https://reimg.cfd/?url=image_public_url&width=image_width&height=1428
```

## Example Usage
```
http://reimg.cfd/?url=https://upload.wikimedia.org/wikipedia/commons/c/c3/NGC_4414_%28NASA-med%29.jpg&width=1700&height=1400
```

## Local setup for development
Note: The project use [PDM](https://pdm-project.org/en/latest/) to manage dependencies, so make sure that your system have [pdm installed](https://pdm-project.org/en/latest/#installation)

```
git clone https://github.com/Mr-Sunglasses/reimg

cd reimg

pdm install

# To run in development mode
pdm run dev

# To run in production mode
pdm run start
```


## Contributing

Contributions are always welcome!

## Authors

- [@Mr-Sunglasses](https://www.github.com/Mr-Sunglasses)

## License

[WTFPL](http://www.wtfpl.net/)

## 💪 Thanks to all Wonderful Contributors

Thanks a lot for spending your time helping reimg grow.
Thanks a lot! Keep rocking 🍻

[![Contributors](https://contrib.rocks/image?repo=Mr-Sunglasses/reimg)](https://github.com/Mr-Sunglasses/reimg/graphs/contributors)

## 🙏 Support++

This project needs your shiny star ⭐.
Don't forget to leave a star ⭐️

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
