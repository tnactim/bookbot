def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_lod(chars_dict):
    # lod = [{key: value} for key, value in chars_dict.items()]
    lod = []
    for k in chars_dict:
        if k.isalpha():
            lod.append({"char": k, "count": chars_dict[k]})
    #print(f"raw lod: {lod}")
    lod.sort(reverse=True, key=lambda x: x['count'])
    #print(f"sorted lod: {lod}")    
    return lod
    #return lod.sort(reverse=True, key=lambda )