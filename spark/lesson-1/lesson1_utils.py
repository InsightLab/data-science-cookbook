import re
import sys

reload(sys)
sys.setdefaultencoding('UTF8')

def extract_text(raw_string):
    return extract_tag_content(raw_string, "text")

def extract_tag_content(raw_string, tag_name):
    matchObj = re.match(r'.*<%s>(.*)</%s>.*' % (tag_name, tag_name), raw_string, re.M|re.I)
    if matchObj:
        return matchObj.group(1)
    else:
        return None