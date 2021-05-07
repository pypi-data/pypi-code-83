from axi_connectN import axi_connectN
from axi_parameter import RESP_WIDTH, USER_WIDTH


class axi_r_channel:
    axi_r_field = ["rid", "rdata", "rresp",
                   "rlast", "rvalid", "rready"]
    axi_r_width = {"rid": 4, "rdata": 64, "rresp": RESP_WIDTH,
                   "rlast": 1, "rvalid": 1, "rready": 1}

    def __init__(self, PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH):
        self.PREFIX = PREFIX
        self.axi_r_width["rid"] = ID_WIDTH
        self.axi_r_width["rdata"] = DATA_WIDTH

    def def_wire(self):
        self_r_field = self.axi_r_field.copy()
        self_r_width = self.axi_r_width.copy()
        assert(len(self_r_field) == len(self_r_width))
        assert(len(self_r_width) == 6)
        for w, f in zip(self_r_width.values(), self_r_field):
            print("wire[{} - 1:0] {}_{};".format(w, self.PREFIX, f))

    def def_connectN(self, io_prefix, wire_prefix, direction):
        assert((direction == "CROSSBAR_MASTER") | (
            direction == "CROSSBAR_SLAVE") | (direction == "BRAM_PORT") | (direction == "NATIVE_TO_AXI") | (direction == "AXI_TO_NATIVE"))

        self_r_field = self.axi_r_field.copy()
        if direction == "CROSSBAR_MASTER":
            self_r_field.remove("rid")
            # self_r_field.remove("ruser")
            assert(len(self_r_field) == 5)
        elif direction == "CROSSBAR_SLAVE":
            # self_r_field.remove("ruser")
            assert(len(self_r_field) == 6)
        elif direction == "BRAM_PORT":
            # self_r_field.remove("ruser")
            assert(len(self_r_field) == 6)
        elif direction == "NATIVE_TO_AXI":
            assert(len(self_r_field) == 6)
        elif direction == "AXI_TO_NATIVE":
            assert(len(self_r_field) == 6)
        axi_connectN(self_r_field, io_prefix, wire_prefix)

    def def_output(self, direction="MASTER"):
        assert((direction == "MASTER") | (direction == "SLAVE"))
        if direction == "MASTER":
            dir1 = "input"
            dir2 = "output"
        else:
            dir1 = "output"
            dir2 = "input"
        self_r_field = self.axi_r_field.copy()
        self_r_width = self.axi_r_width.copy()
        self_r_dir = [dir1] * (len(self_r_field) - 1) + [dir2]
        assert(len(self_r_field) == len(self_r_width)
               & len(self_r_field) == len(self_r_dir))
        for d, w, f in zip(self_r_dir, self_r_width.values(), self_r_field):
            print("{} wire[{} - 1:0] {}_{},".format(d, w, self.PREFIX, f))
