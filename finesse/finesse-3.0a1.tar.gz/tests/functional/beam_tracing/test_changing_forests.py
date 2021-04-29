"""Testing the structure of TraceForests built from the model forest with
only changing trees and branches included. These are constructed as an
initial step when building the simulation."""

import pytest
from finesse import Model
import finesse.tracing.ctracer as ctracer
from ...util import assert_trace_trees_equal


@pytest.fixture
def cavity_model():
    IFO = Model()
    IFO.parse(
        """
    l L0 P=1
    s s_in L0.p1 BS1.p1 L=1
    bs BS1
    s s0 BS1.p3 ITM.p1 L=5

    m ITM R=0.99 T=0.01 Rc=-2090
    s CAV ITM.p2 ETM.p1 L=4k
    m ETM R=0.99 T=0.01 Rc=2090

    cav FP ITM.p2

    s sout ETM.p2 END.p1 L=2
    nothing END
    """
    )

    return IFO


##### Changing a parameter when only the Cavity object is present #####


@pytest.mark.parametrize(
    "change", ("CAV.L", "ITM.Rcx", "ETM.Rcy"),
)
def test_changing_cavity_geometry_forest(cavity_model: Model, change):
    """Check that the changing forest is the whole cavity model when setting
    a geometric parameter of the cavity to tunable."""
    IFO = cavity_model

    internal_cav_tree = ctracer.TraceTree.from_cavity(IFO.FP)
    external_tree_out = ctracer.TraceTree.from_node(
        IFO.ETM.p2.o, IFO.FP, symmetric=True, pre_node=IFO.ETM.p1.i,
    )
    external_tree_back = ctracer.TraceTree.from_node(
        IFO.ITM.p1.o, IFO.FP, symmetric=True, pre_node=IFO.ITM.p2.i,
    )
    back_branch_tree = ctracer.TraceTree.from_node(
        IFO.BS1.p1.i, IFO.FP, symmetric=True, exclude=[IFO.BS1.p3.o,],
    )

    expect_forest = [
        internal_cav_tree,
        external_tree_out,
        external_tree_back,
        back_branch_tree,
    ]

    comp, param = change.split(".")
    pchange = getattr(IFO.elements[comp], param)
    pchange.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        # Only a single Cavity dependency so shouldn't be any
        # mismatch node couplings present
        assert len(sim.mismatched_node_couplings) == 0


@pytest.mark.parametrize(
    "change", ("ITM.phi", "ETM.phi", "ITM.R", "ETM.T", "ITM.xbeta", "ETM.ybeta"),
)
def test_changing_non_geometric_cavity_parameter_forest(cavity_model: Model, change):
    """Check that the changing forest is empty when only a non-geometric parameter
    is set to tunable."""
    IFO = cavity_model

    comp, param = change.split(".")
    pchange = getattr(IFO.elements[comp], param)
    pchange.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(chng_forest) == 0
        assert len(sim.mismatched_node_couplings) == 0


def test_changing_post_cavity_space_length_forest(cavity_model: Model):
    """Check that the changing forest is just the tree from the end mirror
    forwards when length of space after cavity is set to tunable."""
    IFO = cavity_model

    external_tree_out = ctracer.TraceTree.from_node(
        IFO.ETM.p2.o, IFO.FP, symmetric=True,
    )

    expect_forest = [external_tree_out]

    pchange = IFO.elements["sout"].L
    pchange.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == 0


def test_changing_pre_cavity_space_length_forest(cavity_model: Model):
    """Check that the changing forest is just the tree from the input mirror
    backwards when length of space before cavity is set to tunable."""
    IFO = cavity_model

    external_tree_back = ctracer.TraceTree.from_node(
        IFO.ITM.p1.o, IFO.FP, symmetric=True,
    )
    back_branch_tree = ctracer.TraceTree.from_node(
        IFO.BS1.p1.i, IFO.FP, symmetric=True, exclude=[IFO.BS1.p3.o,],
    )

    expect_forest = [
        external_tree_back,
        back_branch_tree,
    ]

    pchange = IFO.elements["s0"].L
    pchange.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == 0


def test_changing_pre_bs_space_length_forest(cavity_model: Model):
    """Check that the changing forest is just the tree from the BS
    backwards when length of space before BS is set to tunable."""
    IFO = cavity_model

    external_tree_back = ctracer.TraceTree.from_node(
        IFO.BS1.p1.o, IFO.FP, symmetric=True,
    )

    expect_forest = [external_tree_back]

    pchange = IFO.elements["s_in"].L
    pchange.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == 0


##### Adding a Gauss at the laser for extra complexity #####


@pytest.mark.parametrize(
    "change", ("CAV.L", "ITM.Rcx", "ETM.Rcy"),
)
def test_changing_cavity_geometry_with_laser_gauss_forest(cavity_model: Model, change):
    """Check that the changing forest is the whole cavity model excluding gauss tree
    when setting a geometric parameter of cavity to tunable."""
    IFO = cavity_model
    IFO.parse("gauss gL0 L0.p1.o q=-1+1j")

    internal_cav_tree = ctracer.TraceTree.from_cavity(IFO.FP)
    external_tree_out = ctracer.TraceTree.from_node(
        IFO.ETM.p2.o, IFO.FP, symmetric=True, pre_node=IFO.ETM.p1.i,
    )
    external_tree_back = ctracer.TraceTree.from_node(
        IFO.ITM.p1.o,
        IFO.FP,
        symmetric=True,
        pre_node=IFO.ITM.p2.i,
        exclude=[IFO.BS1.p1.o],
    )

    expect_forest = [
        internal_cav_tree,
        external_tree_out,
        external_tree_back,
    ]

    # Mismatch node couplings should occur on transmission through BS1 in this case
    expect_mm_couplings = (
        (IFO.BS1.p1.i, IFO.BS1.p3.o),
        (IFO.BS1.p3.i, IFO.BS1.p1.o),
        (IFO.BS1.p2.i, IFO.BS1.p4.o),
        (IFO.BS1.p4.i, IFO.BS1.p2.o),
    )

    comp, param = change.split(".")
    pchange = getattr(IFO.elements[comp], param)
    pchange.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == len(expect_mm_couplings)
        assert set(sim.mismatched_node_couplings) == set(expect_mm_couplings)


def test_changing_pre_bs_space_length_with_laser_gauss_forest(cavity_model: Model):
    """Check that the changing forest is just the tree from the BS
    forwards (from gauss node) when setting pre-BS space length tunable."""
    IFO = cavity_model
    IFO.parse("gauss gL0 L0.p1.o q=-1+1j")

    gauss_tree_forward = ctracer.TraceTree.from_node(
        IFO.L0.p1.o, IFO.gL0, symmetric=True, is_gauss=True, exclude=[IFO.BS1.p3.o],
    )

    expect_forest = [gauss_tree_forward]

    # Mismatch node couplings should occur on transmission through BS1 in this case
    expect_mm_couplings = (
        (IFO.BS1.p1.i, IFO.BS1.p3.o),
        (IFO.BS1.p3.i, IFO.BS1.p1.o),
        (IFO.BS1.p2.i, IFO.BS1.p4.o),
        (IFO.BS1.p4.i, IFO.BS1.p2.o),
    )

    pchange = IFO.elements["s_in"].L
    pchange.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == len(expect_mm_couplings)
        assert set(sim.mismatched_node_couplings) == set(expect_mm_couplings)


@pytest.mark.parametrize(
    "change", ("gL0.w0x", "gL0.w0y", "gL0.zx", "gL0.zy"),
)
def test_changing_laser_gauss_forest(cavity_model: Model, change):
    """Check that the changing forest is just the tree from the laser
    forwards when setting a Gauss parameter tunable."""
    IFO = cavity_model
    IFO.parse("gauss gL0 L0.p1.o q=-1+1j")

    gauss_tree_forward = ctracer.TraceTree.from_node(
        IFO.L0.p1.o, IFO.gL0, symmetric=True, is_gauss=True, exclude=[IFO.BS1.p3.o],
    )

    expect_forest = [gauss_tree_forward]

    # Mismatch node couplings should occur on transmission through BS1 in this case
    expect_mm_couplings = (
        (IFO.BS1.p1.i, IFO.BS1.p3.o),
        (IFO.BS1.p3.i, IFO.BS1.p1.o),
        (IFO.BS1.p2.i, IFO.BS1.p4.o),
        (IFO.BS1.p4.i, IFO.BS1.p2.o),
    )

    comp, param = change.split(".")
    pchange = getattr(IFO.elements[comp], param)
    pchange.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == len(expect_mm_couplings)
        assert set(sim.mismatched_node_couplings) == set(expect_mm_couplings)


def test_changing_bs_roc_with_cavity_priority_forest(cavity_model: Model):
    """Check that the changing forest is the trees coming from BS1 when
    setting BS1.Rcx tunable and cavity has highest trace priority."""
    IFO = cavity_model
    IFO.parse("gauss gL0 L0.p1.o q=-1+1j priority=-1")

    to_as_port_tree = ctracer.TraceTree.from_node(
        IFO.BS1.p3.i, IFO.FP, symmetric=True, exclude=[IFO.BS1.p1.o],
    )
    to_y_port_tree = ctracer.TraceTree.from_node(
        IFO.BS1.p1.i, IFO.gL0, symmetric=True, is_gauss=True, exclude=[IFO.BS1.p3.o],
    )

    expect_forest = [to_as_port_tree, to_y_port_tree]

    # Mismatch node couplings should occur on transmission through BS1 in this case
    expect_mm_couplings = (
        (IFO.BS1.p1.i, IFO.BS1.p3.o),
        (IFO.BS1.p3.i, IFO.BS1.p1.o),
        (IFO.BS1.p2.i, IFO.BS1.p4.o),
        (IFO.BS1.p4.i, IFO.BS1.p2.o),
    )

    pchange = IFO.elements["BS1"].Rcx
    pchange.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == len(expect_mm_couplings)
        assert set(sim.mismatched_node_couplings) == set(expect_mm_couplings)


def test_changing_bs_roc_with_gauss_priority_forest(cavity_model: Model):
    """Check that the changing forest is the trees coming from BS1 when
    setting BS1.Rcx tunable and gauss has highest trace priority."""
    IFO = cavity_model
    IFO.parse("gauss gL0 L0.p1.o q=-1+1j priority=1")

    from_bs_tree_forward = ctracer.TraceTree.from_node(
        IFO.BS1.p1.i, IFO.gL0, symmetric=True, is_gauss=True, exclude=[IFO.ITM.p2.i],
    )
    branch_tree = ctracer.TraceTree.from_node(
        IFO.BS1.p3.i, IFO.gL0, symmetric=True, is_gauss=True, exclude=[IFO.BS1.p1.o],
    )

    expect_forest = [
        from_bs_tree_forward,
        branch_tree,
    ]

    # Mismatch node couplings should occur on transmission through ITM in this case
    # and also for front surface reflection due to symmetric tracing behaviour
    expect_mm_couplings = (
        (IFO.ITM.p1.i, IFO.ITM.p2.o),
        (IFO.ITM.p2.i, IFO.ITM.p1.o),
        (IFO.ITM.p1.i, IFO.ITM.p1.o),
    )

    pchange = IFO.elements["BS1"].Rcx
    pchange.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == len(expect_mm_couplings)
        assert set(sim.mismatched_node_couplings) == set(expect_mm_couplings)


@pytest.mark.parametrize(
    "change", ("CAV.L", "ITM.Rcx", "ETM.Rcy"),
)
def test_changing_cavity_geometry_with_laser_gauss_disabled_forest(
    cavity_model: Model, change
):
    """Check that the changing forest is the whole cavity model when disabling
    the laser gauss and setting a geometric parameter of cavity tunable."""
    IFO = cavity_model
    IFO.parse("gauss gL0 L0.p1.o q=-1+1j")

    IFO.sim_trace_config["disable"] = "gL0"

    internal_cav_tree = ctracer.TraceTree.from_cavity(IFO.FP)
    external_tree_out = ctracer.TraceTree.from_node(
        IFO.ETM.p2.o, IFO.FP, symmetric=True, pre_node=IFO.ETM.p1.i,
    )
    external_tree_back = ctracer.TraceTree.from_node(
        IFO.ITM.p1.o, IFO.FP, symmetric=True, pre_node=IFO.ITM.p2.i,
    )
    back_branch_tree = ctracer.TraceTree.from_node(
        IFO.BS1.p1.i, IFO.FP, symmetric=True, exclude=[IFO.BS1.p3.o,],
    )

    expect_forest = [
        internal_cav_tree,
        external_tree_out,
        external_tree_back,
        back_branch_tree,
    ]

    comp, param = change.split(".")
    pchange = getattr(IFO.elements[comp], param)
    pchange.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == 0


def test_changing_itm_roc_with_laser_gauss_forest(cavity_model: Model):
    """Check that the changing forest is the cavity forwards with laser gauss
    set as highest priority. Also checks that ITM.p1.i -> ITM.p1.o is in the
    mismatched node couplings as a special case (as these nodes aren't in
    changing forest but coupling can still change when symmetrically tracing)."""
    IFO = cavity_model
    IFO.parse("gauss gL0 L0.p1.o q=-1+1j priority=1")

    internal_cav_tree = ctracer.TraceTree.from_cavity(IFO.FP)
    external_tree_out = ctracer.TraceTree.from_node(
        IFO.ETM.p2.o, IFO.FP, symmetric=True, pre_node=IFO.ETM.p1.i,
    )

    expect_forest = [
        internal_cav_tree,
        external_tree_out,
    ]

    # Mismatch node couplings should occur on transmission through ITM in this case
    # and also for front surface reflection due to symmetric tracing behaviour
    expect_mm_couplings = (
        (IFO.ITM.p1.i, IFO.ITM.p2.o),
        (IFO.ITM.p2.i, IFO.ITM.p1.o),
        (IFO.ITM.p1.i, IFO.ITM.p1.o),
    )

    IFO.ITM.Rcx.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == len(expect_mm_couplings)
        assert set(sim.mismatched_node_couplings) == set(expect_mm_couplings)


@pytest.mark.parametrize(
    "change_cav", ("gL0.w0x", "gL0.w0y", "gL0.zx", "gL0.zy"),
)
@pytest.mark.parametrize(
    "change_gauss", ("CAV.L", "ITM.Rcx", "ETM.Rcy"),
)
def test_changing_cavity_geometry_and_laser_gauss_forest(
    cavity_model: Model, change_cav, change_gauss
):
    """Check that the changing forest is the whole cavity model when setting
    a geometric parameter of the cavity and the laser gauss to tunable."""
    IFO = cavity_model
    IFO.parse("gauss gL0 L0.p1.o q=-1+1j")

    internal_cav_tree = ctracer.TraceTree.from_cavity(IFO.FP)
    external_tree_out = ctracer.TraceTree.from_node(
        IFO.ETM.p2.o, IFO.FP, symmetric=True, pre_node=IFO.ETM.p1.i,
    )
    external_tree_back = ctracer.TraceTree.from_node(
        IFO.ITM.p1.o,
        IFO.FP,
        symmetric=True,
        pre_node=IFO.ITM.p2.i,
        exclude=[IFO.BS1.p1.o],
    )
    gauss_tree_forward = ctracer.TraceTree.from_node(
        IFO.L0.p1.o, IFO.gL0, symmetric=True, is_gauss=True, exclude=[IFO.BS1.p3.o],
    )

    expect_forest = [
        internal_cav_tree,
        external_tree_out,
        external_tree_back,
        gauss_tree_forward,
    ]

    # Mismatch node couplings should occur on transmission through BS1 in this case
    expect_mm_couplings = (
        (IFO.BS1.p1.i, IFO.BS1.p3.o),
        (IFO.BS1.p3.i, IFO.BS1.p1.o),
        (IFO.BS1.p2.i, IFO.BS1.p4.o),
        (IFO.BS1.p4.i, IFO.BS1.p2.o),
    )

    for change in change_cav, change_gauss:
        comp, param = change.split(".")
        pchange = getattr(IFO.elements[comp], param)
        pchange.is_tunable = True

    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == len(expect_mm_couplings)
        assert set(sim.mismatched_node_couplings) == set(expect_mm_couplings)


@pytest.mark.parametrize(
    "change", ("CAV.L", "ITM.Rcx", "ETM.Rcy"),
)
def test_changing_cavity_geometry_and_laser_gauss_reversed_priorities_forest(
    cavity_model: Model, change
):
    """Check that the changing forest is the whole cavity model when setting
    a geometric parameter of the cavity and the laser gauss to tunable."""
    IFO = cavity_model
    IFO.parse("gauss gL0 L0.p1.o q=-1+1j priority=1")

    internal_cav_tree = ctracer.TraceTree.from_cavity(IFO.FP)
    external_tree_out = ctracer.TraceTree.from_node(
        IFO.ETM.p2.o, IFO.FP, symmetric=True, pre_node=IFO.ETM.p1.i,
    )
    gauss_tree_forward = ctracer.TraceTree.from_node(
        IFO.L0.p1.o, IFO.gL0, symmetric=True, is_gauss=True, exclude=[IFO.ITM.p2.i],
    )
    branch_tree = ctracer.TraceTree.from_node(
        IFO.BS1.p3.i, IFO.gL0, symmetric=True, is_gauss=True, exclude=[IFO.BS1.p1.o],
    )

    expect_forest = [
        internal_cav_tree,
        gauss_tree_forward,
        external_tree_out,
        branch_tree,
    ]

    # Mismatch node couplings should occur on transmission through ITM in this case
    # and also for front surface reflection due to symmetric tracing behaviour
    expect_mm_couplings = (
        (IFO.ITM.p1.i, IFO.ITM.p2.o),
        (IFO.ITM.p2.i, IFO.ITM.p1.o),
        (IFO.ITM.p1.i, IFO.ITM.p1.o),
    )

    comp, param = change.split(".")
    pchange_cav = getattr(IFO.elements[comp], param)
    pchange_cav.is_tunable = True
    pchange_gauss = IFO.elements["gL0"].zx
    pchange_gauss.is_tunable = True
    with IFO.built() as sim:
        chng_forest = sim.trace_forest.forest

        assert len(expect_forest) == len(chng_forest)
        for tree1, tree2 in zip(expect_forest, chng_forest):
            assert_trace_trees_equal(tree1, tree2)

        assert len(sim.mismatched_node_couplings) == len(expect_mm_couplings)
        assert set(sim.mismatched_node_couplings) == set(expect_mm_couplings)
