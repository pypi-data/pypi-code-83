from axi_connectN import axi_connectN
from axi_parameter import STRB_WIDTH, USER_WIDTH


class axi_w_channel:
    axi_w_field = ["wid", "wdata", "wstrb",
                   "wlast", "wvalid", "wready"]
    axi_w_width = {"wid": 1, "wdata": 64, "wstrb": STRB_WIDTH,
                   "wlast": 1, "wvalid": 1, "wready": 1}

    def __init__(self, PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH):
        self.PREFIX = PREFIX
        self.axi_w_width["wid"] = ID_WIDTH
        self.axi_w_width["wdata"] = DATA_WIDTH
        self.axi_w_width["wstrb"] = int(DATA_WIDTH/8)

    def def_wire(self):
        self_w_field = self.axi_w_field.copy()
        self_w_width = self.axi_w_width.copy()

        assert(len(self_w_field) == len(self_w_width))

        for w, f in zip(self_w_width.values(), self_w_field):
            print("wire[{} - 1:0] {}_{};".format(w, self.PREFIX, f))

    def def_connectN(self, io_prefix, wire_prefix, direction):
        assert((direction == "CROSSBAR_MASTER") | (
            direction == "CROSSBAR_SLAVE") | (direction == "BRAM_PORT") | (direction == "NATIVE_TO_AXI") | (direction == "AXI_TO_NATIVE"))

        self_w_field = self.axi_w_field.copy()
        if direction == "CROSSBAR_MASTER":
            self_w_field.remove("wid")
            # self_w_field.remove("wuser")
            assert(len(self_w_field) == 5)
        elif direction == "CROSSBAR_SLAVE":
            self_w_field.remove("wid")
            # self_w_field.remove("wuser")
            assert(len(self_w_field) == 5)
        elif direction == "BRAM_PORT":
            self_w_field.remove("wid")
            # self_w_field.remove("wuser")
            assert(len(self_w_field) == 5)
        elif direction == "NATIVE_TO_AXI":
            self_w_field.remove("wid")
            assert(len(self_w_field) == 5)
        elif direction == "AXI_TO_NATIVE":
            self_w_field.remove("wid")
            # self_w_field.remove("wuser")
            assert(len(self_w_field) == 5)
        axi_connectN(self_w_field, io_prefix, wire_prefix)

    def def_output(self, direction="MASTER"):
        assert((direction == "MASTER") | (direction == "SLAVE"))
        if direction == "MASTER":
            dir1 = "output"
            dir2 = "input"
        else:
            dir1 = "input"
            dir2 = "output"
        self_w_field = self.axi_w_field.copy()
        self_w_width = self.axi_w_width.copy()
        self_w_dir = [dir1] * (len(self_w_field) - 1) + [dir2]
        assert(len(self_w_field) == len(self_w_width)
               & len(self_w_field) == len(self_w_dir))
        for d, w, f in zip(self_w_dir, self.axi_w_width.values(), self_w_field):
            print("{} wire[{} - 1:0] {}_{},".format(d, w, self.PREFIX, f))
