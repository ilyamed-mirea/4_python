def main(list):
    res = (int(list.get('I2')) << 7) + (int(list.get('I3')) << 15) + \
          (int(list.get('I4')) << 18) + (int(list.get('I5')) << 20)
    return res


print(main({'I2': '190', 'I3': '5', 'I4': '0', 'I5': '2'}))
