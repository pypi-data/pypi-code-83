from axi_aw_channel import axi_aw_channel
from axi_w_channel import axi_w_channel
from axi_b_channel import axi_b_channel
from axi_ar_channel import axi_ar_channel
from axi_r_channel import axi_r_channel


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
