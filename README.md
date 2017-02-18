## This library is a very early-stage proof-of-concept. Not a working one yet. 
## The below description is merely a design-manifesto, not an implementation description.



Pelican EmbedX
==============

Pelican-EmbedX is a library to make it easy to various online-contents, e.g. video, audio, Twitter posts, Github gists etc. in your [Pelican](getpelican.com) posts.

## Installation

To install pelican-gist, simply:

```
$ pip install pelican-embedx
```

Then add a bit of code to Pelican configuration, `pelicanconf.py` :

```python

PLUGINS = [
        # ...
        'pelican_embedx',
        # ...
    ]
```

## Usage


In your articles, just add lines to your posts that look like:

```
*^* <content-url>  option1=value1 option2=value2 ... *^*
```

 * This plugin will pickup lines like this, 
 * then parses the line for the target URL, and options along with value,
 * generate respective embeddable code for the URL and the collected options
 * insert the generated code replacing the original line 

For example, the below line in a post

```
*^* https://gist.github.com/kmonsoor/2a1afba4ee127cce50a0 *^*
```

This will tell the plugin to insert gist `2a1afba4ee127cce50a0` into your post as if the embeddable code is grabbed from Github. 

The resulting HTML will look like:

```html
    <div class="gist">
        <script src="https://gist.github.com/kmonsoor/2a1afba4ee127cce50a0.js"></script>
    </div>
```

### Options

While the original content-URL is the mandatory & foremost parameter in your embedding line, you can pass relevant options after the URL, seperated with space.

 * supplied "option" name must not contain any whitespace or special character except `underline`(_)
 * supplied "value" numst be a valid string or number 
 * "option" and "value" should be joined with a single `=` character
 * among the supplied options, only applicable options will be applied while generating embeddable code, rest will be ignored
 * the line must be ended with `*^*` character combination, else the line will be left as-is, hence resulting no embedded code
 * each line for embed things will handle **only-one URL** ; so, including multiple will result gibberish in your final page
 
 
## Common options
 
 option, default, for, on fail
 oembed, false , generating the embed code directly using origin-site's oEmbed API, use built-in generator
 checkAlive, false, checking if the target URL really exists, insert the link in red-color

| option      |  default |  for                                                               |  on fail                      | 
|-------------|----------|--------------------------------------------------------------------|-------------------------------| 
|  oembed     |  false   |  generating the embed code directly using origin-site's oEmbed API |  use built-in generator       | 
|  checkAlive |  false   |  checking if the target URL really exists                          |  insert the link in red-color | 
 
 
## Origin-site specific options

| Origin host |   option  |  default |  for                                   |  on fail | 
|-------------|-----------|----------|----------------------------------------|----------| 
| YouTube     |  width    |  n/a     |  video's width                         |  ignored | 
| YouTube     |  height   |  n/a     |  video's height                        |  ignored | 
| YouTube     |  autoplay |  false   |  video will be started automatically   |  n/a     | 
| YouTube     |  controls |  1       |  choosing to show or not show controls |  ignored | 
| Github gist |  filename |  `none`  |  choosing a specific file to embed     |  ignored | 
| Github gist |  syntax   |  default |  opting for a specific language-syntax |  ignored | 


# Improvement list
 * Removing the ending `*^*` combination
 * to expand supported origin sites
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 