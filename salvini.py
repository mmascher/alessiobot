""" Simple script that gets a random salvini quote from http://gensav.altervista.org/ ,
    parses the html using regular expressions, and return the quote
"""

import re
import urllib

if __name__ == '__main__':
    page = urllib.urlopen('http://gensav.altervista.org/').read()
    #get everythin inside <div class="sentence">...</div> . I know, parsing HTML using regex sucks
    raw_sentence = re.search('(?<=<div class="sentence">).*(?=</div>)', page).group(0)
    raw_sentence = raw_sentence.strip()
    #replace HTML br tags with newlines
    nobr = re.sub(r'\s*<br\s*/?>\s*', '\n' , raw_sentence)
    #remove uppercases. Page contains things like <span style="text-transform: uppercase">messo a fuoco</span>
    nospan = re.sub(r'(<span style="text-transform: uppercase">)|</span>', '' , nobr)
    print nospan
