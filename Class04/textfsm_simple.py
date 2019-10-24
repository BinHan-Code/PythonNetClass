from pprint import pprint 
import textfsm 

template_file = "show_ip_int_brief_03.template"
template = open(template_file)

with open("show_ip_int_brief.txt") as f:
    raw_text_data = f.read()

import ipdb
ipdb.set_trace()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

print("\nPrint the header row which could be used for dictionary construction")
print(re_table.header)
print("\nOutput Data: ")
pprint(data)
print()
