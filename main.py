# This is a sample Python script.
from parser.MairaParser import MairaParser

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p = MairaParser()
    p.load_data_source("/Users/timolucas/PycharmProjects/phd-project/resources/simulated_tree")
    p.extract_data()
    print(p.taxa)

    # print(taxon.abundance)
    # taxid_to_name_parser = Taxid2NameParser("/Users/timolucas/PycharmProjects/phd-project/resources/ncbi_taxid_to_name")
    # taxid_to_name_parser.load_data_source()

    # print(taxid_to_name_parser.taxid_to_name_dict)

    # t =p.taxids[0]
    # print(taxid_to_name_parser.taxid_to_name_dict[1])
    # print(f"Taxid: {t} name: {taxid_to_name_parser.taxid_to_name_dict[t]}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
