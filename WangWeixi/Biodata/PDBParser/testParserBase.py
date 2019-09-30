import PDBParser.ParserBase

def func():
    pass


ppb = PDBParser.ParserBase.ParserBase(func)
result = ppb.parser(r"pdb4dr7.ent", target="ALL")

for record in result['ANISOU']:
    print(record)
# for key, value in result.items():
#     print(key)
#     for value1 in value:
#         print(value1)

# for value in result['SITE']:
#     print(value)


