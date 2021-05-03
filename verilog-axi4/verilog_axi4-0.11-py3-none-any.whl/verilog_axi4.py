
LEM_WIDTH = 8

axi_aw_field = ["awid", "awaddr", "awlen", "awsize", "awburst", "awlock",
                "awcache", "awprot", "awqos", "awregion", "awuser", "awvalid", "awready"]
axi_w_field = ["wid", "wdata", "wstrb", "wlast", "wuser", "wvalid", "wready"]
axi_b_field = ["bid", "bresp", "buser", "bvalid", "bready"]
axi_ar_field = ["arid", "araddr", "arlen", "arsize", "arburst",
                "arlock", "arcache", "arprot", "arqos", "arregion", "aruser", "arvalid", "arready"]
axi_r_field = ["rid", "rdata", "rresp", "rlast", "ruser", "rvalid", "rready"]
axi_field = axi_aw_field + axi_w_field + \
    axi_b_field + axi_ar_field + axi_r_field


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


# def axi_output(dir1, dir2, axi_width, axi_field):
#     for width, name in axi_width, axi_field:
#         print("{} ")

# ADDR_WIDTH           : width of awaddr and araddr signals
# DATA_WIDTH           : width of wdata and rdata signals
# STRB_WIDTH           : width of wstrb signal
# ID_WIDTH             : width of *id signals
# AWUSER_ENABLE        : enable awuser signal
# AWUSER_WIDTH         : width of awuser signal
# WUSER_ENABLE         : enable wuser signal
# WUSER_WIDTH          : width of wuser signal
# BUSER_ENABLE         : enable buser signal
# BUSER_WIDTH          : width of buser signal
# ARUSER_ENABLE        : enable aruser signal
# ARUSER_WIDTH         : width of aruser signal
# RUSER_ENABLE         : enable ruser signal
# RUSER_WIDTH          : width of ruser signal

# FIELD    axi_crossbar_slave   axi_crossbar_master     axi_ram
# arid       YES                      NO                  YES       : Read address ID
# araddr     YES                      YES                 YES       : Read address
# arlen      YES                      YES                 YES       : Read burst length
# arsize     YES                      YES                 YES       : Read burst size
# arburst    YES                      YES                 YES       : Read burst type
# arlock     YES                      YES                 NO        : Read locking
# arcache    YES                      YES                 NO        : Read cache handling
# arprot     YES                      YES                 NO        : Read protection level
# arqos      YES                      YES                 NO        : Read QoS setting
# arregion   NO                       YES                 NO        : Read region
# aruser     NO                       NO                  NO        : Read user sideband signal
# arvalid    YES                      YES                 YES       : Read address valid
# arready    YES                      YES                 YES       : Read address ready (from slave)


class axi_ar_channel:
    def __init__(self, PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH, LEN_WIDTH=8, SIZE_WIDTH=3, BURST_WIDTH=2, LOCK_WIDTH=1, CACHE_WIDTH=4, PROT_WIDTH=3, QOS_WIDTH=4, REGION_WIDTH=4, USER_WIDTH=2):
        self.PREFIX = PREFIX
        self.ADDR_WIDTH = ADDR_WIDTH
        self.DATA_WIDTH = DATA_WIDTH
        self.ID_WIDTH = ID_WIDTH
        self.LEN_WIDTH = LEN_WIDTH
        self.SIZE_WIDTH = SIZE_WIDTH
        self.BURST_WIDTH = BURST_WIDTH
        self.LOCK_WIDTH = LOCK_WIDTH
        self.CACHE_WIDTH = CACHE_WIDTH
        self.PROT_WIDTH = PROT_WIDTH
        self.QOS_WIDTH = QOS_WIDTH
        self.REGION_WIDTH = REGION_WIDTH
        self.USER_WIDTH = USER_WIDTH

    def def_wire(self):
        print("wire[{} - 1:0] {}_arid;".format(self.ID_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_araddr;".format(self.ADDR_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_arlen;".format(self.LEN_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_arsize;".format(self.SIZE_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_arburst;".format(self.BURST_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_arlock;".format(self.LOCK_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_arcache;".format(self.CACHE_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_arprot;".format(self.PROT_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_arqos;".format(self.QOS_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_arregion;".format(self.REGION_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_aruser;".format(self.USER_WIDTH, self.PREFIX))
        print("wire[1 - 1:0] {}_arvalid;".format(self.PREFIX))
        print("wire[1 - 1:0] {}_arready;".format(self.PREFIX))

    def def_connectN(self, io_prefix, wire_prefix, direction):
        self_ar_field = axi_ar_field.copy()
        if direction == "CROSSBAR_MASTER":
            # self_ar_field.remove("arregion")
            self_ar_field.remove("aruser")
            self_ar_field.remove("arid")
        elif direction == "CROSSBAR_SLAVE":
            self_ar_field.remove("arregion")
            self_ar_field.remove("aruser")
        elif direction == "BRAM_PORT":
            self_ar_field.remove("arlock")
            self_ar_field.remove("arcache")
            self_ar_field.remove("arqos")
            self_ar_field.remove("arprot")

        axi_connectN(self_ar_field, io_prefix, wire_prefix)

    def def_output(self, direction="MASTER"):
        if direction == "MASTER":
            dir1 = "output"
            dir2 = "input"
        else:
            dir1 = "input"
            dir2 = "output"

        print("{} wire[{} - 1:0] {}_arid;".format(dir1,
                                                  self.ID_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_araddr;".format(dir1, self.ADDR_WIDTH, self.PREFIX))
        print("{} wire[{} - 1:0] {}_arlen;".format(dir1,
                                                   self.LEN_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_arsize;".format(dir1, self.SIZE_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_arburst;".format(dir1, self.BURST_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_arlock;".format(dir1, self.LOCK_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_arcache;".format(dir1, self.CACHE_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_arprot;".format(dir1, self.PROT_WIDTH, self.PREFIX))
        print("{} wire[{} - 1:0] {}_arqos;".format(dir1,
                                                   self.QOS_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_arregion;".format(dir1, self.REGION_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_aruser;".format(dir1, self.USER_WIDTH, self.PREFIX))
        print("{} wire[1 - 1:0] {}_arvalid;".format(dir1, self.PREFIX))
        print("{} wire[1 - 1:0] {}_arready;".format(dir2, self.PREFIX))

        # FIELD     axi_crossbar_slave   axi_crossbar_master     axi_ram
        # rid        YES                      NO                  YES       : Read data ID
        # rdata      YES                      YES                 YES       : Read data
        # rresp      YES                      YES                 YES       : Read response
        # rlast      YES                      YES                 YES       : Read data last transfer in burst
        # ruser      NO                       NO                  NO        : Read data user sideband signal
        # rvalid     YES                      YES                 YES       : Read response valid
        # rready     YES                      YES                 YES       : Read response ready (from master)


class axi_r_channel:
    def __init__(self, PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH, LEN_WIDTH=8, SIZE_WIDTH=3, BURST_WIDTH=2, LOCK_WIDTH=1, CACHE_WIDTH=4, PROT_WIDTH=3, QOS_WIDTH=4, REGION_WIDTH=4, USER_WIDTH=2):
        self.PREFIX = PREFIX
        self.ADDR_WIDTH = ADDR_WIDTH
        self.DATA_WIDTH = DATA_WIDTH
        self.ID_WIDTH = ID_WIDTH
        self.USER_WIDTH = USER_WIDTH

    def def_wire(self):
        print("wire[{} - 1:0] {}_rid;".format(self.ID_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_raddr;".format(self.ADDR_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_rdata;".format(self.DATA_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_ruser;".format(self.USER_WIDTH, self.PREFIX))
        print("wire[1 - 1:0] {}_rvalid;".format(self.PREFIX))
        print("wire[1 - 1:0] {}_rready;".format(self.PREFIX))

    def def_connectN(self, io_prefix, wire_prefix, direction):
        self_r_field = axi_r_field.copy()
        if direction == "CROSSBAR_MASTER":
            self_r_field.remove("rid")
            self_r_field.remove("ruser")
        elif direction == "CROSSBAR_SLAVE":
            self_r_field.remove("ruser")

        axi_connectN(self_r_field, io_prefix, wire_prefix)

    def def_output(self, direction="MASTER"):
        if direction == "MASTER":
            dir1 = "input"
            dir2 = "output"
        else:
            dir1 = "output"
            dir2 = "input"
        print("{} wire[{} - 1:0] {}_rid;".format(dir1,
                                                 self.ID_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_raddr;".format(dir1, self.ADDR_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_rdata;".format(dir1, self.DATA_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_ruser;".format(dir1, self.USER_WIDTH, self.PREFIX))
        print("{} wire[1 - 1:0] {}_rvalid;".format(dir1, self.PREFIX))
        print("{} wire[1 - 1:0] {}_rready;".format(dir2, self.PREFIX))

# FIELD    axi_crossbar_slave   axi_crossbar_master     axi_ram
# awid        YES                      NO                  YES      : Write address ID
# awaddr      YES                      YES                 YES      : Write address
# awlen       YES                      YES                 YES      : Write burst length
# awsize      YES                      YES                 YES      : Write burst size
# awburst     YES                      YES                 YES      : Write burst type
# awlock      YES                      YES                 NO       : Write locking
# awcache     YES                      YES                 NO       : Write cache handling
# awprot      YES                      YES                 NO       : Write protection level
# awqos       YES                      YES                 NO       : Write QoS setting
# awregion    NO                       YES                 YES      : Write region
# awuser      NO                       NO                  NO       : Write user sideband signal
# awvalid     YES                      YES                 YES      : Write address valid
# awready     YES                      YES                 YES      : Write address ready (from slave)


class axi_aw_channel:
    def __init__(self, PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH, LEN_WIDTH=8, SIZE_WIDTH=3, BURST_WIDTH=2, LOCK_WIDTH=1, CACHE_WIDTH=4, PROT_WIDTH=3, QOS_WIDTH=4, REGION_WIDTH=4, USER_WIDTH=2):
        self.PREFIX = PREFIX
        self.ADDR_WIDTH = ADDR_WIDTH
        self.DATA_WIDTH = DATA_WIDTH
        self.ID_WIDTH = ID_WIDTH
        self.LEN_WIDTH = LEN_WIDTH
        self.SIZE_WIDTH = SIZE_WIDTH
        self.BURST_WIDTH = BURST_WIDTH
        self.LOCK_WIDTH = LOCK_WIDTH
        self.CACHE_WIDTH = CACHE_WIDTH
        self.PROT_WIDTH = PROT_WIDTH
        self.QOS_WIDTH = QOS_WIDTH
        self.REGION_WIDTH = REGION_WIDTH
        self.USER_WIDTH = USER_WIDTH

    def def_wire(self):
        print("wire[{} - 1:0] {}_awid;".format(self.ID_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_awaddr;".format(self.ADDR_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_awlen;".format(self.LEN_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_awsize;".format(self.SIZE_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_awburst;".format(self.BURST_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_awlock;".format(self.LOCK_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_awcache;".format(self.CACHE_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_awprot;".format(self.PROT_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_awqos;".format(self.QOS_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_awregion;".format(self.REGION_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_awuser;".format(self.USER_WIDTH, self.PREFIX))
        print("wire[1 - 1:0] {}_awvalid;".format(self.PREFIX))
        print("wire[1 - 1:0] {}_awready;".format(self.PREFIX))

    def def_connectN(self, io_prefix, wire_prefix, direction):
        self_aw_field = axi_aw_field.copy()
        if direction == "CROSSBAR_MASTER":
            self_aw_field.remove("awuser")
            self_aw_field.remove("awid")
        elif direction == "CROSSBAR_SLAVE":
            self_aw_field.remove("awregion")
            self_aw_field.remove("awuser")
        elif direction == "BRAM_PORT":
            self_aw_field.remove("awlock")
            self_aw_field.remove("awcache")
            self_aw_field.remove("awqos")
            self_aw_field.remove("awprot")
        axi_connectN(self_aw_field, io_prefix, wire_prefix)

    def def_output(self, direction="MASTER"):
        if direction == "MASTER":
            dir1 = "output"
            dir2 = "input"
        else:
            dir1 = "input"
            dir2 = "output"
        print("{} wire[{} - 1:0] {}_awid;".format(dir1,
                                                  self.ID_WIDTH, self.PREFIX))
        print("{} wire[{} - 1:0] {}_awaddr;".format(dir1,
                                                    self.ADDR_WIDTH, self.PREFIX))
        print("{} wire[{} - 1:0] {}_awlen;".format(dir1,
                                                   self.LEN_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_awsize;".format(dir1, self.SIZE_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_awburst;".format(dir1, self.BURST_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_awlock;".format(dir1, self.LOCK_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_awcache;".format(dir1, self.CACHE_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_awprot;".format(dir1, self.PROT_WIDTH, self.PREFIX))
        print("{} wire[{} - 1:0] {}_awqos;".format(dir1,
                                                   self.QOS_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_awregion;".format(dir1, self.REGION_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_awuser;".format(dir1, self.USER_WIDTH, self.PREFIX))
        print("{} wire[1 - 1:0] {}_awvalid;".format(dir1, self.PREFIX))
        print("{} wire[1 - 1:0] {}_awready;".format(dir2, self.PREFIX))
# FIELD    axi_crossbar_slave   axi_crossbar_master     axi_ram
# wdata       YES                      YES               YES        : Write data
# wstrb       YES                      YES               YES        : Write data strobe (byte select)
# wlast       YES                      YES               YES        : Write data last transfer in burst
# wuser       NO                       NO                NO         : Write data user sideband signal
# wvalid      YES                      YES               YES        : Write data valid
# wready      YES                      YES               YES        : Write data ready (from slave)


class axi_w_channel:
    def __init__(self, PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH, LEN_WIDTH=8, SIZE_WIDTH=3, BURST_WIDTH=2, LOCK_WIDTH=1, CACHE_WIDTH=4, PROT_WIDTH=3, QOS_WIDTH=4, REGION_WIDTH=4, USER_WIDTH=2):
        self.PREFIX = PREFIX
        self.ADDR_WIDTH = ADDR_WIDTH
        self.DATA_WIDTH = DATA_WIDTH
        self.ID_WIDTH = ID_WIDTH
        self.USER_WIDTH = USER_WIDTH

    def def_wire(self):
        # print("wire[{} - 1:0] {}_wid;".format(self.ID_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_waddr;".format(self.ADDR_WIDTH, self.PREFIX))
        print(
            "wire[{} - 1:0] {}_wstrb;".format(int(self.DATA_WIDTH/8), self.PREFIX))
        print("wire[{} - 1:0] {}_wdata;".format(self.DATA_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_wuser;".format(self.USER_WIDTH, self.PREFIX))
        print("wire[1 - 1:0] {}_wvalid;".format(self.PREFIX))
        print("wire[1 - 1:0] {}_wready;".format(self.PREFIX))

    def def_connectN(self, io_prefix, wire_prefix, direction):
        self_w_field = axi_w_field.copy()
        if direction == "CROSSBAR_MASTER":
            self_w_field.remove("wid")
            self_w_field.remove("wuser")
        elif direction == "CROSSBAR_SLAVE":
            self_w_field.remove("wid")
            self_w_field.remove("wuser")
        axi_connectN(self_w_field, io_prefix, wire_prefix)

    def def_output(self, direction="MASTER"):
        if direction == "MASTER":
            dir1 = "output"
            dir2 = "input"
        else:
            dir1 = "input"
            dir2 = "output"
        print("{} wire[{} - 1:0] {}_waddr;".format(dir1,
                                                   self.ADDR_WIDTH, self.PREFIX))
        print(
            "{} wire[{} - 1:0] {}_wstrb;".format(dir1, int(self.DATA_WIDTH/8), self.PREFIX))
        print("{} wire[{} - 1:0] {}_wdata;".format(dir1,
                                                   self.DATA_WIDTH, self.PREFIX))
        print("{} wire[{} - 1:0] {}_wuser;".format(dir1,
                                                   self.USER_WIDTH, self.PREFIX))
        print("{} wire[1 - 1:0] {}_wvalid;".format(dir1, self.PREFIX))
        print("{} wire[1 - 1:0] {}_wready;".format(dir2, self.PREFIX))
# FIELD    axi_crossbar_slave   axi_crossbar_master     axi_ram
# bid         YES                      NO                  YES      : Write response ID
# bresp       YES                      YES                 YES      : Write response
# buser       NO                       NO                  NO       : Write response user sideband signal
# bvalid      YES                      YES                 YES      : Write response valid
# bready      YES                      YES                 YES      : Write response ready (from master)


class axi_b_channel:
    def __init__(self, PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH, RESP_WIDTH=2, LEN_WIDTH=8, SIZE_WIDTH=3, BURST_WIDTH=2, LOCK_WIDTH=1, CACHE_WIDTH=4, PROT_WIDTH=3, QOS_WIDTH=4, REGION_WIDTH=4, USER_WIDTH=2):
        self.PREFIX = PREFIX
        self.ADDR_WIDTH = ADDR_WIDTH
        self.DATA_WIDTH = DATA_WIDTH
        self.ID_WIDTH = ID_WIDTH
        self.USER_WIDTH = USER_WIDTH
        self.RESP_WIDTH = RESP_WIDTH

    def def_wire(self):
        print("wire[{} - 1:0] {}_bid;".format(self.ID_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_bresp;".format(self.RESP_WIDTH, self.PREFIX))
        print("wire[{} - 1:0] {}_buser;".format(self.USER_WIDTH, self.PREFIX))
        print("wire[1 - 1:0] {}_bvalid;".format(self.PREFIX))
        print("wire[1 - 1:0] {}_bready;".format(self.PREFIX))

    def def_connectN(self, io_prefix, wire_prefix, direction):
        self_b_field = axi_b_field.copy()
        if direction == "CROSSBAR_MASTER":
            self_b_field.remove("bid")
            self_b_field.remove("buser")
        elif direction == "CROSSBAR_SLAVE":
            self_b_field.remove("buser")
        axi_connectN(self_b_field, io_prefix, wire_prefix)

    def def_output(self, direction="MASTER"):
        if direction == "MASTER":
            dir1 = "input"
            dir2 = "output"
        else:
            dir1 = "output"
            dir2 = "input"
        print("{} wire[{} - 1:0] {}_bid;".format(dir1,
                                                 self.ID_WIDTH, self.PREFIX))
        print("{} wire[{} - 1:0] {}_bresp;".format(dir1,
                                                   self.RESP_WIDTH, self.PREFIX))
        print("{} wire[{} - 1:0] {}_buser;".format(dir1,
                                                   self.USER_WIDTH, self.PREFIX))
        print("{} wire[1 - 1:0] {}_bvalid;".format(dir1, self.PREFIX))
        print("{} wire[1 - 1:0] {}_bready;".format(dir2, self.PREFIX))


class axi():
    def __init__(self, PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH):
        self.axi_ar = axi_ar_channel(PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH)
        self.axi_aw = axi_aw_channel(PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH)
        self.axi_r = axi_r_channel(PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH)
        self.axi_w = axi_w_channel(PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH)
        self.axi_b = axi_b_channel(PREFIX, ADDR_WIDTH, DATA_WIDTH, ID_WIDTH)

    def def_wire(self):
        self.axi_ar.def_wire()
        self.axi_r.def_wire()
        self.axi_aw.def_wire()
        self.axi_w.def_wire()
        self.axi_b.def_wire()

    def def_connectN(self, io_prefix, wire_prefix, direction="CROSSBAR_SLAVE"):
        self.axi_ar.def_connectN(io_prefix, wire_prefix, direction)
        self.axi_aw.def_connectN(io_prefix, wire_prefix, direction)
        self.axi_r.def_connectN(io_prefix, wire_prefix, direction)
        self.axi_w.def_connectN(io_prefix, wire_prefix, direction)
        self.axi_b.def_connectN(io_prefix, wire_prefix, direction)

    def def_output(self, direction="MASTER"):
        self.axi_ar.def_output(direction)
        self.axi_aw.def_output(direction)
        self.axi_r.def_output(direction)
        self.axi_w.def_output(direction)
        self.axi_b.def_output(direction)
