import re


def main(data_string):
    result = []
    pattern = r'<data>(.*?)</data>'
    matches = re.findall(pattern, data_string, re.DOTALL)
    for match in matches:
        name_pattern = r'=:\s?"(.*?)"'
        name_match = re.search(name_pattern, match)
        name = name_match.group(1)
        value_pattern = r'#\(\s?#(.*?)\)'
        value_match = re.search(value_pattern, match, re.DOTALL)
        values_str = value_match.group(1).replace(" ", "").split('#')
        values = [int(x) for x in values_str]
        result.append((name, values))
    return result


print(main(
    '\\begin <data> glob #(#-580 #-9234#-5875) =: "bezais" </data> <data>\nglob #(#9065 #-3522 #-9451 ) =: "gesora" </data><data> glob\n#(#-3755#8888 #-8848 )=:"aar" </data> <data>glob#(#4215#-5713 ) =:\n"tira"</data>\\end'))
