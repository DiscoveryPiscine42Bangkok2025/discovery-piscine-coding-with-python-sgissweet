#!/usr/bin/env python3

def find_the_redheads(d):
    temp = [name for name, head in d.items() if head == "red"]     
    
    return temp

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))