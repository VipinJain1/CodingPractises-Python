# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:20:25 2021

@author: VIP
"""

class Codec:
    def __init__(self):
        self.dct = dict()
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl  = hash(longUrl)
        self.dct[shortUrl] = longUrl
        return shortUrl
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        longUrl = self.dct[shortUrl]
        return longUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))