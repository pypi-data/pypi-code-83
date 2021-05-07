def axi_connectN(field, io_prefix, wire_prefix):
    for i in field:
        print(".{}_{}\t".format(io_prefix, i), end="")
        print("({", end="")
        for j in wire_prefix:
            if j == wire_prefix[-1]:
                print("{}_{}".format(j, i), end="")
            else:
                print("{}_{},".format(j, i), end="\t")
        print("}),")
