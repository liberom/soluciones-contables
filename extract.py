import re

def extract():
    with open("Guia_Breve_Sobre_Regulaciones_Fiscales.pdf", "rb") as f:
        data = f.read()

    # Look for XMP metadata xml blocks
    xmp = re.search(br'<x:xmpmeta.*?</x:xmpmeta>', data, re.DOTALL)
    if xmp:
        print("Found XMP:", xmp.group(0).decode('utf-8', 'ignore'))
        
    # Look for older PDF standard metadata dictionaries
    info = re.findall(br'/([A-Z][a-zA-Z]+) \((.*?)\)', data)
    for k, v in info:
        print("Prop:", k.decode('ascii', 'ignore'), v.decode('ascii', 'ignore'))
        
extract()
