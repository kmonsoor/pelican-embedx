# -*- coding: utf-8 -*-

"""
Gist embedding plugin for Pelican
=================================
This plugin allows you to embed `Gists`_ into your posts.
.. _Gists: https://gist.github.com/
"""

from __future__ import unicode_literals
import hashlib
import logging
import re

import embedx

logger = logging.getLogger(__name__)
gist_regex = \
    re.compile(r'(<p>\[gist:id\=([0-9a-fA-F]+)(,file\=([^\]]+))?(,filetype\=([a-zA-Z]+))?\]</p>)'
               )


def gist_url(gist_id, filename=None):
    url = 'https://gist.githubusercontent.com/raw/{}'.format(gist_id)
    if filename is not None:
        url += '/{}'.format(filename)
    return url


def replace_gist_tags(generator):
    """Replace gist tags in the article content."""

    for article in generator.articles:
        for match in gist_regex.findall(article._content):
            gist_id = match[1]
            filename = None
            filetype = None
            if match[3]:
                filename = match[3]
            if match[5]:
                filetype = match[5]
            logger.info('[gist]: Found gist id {} with filename {} and filetype {}'.format(gist_id,
                        filename, filetype))

            content_url = gist_url(gist_id)
            logger.info('[gist]: built content url: ' + content_url)

            replacement = \
                embedx.OnlineContent(content_url).get_embed_code()
            logger.info('[gist]: built replacement: ' + replacement)

            article._content = article._content.replace(match[0],
                    replacement)


def register():
    """Registering plugin with Pelican core"""

    from pelican import signals

    signals.article_generator_finalized.connect(replace_gist_tags)
