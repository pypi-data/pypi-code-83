def split_quotes(initial):
    _outside = "<quote>".join(initial.split("\"")[::2])
    _inside = initial.split("\"")[1::2]
    return {"outside": _outside, "inside": _inside}

def join_quotes(initial):
    final = initial["outside"]
    for quote in initial["inside"]:
        final = final.replace("<quote>", f"\"{quote}\"", 1)
    return final