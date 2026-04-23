def freq_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0)+1
    return freq
    
print(freq_char("rakhi choudhary"))
