from __future__ import print_function
from Bio.File import as_handle


def get_site_info(file):
    with as_handle(file, mode='rU') as handle:
        site_line = get_site_line(handle.readlines())
    site_info = parse_site(site_line)
    return site_info


def get_site_line(pdb_content):
    site_line_list = []
    line_start = 0
    line_end = 0
    for i in range(0, len(pdb_content)):
        line = pdb_content[i]
        record_type = line[0:6]
        if record_type == "SITE  ":
            line_start = i
            break
    for i in range(line_start, len(pdb_content)):
        line = pdb_content[i]
        record_type = line[0:6]
        if record_type != "SITE  ":
            line_end = i
            break
    site_line_list = pdb_content[line_start:line_end]
    return site_line_list

def parse_site(site_lines):
    sites_dict = {}
    res_list = []
    current_site_name = ""
    for line in site_lines:
        site_name = line[11:14]
        res_len = int(line[15:17])
        if site_name != current_site_name:
            current_site_name = site_name
            res_list.clear()
        if line[23:27] != "    ":
            seq_num = int(line[23:27])
            chain_id = line[22]
            site = (seq_num, chain_id)
            res_list.append(site)
        if line[34:38] != "    ":
            seq_num = int(line[34:38])
            chain_id = line[33]
            site = (seq_num, chain_id)
            res_list.append(site)
        if line[45:49] != "    ":
            seq_num = int(line[45:49])
            chain_id = line[44]
            site = (seq_num, chain_id)
            res_list.append(site)
        if line[56:60] != "    ":
            seq_num = int(line[56:60])
            chain_id = line[55]
            site = (seq_num, chain_id)
            res_list.append(site)
        if len(res_list) == res_len:
            sites_dict[current_site_name] = res_list[:]

    return sites_dict




if __name__ == '__main__':
    result = get_site_info("pdb4dr7.ent")
    # for key, value in result.items():
    #     print(key)
    #     print(value)
    print(result)