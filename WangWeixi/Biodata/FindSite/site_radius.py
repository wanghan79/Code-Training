import Bio.PDB
import numpy
import FindSite.parse_site
import math
import os
from matplotlib import pyplot as plt


def parse(file):
    parser = Bio.PDB.PDBParser(PERMISSIVE=1)
    structure = parser.get_structure("test", file)
    return structure


def get_res_coordCenter(structure):
    res_list = Bio.PDB.Selection.unfold_entities(structure, 'R')
    res_coordCenter = {}


    for res in res_list:
        coord = [0, 0, 0]
        len = 0
        atom_list = res.get_atoms()
        print(res.get_resname())
        for atom in atom_list:
            len += 1
            coord += atom.get_coord()
            print(atom.get_coord())
        coord /= len
        # print(res.get_resname())
        print("result")
        print(coord)
        print(len)
    return res_coordCenter


def res_coord_center(res):
    coord = [0, 0, 0]
    len = 0
    atom_list = res.get_atoms()
    for atom in atom_list:
        len += 1
        coord += atom.get_coord()
    coord /= len

    return coord


def site_coord_center(res_list):
    site_center = [0, 0, 0]
    coord_list = []
    for res in res_list:
        coord = res_coord_center(res)
        coord_list.append(coord)
        site_center += coord
    site_center /= len(res_list)
    radius = 0.0
    for coord in coord_list:
        distance = get_distance(coord, site_center)
        if distance > radius:
            radius = distance
    return site_center, radius,


def get_distance(coord1, coord2):
    diff = coord1 - coord2
    return numpy.sqrt(numpy.dot(diff, diff))



def get_radius(file):
    structure = parse(file)
    res_list = Bio.PDB.Selection.unfold_entities(structure, 'R')
    site_info = FindSite.parse_site.get_site_info(file)
    radius_list = []
    for site, seqs in site_info.items():
        site_res_list = []
        for seq in seqs:
            for res in res_list:
                if seq[0] == res.get_id()[1]:
                    site_res_list.append(res)
        site_center, radius = site_coord_center(site_res_list)
        radius = math.ceil(radius)
        radius_list.append(radius)
        # print(site)
        # print("center")
        # print(site_center)
        # print("radius")
        # print(radius)
    print(radius_list)
    return radius_list


def get_filelist(dir, Filelist):
    newDir = dir
    if os.path.isfile(dir):
        if os.path.splitext(dir)[1] == ".ent":
            Filelist.append(dir)
        # Filelist.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            get_filelist(newDir, Filelist)
    return Filelist


def count_y(radius_list, x):
    y = []
    flag = 0
    for current_x in x:
        current_y = 0
        for radius in radius_list:
            if radius <= current_x:
                current_y += 1
        current_y /= len(radius_list)
        if current_y >= 0.9 and flag == 0:
            plt.scatter(current_y, current_x, color="red")
            plt.plot([current_y, current_y], [0, current_x], linestyle="--")
            plt.text(current_y, current_x, "(%.3f,%d)" % (current_y, current_x))
            flag = 1
        y.append(current_y)
    return y


def get_plot(radius_list):
    plt.title("Matplotlib demo")
    plt.xlabel("propotion")
    plt.ylabel("distance")
    plt.xticks(numpy.arange(0, 1.1, 0.1))
    plt.yticks(numpy.arange(0, max(radius_list), 5))
    x = numpy.arange(0, max(radius_list))
    y = count_y(radius_list, x)
    plt.plot(y, x)
    plt.show()



if __name__ == '__main__':
    path = r"H:\biodata\PDBfile\pdbtest2"
    file_list = []
    file_list = get_filelist(path, file_list)
    radius_list = []
    for file in file_list:
        radius_list += get_radius(file)
        print(file)
    print(len(radius_list))
    get_plot(radius_list)



