from axi_connectN import axi_connectN
from axi_parameter import LEN_WIDTH, SIZE_WIDTH, BURST_WIDTH, LOCK_WIDTH, CACHE_WIDTH, PROT_WIDTH, QOS_WIDTH, REGION_WIDTH, USER_WIDTH


class axi_ar_channel:
    axi_ar_field = ["arid", "araddr", "arlen", "arsize",  "arburst",
                    "arlock", "arcache", "arprot", "arqos", "arregion",  "arvalid", "arready"]
    axi_ar_width = {"arid": 4, "araddr": 32, "arlen": LEN_WIDTH, "arsize": SIZE_WIDTH, "arburst": BURST_WIDTH,
                    "arlock": LOCK_WIDTH, "arcache": CACHE_WIDTH, "arprot": PROT_WIDTH, "arqos": QOS_WIDTH, "arregion": REGION_WIDTH,  "arvalid": 1, "arready": 1}

    def __init__(self, PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH):
        self.PREFIX = PREFIX
        self.axi_ar_width["araddr"] = ADDR_WIDTH
        self.axi_ar_width["arid"] = ID_WIDTH

    def def_wire(self):
        self_ar_field = self.axi_ar_field.copy()
        self_ar_width = self.axi_ar_width.copy()
        assert(len(self_ar_field) == len(self_ar_width))
        assert(len(self_ar_width) == 12)
        for w, f in zip(self_ar_width.values(), self_ar_field):
            print("wire[{} - 1:0] {}_{};".format(w, self.PREFIX, f))

    def def_connectN(self, io_prefix, wire_prefix, direction):
        assert((direction == "CROSSBAR_MASTER") | (
            direction == "CROSSBAR_SLAVE") | (direction == "BRAM_PORT") | (direction == "NATIVE_TO_AXI") | (direction == "AXI_TO_NATIVE"))

        self_ar_field = self.axi_ar_field.copy()
        if direction == "CROSSBAR_MASTER":
            self_ar_field.remove("arid")
            # self_ar_field.remove("aruser")
            assert(len(self_ar_field) == 11)
        elif direction == "CROSSBAR_SLAVE":
            self_ar_field.remove("arregion")
            # self_ar_field.remove("aruser")
            assert(len(self_ar_field) == 11)
        elif direction == "BRAM_PORT":
            self_ar_field.remove("arregion")
            # self_ar_field.remove("aruser")
            self_ar_field.remove("arlock")
            self_ar_field.remove("arcache")
            self_ar_field.remove("arqos")
            self_ar_field.remove("arprot")
            assert(len(self_ar_field) == 7)
        elif direction == "NATIVE_TO_AXI":
            assert(len(self_ar_field) == 12)
        elif direction == "AXI_TO_NATIVE":
            self_ar_field.remove("arregion")
            # self_ar_field.remove("aruser")
            assert(len(self_ar_field) == 11)
        axi_connectN(self_ar_field, io_prefix, wire_prefix)

    def def_output(self, direction="MASTER"):
        assert((direction == "MASTER") | (direction == "SLAVE"))
        if direction == "MASTER":
            dir1 = "output"
            dir2 = "input"
        else:
            dir1 = "input"
            dir2 = "output"
        self_ar_field = self.axi_ar_field.copy()
        self_ar_width = self.axi_ar_width.copy()
        self_ar_dir = [dir1] * (len(self_ar_field) - 1) + [dir2]
        assert(len(self_ar_field) == len(self_ar_width)
               & len(self_ar_field) == len(self_ar_dir))
        for d, w, f in zip(self_ar_dir, self_ar_width.values(), self_ar_field):
            print("{} wire[{} - 1:0] {}_{},".format(d, w, self.PREFIX, f))
