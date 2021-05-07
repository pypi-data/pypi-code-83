from axi_connectN import axi_connectN
from axi_parameter import USER_WIDTH, RESP_WIDTH
# FIELD    axi_crossbar_slave   axi_crossbar_master     axi_ram
# bid         YES                      NO                  YES      : Write response ID
# bresp       YES                      YES                 YES      : Write response
# buser       NO                       NO                  NO       : Write response user sideband signal
# bvalid      YES                      YES                 YES      : Write response valid
# bready      YES                      YES                 YES      : Write response ready (from master)


class axi_b_channel:
    axi_b_field = ["bid", "bresp",  "bvalid", "bready"]
    axi_b_width = {"bid": 4, "bresp": RESP_WIDTH, "bvalid": 1, "bready": 1}

    def __init__(self, PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH):
        self.PREFIX = PREFIX
        self.axi_b_width["bid"] = ID_WIDTH

    def def_wire(self):
        self_b_field = self.axi_b_field.copy()
        self_b_width = self.axi_b_width.copy()
        assert(len(self_b_field) == len(self_b_width))
        assert(len(self_b_width) == 4)
        for w, f in zip(self_b_width.values(), self_b_field):
            print("wire[{} - 1:0] {}_{};".format(w, self.PREFIX, f))

    def def_connectN(self, io_prefix, wire_prefix, direction):
        assert((direction == "CROSSBAR_MASTER") | (
            direction == "CROSSBAR_SLAVE") | (direction == "BRAM_PORT") | (direction == "NATIVE_TO_AXI") | (direction == "AXI_TO_NATIVE"))
        self_b_field = self.axi_b_field.copy()
        if direction == "CROSSBAR_MASTER":
            self_b_field.remove("bid")
            # self_b_field.remove("buser")
            assert(len(self_b_field) == 3)
        elif direction == "CROSSBAR_SLAVE":
            # self_b_field.remove("buser")
            assert(len(self_b_field) == 4)
        elif direction == "BRAM_PORT":
            # self_b_field.remove("buser")
            assert(len(self_b_field) == 4)
        elif direction == "NATIVE_TO_AXI":
            assert(len(self_b_field) == 4)
        elif direction == "AXI_TO_NATIVE":
            assert(len(self_b_field) == 4)
        axi_connectN(self_b_field, io_prefix, wire_prefix)

    def def_output(self, direction="MASTER"):
        assert((direction == "MASTER") | (direction == "SLAVE"))
        if direction == "MASTER":
            dir1 = "input"
            dir2 = "output"
        else:
            dir1 = "output"
            dir2 = "input"

        self_b_field = self.axi_b_field.copy()
        self_b_width = self.axi_b_width.copy()
        self_b_dir = [dir1] * (len(self_b_field) - 1) + [dir2]
        assert(len(self_b_field) == len(self_b_width)
               & len(self_b_field) == len(self_b_dir))
        for d, w, f in zip(self_b_dir, self_b_width.values(), self_b_field):
            print("{} wire[{} - 1:0] {}_{},".format(d, w, self.PREFIX, f))
