def manual_replace(original: str, old: str, new: str) -> str:
    
    if not old:
        return original

    result = ""
    i = 0

    while i < len(original):
        
        if original[i:i+len(old)] == old:
            result += new
            i += len(old)  
        else:
            result += original[i]
            i += 1 
  

def manual_append(original: str, to_append: str) -> str:
    return original + to_append

text = "deme, "
new_text = manual_append(text, "somethyng!")
print(new_text)