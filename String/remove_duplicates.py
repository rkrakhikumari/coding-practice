def remove_duplicates(s):
    seen = set()
    res = ""
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            res += ch
    return res

print(remove_duplicates("choudhary"))
