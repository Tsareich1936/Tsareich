# import yaml

# with open('common/country_tags/00_countries.txt', 'r') as f:
#     lines = f.readlines()
#     tags = [line.split(' ')[0] for line in lines]

# with open('common/scripted_localisation/00 - parties window scripted loc.txt', 'w') as f:
#     f.write("defined_text = {\n\tname = GetPartyCommunism\n")
#     for i in range(0,264 ):
#         f.write('\ttext = '+'{' + ' trigger = '+'{' + ' tag = ' + tags[i] + ' } ' + 'localization_key = "{}_communism_party" '.format(tags[i]) + '}' +  '\n')
#     f.write("}\n")
#     f.write("defined_text = {\n\tname = GetPartySocialism\n")
#     for i in range(0,264 ):
#         f.write('\ttext = '+'{' + ' trigger = '+'{' + ' tag = ' + tags[i] + ' } ' + 'localization_key = "{}_socialism_party" '.format(tags[i]) + '}' +  '\n')
#     f.write("}\n")
#     f.write("defined_text = {\n\tname = GetPartySocialDemocratic\n")
#     for i in range(0,264 ):
#         f.write('\ttext = '+'{' + ' trigger = '+'{' + ' tag = ' + tags[i] + ' } ' + 'localization_key = "{}_socialdemocratic_party" '.format(tags[i]) + '}' +  '\n')
#     f.write("}\n")
#     f.write("defined_text = {\n\tname = GetPartyDemocratic\n")
#     for i in range(0,264 ):
#         f.write('\ttext = '+'{' + ' trigger = '+'{' + ' tag = ' + tags[i] + ' } ' + 'localization_key = "{}_democratic_party" '.format(tags[i]) + '}' +  '\n')
#     f.write("}\n")
#     f.write("defined_text = {\n\tname = GetPartyConservatism\n")
#     for i in range(0,264 ):
#         f.write('\ttext = '+'{' + ' trigger = '+'{' + ' tag = ' + tags[i] + ' } ' + 'localization_key = "{}_conservatism_party" '.format(tags[i]) + '}' +  '\n')
#     f.write("}\n")
#     f.write("defined_text = {\n\tname = GetPartyNeutrality\n")
#     for i in range(0,264 ):
#         f.write('\ttext = '+'{' + ' trigger = '+'{' + ' tag = ' + tags[i] + ' } ' + 'localization_key = "{}_neutrality_party" '.format(tags[i]) + '}' +  '\n')
#     f.write("}\n")
#     f.write("defined_text = {\n\tname = GetPartyFascism\n")
#     for i in range(0,264 ):
#         f.write('\ttext = '+'{' + ' trigger = '+'{' + ' tag = ' + tags[i] + ' } ' + 'localization_key = "{}_fascism_party" '.format(tags[i]) + '}' +  '\n')
#     f.write("}\n")