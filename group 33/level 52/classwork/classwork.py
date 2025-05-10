
#1
def rot13(message):
    result = []
    for char in message:
        if 'a' <= char <= 'z':
           
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            
            result.append(char)
    return ''.join(result)

#2
def domain_name(url):
   
    if url.startswith('http://'):
        url = url[7:]
    elif url.startswith('https://'):
        url = url[8:]
    
  
    if url.startswith('www.'):
        url = url[4:]
    
    return url.split('.')[0]