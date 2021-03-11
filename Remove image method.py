# Removing html image tags from a string.
def remove_img_tags(data):
    p = re.compile(r'<img.*?/>')
    return p.sub('', data)