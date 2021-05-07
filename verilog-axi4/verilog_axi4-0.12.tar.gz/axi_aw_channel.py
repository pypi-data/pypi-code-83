from axi_connectN import axi_connectN
from axi_parameter import LEN_WIDTH, SIZE_WIDTH, BURST_WIDTH, LOCK_WIDTH, CACHE_WIDTH, PROT_WIDTH, QOS_WIDTH, REGION_WIDTH, USER_WIDTH
# FIELD    WIDTH  axi_crossbar_slave   axi_crossbar_master     axi_ram
# awid      0-32        YES                      NO                  YES      : Write address ID
# awaddr   12-64        YES                      YES                 YES      : Write address
# awlen      8          YES                      YES                 YES      : Write burst length
# awsize     3          YES                      YES                 YES      : Write burst size
# awburst    2          YES                      YES                 YES      : Write burst type
# awlock     1          YES                      YES                 NO       : Write locking
# awcache    4          YES                      YES                 NO       : Write cache handling
# awprot     3          YES                      YES                 NO       : Write protection level
# awqos      4          YES                      YES                 NO       : Write QoS setting
# awregion   4          NO                       YES                 YES      : Write region
# awuser     1          NO                       NO                  NO       : Write user sideband signal
# awvalid    1          YES                      YES                 YES      : Write address valid
# awready    1          YES                      YES                 YES      : Write address ready (from slave)


class axi_aw_channel:
    axi_aw_field = ["awid", "awaddr", "awlen", "awsize", "awburst", "awlock",
                    "awcache", "awprot", "awqos", "awregion", "awvalid", "awready"]

    axi_aw_width = {"awid": 4, "awaddr": 32, "awlen": LEN_WIDTH, "awsize": SIZE_WIDTH, "awburst": BURST_WIDTH, "awlock": LOCK_WIDTH,
                    "awcache": CACHE_WIDTH, "awprot": PROT_WIDTH, "awqos": QOS_WIDTH, "awregion": REGION_WIDTH, "awvalid": 1, "awready": 1}

    def __init__(self, PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH):
        self.PREFIX = PREFIX
        self.axi_aw_width["awaddr"] = ADDR_WIDTH
        self.axi_aw_width["awid"] = ID_WIDTH

    def def_wire(self):
        self_aw_field = self.axi_aw_field.copy()
        self_aw_width = self.axi_aw_width.copy()
        assert(len(self_aw_field) == len(self_aw_width))
        assert(len(self_aw_width) == 12)
        for w, f in zip(self_aw_width.values(), self_aw_field):
            print("wire[{} - 1:0] {}_{};".format(w, self.PREFIX, f))

    def def_connectN(self, io_prefix, wire_prefix, direction):
        assert((direction == "CROSSBAR_MASTER") | (
            direction == "CROSSBAR_SLAVE") | (direction == "BRAM_PORT") | (direction == "NATIVE_TO_AXI") | (direction == "AXI_TO_NATIVE"))

        self_aw_field = self.axi_aw_field.copy()
        if direction == "CROSSBAR_MASTER":
            # self_aw_field.remove("awuser")
            self_aw_field.remove("awid")
            assert(len(self_aw_field) == 11)
        elif direction == "CROSSBAR_SLAVE":
            self_aw_field.remove("awregion")
            # self_aw_field.remove("awuser")
            assert(len(self_aw_field) == 11)
        elif direction == "BRAM_PORT":
            self_aw_field.remove("awregion")
            # self_aw_field.remove("awuser")
            self_aw_field.remove("awlock")
            self_aw_field.remove("awcache")
            self_aw_field.remove("awqos")
            self_aw_field.remove("awprot")
            assert(len(self_aw_field) == 7)
        elif direction == "NATIVE_TO_AXI":
            # self_aw_field.remove("awuser")
            assert(len(self_aw_field) == 12)
        elif direction == "AXI_TO_NATIVE":
            self_aw_field.remove("awregion")
            # self_aw_field.remove("awuser")
            assert(len(self_aw_field) == 11)
        axi_connectN(self_aw_field, io_prefix, wire_prefix)

    def def_output(self, direction="MASTER"):
        assert((direction == "MASTER") | (direction == "SLAVE"))

        self_aw_field = self.axi_aw_field.copy()
        self_aw_width = self.axi_aw_width.copy()
        if direction == "MASTER":
            dir1 = "output"
            dir2 = "input"

        else:
            dir1 = "input"
            dir2 = "output"
        self_aw_dir = [dir1] * (len(self_aw_field) - 1) + [dir2]
        assert(len(self_aw_field) == len(self_aw_width)
               & len(self_aw_field) == len(self_aw_dir))
        for d, w, f in zip(self_aw_dir, self_aw_width.values(), self_aw_field):
            print("{} wire[{} - 1:0] {}_{},".format(d, w, self.PREFIX, f))
