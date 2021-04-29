"""Testing the structure of TraceForests built for beam tracing routines.

These form the core of all beam tracing code so simply testing that these are structured
correctly is enough to check beam tracing itself in most cases.
"""

import logging
import pytest
import finesse.tracing.ctracer as ctracer
from finesse.exceptions import BeamTraceException
from ...util import assert_trace_trees_equal


##### Simple Fabry-Perot cavity tests #####


@pytest.fixture(scope="module")
def fp_cavity_script():
    return """
    l L0 P=1

    s s0 L0.p1 ITM.p1

    m ITM R=0.99 T=0.01 Rc=-10
    s CAV ITM.p2 ETM.p1 L=1
    m ETM R=0.99 T=0.01 Rc=10
    """


def test_fp_single_cavity_forest(model, fp_cavity_script):
    """Check forest structure for simple FP cavity file with single Cavity object as
    dependency."""
    model.parse(fp_cavity_script)
    model.parse("cav FP ITM.p2")

    model.beam_trace()

    internal_cav_tree = ctracer.TraceTree.from_cavity(model.FP)
    external_tree_out = ctracer.TraceTree.from_node(
        model.ETM.p2.o, model.FP, symmetric=True, pre_node=model.ETM.p1.i,
    )
    external_tree_back = ctracer.TraceTree.from_node(
        model.ITM.p1.o, model.FP, symmetric=True, pre_node=model.ITM.p2.i,
    )

    forest = [internal_cav_tree, external_tree_out, external_tree_back]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_fp_single_gauss_at_laser_forest(model, fp_cavity_script):
    """Check forest structure for simple FP cavity file with single Gauss object,
    positioned at Laser output, as dependency."""
    model.parse(fp_cavity_script)
    model.parse("gauss gL0 L0.p1.o w0=1.2m z=-1.2")

    model.beam_trace()

    gauss_tree = ctracer.TraceTree.from_node(
        model.L0.p1.o, model.gL0, symmetric=True, is_gauss=True,
    )

    forest = [gauss_tree]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_fp_single_gauss_at_laser_reversed_forest(model, fp_cavity_script):
    """Check forest structure for simple FP cavity file with single Gauss object,
    positioned at Laser output but reversed into the Laser, as dependency."""
    model.parse(fp_cavity_script)
    model.parse("gauss gL0 L0.p1.i w0=1.2m z=1.2")

    model.beam_trace()

    gauss_tree_single = ctracer.TraceTree.from_node(
        model.L0.p1.i, model.gL0, symmetric=True, is_gauss=True,
    )
    gauss_tree_forward = ctracer.TraceTree.from_node(
        model.L0.p1.o, model.gL0, symmetric=True, is_gauss=True,
    )

    forest = [gauss_tree_single, gauss_tree_forward]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_fp_cavity_with_laser_gauss_forest__implicit_order(model, fp_cavity_script):
    """Check forest structure for simple FP cavity file with Gauss object, positioned at
    Laser output, and Cavity object as dependencies.

    No tracing priorities given, using implicit ordering.
    """
    model.parse(fp_cavity_script)
    model.parse(
        """
    cav FP ITM.p2
    gauss gL0 L0.p1.o w0=1.2m z=-1.2
    """
    )

    model.beam_trace()

    internal_cav_tree = ctracer.TraceTree.from_cavity(model.FP)
    external_tree_out = ctracer.TraceTree.from_node(
        model.ETM.p2.o, model.FP, symmetric=True, pre_node=model.ETM.p1.i,
    )
    gauss_tree = ctracer.TraceTree.from_node(
        model.L0.p1.o,
        model.gL0,
        symmetric=True,
        is_gauss=True,
        exclude=model.FP.path.nodes_only,
    )

    forest = [internal_cav_tree, external_tree_out, gauss_tree]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_fp_cavity_with_laser_gauss_forest__explicit_order(model, fp_cavity_script):
    """Check forest structure for simple FP cavity file with Gauss object, positioned at
    Laser output, and Cavity object as dependencies.

    Set Gauss object as highest priority.
    """
    model.parse(fp_cavity_script)
    model.parse(
        """
    cav FP ITM.p2
    gauss gL0 L0.p1.o w0=1.2m z=-1.2 priority=1
    """
    )

    model.beam_trace()

    internal_cav_tree = ctracer.TraceTree.from_cavity(model.FP)
    external_tree_out = ctracer.TraceTree.from_node(
        model.ETM.p2.o, model.FP, symmetric=True, pre_node=model.ETM.p1.i,
    )
    gauss_tree = ctracer.TraceTree.from_node(
        model.L0.p1.o,
        model.gL0,
        symmetric=True,
        is_gauss=True,
        exclude=model.FP.path.nodes_only,
    )

    forest = [internal_cav_tree, gauss_tree, external_tree_out]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_fp_single_gauss_at_back_of_cavity(model, fp_cavity_script):
    """Check forest structure for simple FP cavity file with single Gauss object,
    positioned at the rear of the cavity, as dependency."""
    model.parse(fp_cavity_script)
    model.parse("gauss gL0 ETM.p2.i w0=1.2m z=-1.2")

    model.beam_trace()

    gauss_tree = ctracer.TraceTree.from_node(
        model.ETM.p2.i, model.gL0, symmetric=True, is_gauss=True,
    )

    forest = [gauss_tree]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_fp_cavity_with_gauss_at_back(model, fp_cavity_script):
    """Check forest structure for simple FP cavity file with Gauss object, positioned at
    rear of cavity, and Cavity object as dependencies.

    No tracing priorities given, using implicit ordering.
    """
    model.parse(fp_cavity_script)
    model.parse(
        """
    cav FP ITM.p2
    gauss gL0 ETM.p2.i w0=1.2m z=-1.2
    """
    )

    model.beam_trace()

    internal_cav_tree = ctracer.TraceTree.from_cavity(model.FP)
    external_tree_back = ctracer.TraceTree.from_node(
        model.ITM.p1.o, model.FP, symmetric=True, pre_node=model.ITM.p2.i,
    )
    gauss_tree = ctracer.TraceTree.from_node(
        model.ETM.p2.i,
        model.gL0,
        symmetric=True,
        is_gauss=True,
        exclude=model.FP.path.nodes_only,
    )

    forest = [internal_cav_tree, external_tree_back, gauss_tree]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_fp_cavity_with_gauss_in_cavity_logs_error(model, fp_cavity_script, caplog):
    """Test that putting a Gauss object inside a Cavity path logs an error and continues
    without Gauss."""
    model.parse(fp_cavity_script)
    model.parse(
        """
    cav FP ITM.p2
    gauss gL0 ITM.p2.o w0=1.2m z=-1.2
    """
    )

    with caplog.at_level(logging.ERROR):
        model.beam_trace()

        assert "Ignoring this Gauss." in caplog.text

    internal_cav_tree = ctracer.TraceTree.from_cavity(model.FP)
    external_tree_out = ctracer.TraceTree.from_node(
        model.ETM.p2.o, model.FP, symmetric=True, pre_node=model.ETM.p1.i,
    )
    external_tree_back = ctracer.TraceTree.from_node(
        model.ITM.p1.o, model.FP, symmetric=True, pre_node=model.ITM.p2.i,
    )

    forest = [internal_cav_tree, external_tree_out, external_tree_back]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_fp_single_cavity_unstable_raises_exception(model, fp_cavity_script):
    """Test that Fabry-Perot cavity file with cavity unstable raises
    BeamTraceException."""
    model.parse(fp_cavity_script)
    model.elements["CAV"].L = 20
    model.parse("cav FP ITM.p2")

    with pytest.raises(BeamTraceException):
        model.beam_trace()


def test_fp_gauss_at_laser_and_unstable_cavity_forest(model, fp_cavity_script, caplog):
    """Check forest structure for simple FP cavity file with Gauss object, positioned at
    Laser output, as dependency and an unstable cavity."""
    model.parse(fp_cavity_script)
    model.elements["CAV"].L = 20
    model.parse(
        """
    cav FP ITM.p2
    gauss gL0 L0.p1.o w0=1.2m z=-1.2
    """
    )

    with caplog.at_level(logging.WARNING):
        model.beam_trace()

        assert "The cavities ['FP'] are unstable" in caplog.text

    gauss_tree = ctracer.TraceTree.from_node(
        model.L0.p1.o, model.gL0, symmetric=True, is_gauss=True,
    )

    forest = [gauss_tree]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


##### Michelson (no recycling) tests #####


@pytest.fixture(scope="module")
def michelson_fp_script():
    return """
    l L0 P=1
    s s0 L0.p1 BS.p1 L=10

    bs BS

    s sY BS.p2 ITMY.p1 L=100

    m ITMY R=0.99 T=0.01 Rc=-5580
    s LY ITMY.p2 ETMY.p1 L=10k
    m ETMY R=0.99 T=0.01 Rc=5580

    s sX BS.p3 ITMX.p1 L=50

    m ITMX R=0.99 T=0.01 Rc=-5580
    s LX ITMX.p2 ETMX.p1 L=10k
    m ETMX R=0.99 T=0.01 Rc=5580
    """


def test_mfp_forest_xy_arm_cavities__implicit_order(model, michelson_fp_script):
    """Check forest structure for Michelson with both ARM cavities.

    No priorities given so using implicit order.
    """
    model.parse(michelson_fp_script)
    model.parse(
        """
    cav FPX ITMX.p2
    cav FPY ITMY.p2
    """
    )
    model.beam_trace()

    internal_Xcav_tree = ctracer.TraceTree.from_cavity(model.FPX)
    internal_Ycav_tree = ctracer.TraceTree.from_cavity(model.FPY)

    external_Xcav_out = ctracer.TraceTree.from_node(
        model.ETMX.p2.o, model.FPX, symmetric=True, pre_node=model.ETMX.p1.i,
    )
    external_Xcav_back = ctracer.TraceTree.from_node(
        model.ITMX.p1.o, model.FPX, symmetric=True, pre_node=model.ITMX.p2.i,
    )

    external_Ycav_out = ctracer.TraceTree.from_node(
        model.ETMY.p2.o, model.FPY, symmetric=True, pre_node=model.ETMY.p1.i,
    )
    external_Ycav_back = ctracer.TraceTree.from_node(
        model.ITMY.p1.o,
        model.FPY,
        symmetric=True,
        pre_node=model.ITMY.p2.i,
        exclude=[model.BS.p1.o, model.BS.p4.o],
    )

    forest = [
        internal_Xcav_tree,
        internal_Ycav_tree,
        external_Xcav_out,
        external_Xcav_back,
        external_Ycav_out,
        external_Ycav_back,
    ]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_mfp_forest_xy_arm_cavities__explicit_order(model, michelson_fp_script):
    """Check forest structure for Michelson with both ARM cavities.

    Set YARM as highest priority.
    """
    model.parse(michelson_fp_script)
    model.parse(
        """
    cav FPX ITMX.p2
    cav FPY ITMY.p2 priority=2
    """
    )
    model.beam_trace()

    internal_Xcav_tree = ctracer.TraceTree.from_cavity(model.FPX)
    internal_Ycav_tree = ctracer.TraceTree.from_cavity(model.FPY)

    external_Xcav_out = ctracer.TraceTree.from_node(
        model.ETMX.p2.o, model.FPX, symmetric=True, pre_node=model.ETMX.p1.i,
    )
    external_Xcav_back = ctracer.TraceTree.from_node(
        model.ITMX.p1.o,
        model.FPX,
        symmetric=True,
        pre_node=model.ITMX.p2.i,
        exclude=[model.BS.p1.o, model.BS.p4.o],
    )

    external_Ycav_out = ctracer.TraceTree.from_node(
        model.ETMY.p2.o, model.FPY, symmetric=True, pre_node=model.ETMY.p1.i,
    )
    external_Ycav_back = ctracer.TraceTree.from_node(
        model.ITMY.p1.o, model.FPY, symmetric=True, pre_node=model.ITMY.p2.i,
    )

    forest = [
        internal_Ycav_tree,
        internal_Xcav_tree,
        external_Ycav_out,
        external_Ycav_back,
        external_Xcav_out,
        external_Xcav_back,
    ]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_mfp_forest_gauss_laser(model, michelson_fp_script):
    """Check forest structure for Michelson with neither ARM cavity, but single gauss at
    laser output."""
    model.parse(michelson_fp_script)
    model.parse("gauss gL0 L0.p1.o w0=1.2m z=-1.2")
    model.beam_trace()

    gauss_tree = ctracer.TraceTree.from_node(
        model.L0.p1.o, model.gL0, symmetric=True, is_gauss=True,
    )
    gauss_bs_branch_tree = ctracer.TraceTree.from_node(
        model.BS.p3.i, model.gL0, symmetric=True, exclude=[model.BS.p1.o,],
    )

    forest = [
        gauss_tree,
        gauss_bs_branch_tree,
    ]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_mfp_forest_xy_arm_cavities_gauss_laser__implicit_order(
    model, michelson_fp_script
):
    """Check forest structure for Michelson with both ARM cavities and a gauss at the
    laser.

    No priorities given so using implicit order.
    """
    model.parse(michelson_fp_script)
    model.parse(
        """
    cav FPX ITMX.p2.o
    cav FPY ITMY.p2.o
    gauss gL0 L0.p1.o w0=1.2m z=-1.2
    """
    )
    model.beam_trace()

    internal_Xcav_tree = ctracer.TraceTree.from_cavity(model.FPX)
    internal_Ycav_tree = ctracer.TraceTree.from_cavity(model.FPY)

    external_Xcav_out = ctracer.TraceTree.from_node(
        model.ETMX.p2.o, model.FPX, symmetric=True, pre_node=model.ETMX.p1.i,
    )
    external_Xcav_back = ctracer.TraceTree.from_node(
        model.ITMX.p1.o,
        model.FPX,
        symmetric=True,
        pre_node=model.ITMX.p2.i,
        exclude=[model.BS.p1.o],
    )

    external_Ycav_out = ctracer.TraceTree.from_node(
        model.ETMY.p2.o, model.FPY, symmetric=True, pre_node=model.ETMY.p1.i,
    )
    external_Ycav_back = ctracer.TraceTree.from_node(
        model.ITMY.p1.o,
        model.FPY,
        symmetric=True,
        pre_node=model.ITMY.p2.i,
        exclude=[model.BS.p1.o, model.BS.p4.o],
    )
    gtree_exclude = model.FPX.path.nodes_only + model.FPY.path.nodes_only
    gtree_exclude += [model.BS.p2.o, model.ITMY.p1.i, model.BS.p3.o, model.ITMX.p1.i]
    gauss_tree = ctracer.TraceTree.from_node(
        model.L0.p1.o, model.gL0, symmetric=True, is_gauss=True, exclude=gtree_exclude,
    )

    forest = [
        internal_Xcav_tree,
        internal_Ycav_tree,
        external_Xcav_out,
        external_Xcav_back,
        external_Ycav_out,
        external_Ycav_back,
        gauss_tree,
    ]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_mfp_forest_xy_arm_cavities_gauss_laser__explicit_order1(
    model, michelson_fp_script
):
    """Check forest structure for Michelson with both ARM cavities and a gauss at the
    laser.

    Gauss has higher priority than both cavities.
    """
    model.parse(michelson_fp_script)
    model.parse(
        """
    cav FPX ITMX.p2.o
    cav FPY ITMY.p2.o
    gauss gL0 L0.p1.o w0=1.2m z=-1.2 priority=1
    """
    )
    model.beam_trace()

    internal_Xcav_tree = ctracer.TraceTree.from_cavity(model.FPX)
    internal_Ycav_tree = ctracer.TraceTree.from_cavity(model.FPY)

    external_Xcav_out = ctracer.TraceTree.from_node(
        model.ETMX.p2.o, model.FPX, symmetric=True, pre_node=model.ETMX.p1.i,
    )

    external_Ycav_out = ctracer.TraceTree.from_node(
        model.ETMY.p2.o, model.FPY, symmetric=True, pre_node=model.ETMY.p1.i,
    )

    gtree_exclude = model.FPX.path.nodes_only + model.FPY.path.nodes_only
    gauss_tree = ctracer.TraceTree.from_node(
        model.L0.p1.o, model.gL0, symmetric=True, is_gauss=True, exclude=gtree_exclude,
    )
    gauss_bs_branch_tree = ctracer.TraceTree.from_node(
        model.BS.p3.i, model.gL0, symmetric=True, exclude=[model.BS.p1.o,],
    )

    forest = [
        internal_Xcav_tree,
        internal_Ycav_tree,
        gauss_tree,
        external_Xcav_out,
        external_Ycav_out,
        gauss_bs_branch_tree,
    ]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_mfp_forest_xy_arm_cavities_gauss_laser__explicit_order2(
    model, michelson_fp_script
):
    """Check forest structure for Michelson with both ARM cavities and a gauss at the
    laser.

    XARM cavity has highest priority, followed by Gauss then YARM last as implicit.
    """
    model.parse(michelson_fp_script)
    model.parse(
        """
    cav FPX ITMX.p2.o priority=2
    cav FPY ITMY.p2.o
    gauss gL0 L0.p1.o w0=1.2m z=-1.2 priority=1
    """
    )
    model.beam_trace()

    internal_Xcav_tree = ctracer.TraceTree.from_cavity(model.FPX)
    internal_Ycav_tree = ctracer.TraceTree.from_cavity(model.FPY)

    external_Xcav_out = ctracer.TraceTree.from_node(
        model.ETMX.p2.o, model.FPX, symmetric=True, pre_node=model.ETMX.p1.i,
    )
    external_Xcav_back = ctracer.TraceTree.from_node(
        model.ITMX.p1.o,
        model.FPX,
        symmetric=True,
        pre_node=model.ITMX.p2.i,
        exclude=[model.BS.p1.o],
    )

    external_Ycav_out = ctracer.TraceTree.from_node(
        model.ETMY.p2.o, model.FPY, symmetric=True, pre_node=model.ETMY.p1.i,
    )

    gtree_exclude = model.FPX.path.nodes_only + model.FPY.path.nodes_only
    gtree_exclude += [
        model.BS.p3.o,
    ]
    gauss_tree = ctracer.TraceTree.from_node(
        model.L0.p1.o, model.gL0, symmetric=True, is_gauss=True, exclude=gtree_exclude,
    )

    forest = [
        internal_Xcav_tree,
        internal_Ycav_tree,
        external_Xcav_out,
        external_Xcav_back,
        gauss_tree,
        external_Ycav_out,
    ]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_mfp_forest_only_xarm(model, michelson_fp_script):
    """Check forest structure for Michelson with only XARM cavity.

    This tests that branching at beam splitters --- from BS.p1 -> yarm branch.
    """
    model.parse(michelson_fp_script)
    model.parse(
        """
    cav FPX ITMX.p2
    """
    )
    model.beam_trace()

    internal_Xcav_tree = ctracer.TraceTree.from_cavity(model.FPX)

    external_Xcav_out = ctracer.TraceTree.from_node(
        model.ETMX.p2.o, model.FPX, symmetric=True, pre_node=model.ETMX.p1.i,
    )
    external_Xcav_back = ctracer.TraceTree.from_node(
        model.ITMX.p1.o, model.FPX, symmetric=True, pre_node=model.ITMX.p2.i,
    )
    branch_to_yarm_tree = ctracer.TraceTree.from_node(
        model.BS.p1.i, model.FPX, symmetric=True, exclude=[model.BS.p3.o],
    )

    forest = [
        internal_Xcav_tree,
        external_Xcav_out,
        external_Xcav_back,
        branch_to_yarm_tree,
    ]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_mfp_forest_only_yarm(model, michelson_fp_script):
    """Check forest structure for Michelson with only YARM cavity.

    This tests that branching at beam splitters --- from BS.p4 -> xarm branch.
    """
    model.parse(michelson_fp_script)
    model.parse(
        """
    cav FPY ITMY.p2
    """
    )
    model.beam_trace()

    internal_Ycav_tree = ctracer.TraceTree.from_cavity(model.FPY)

    external_Ycav_out = ctracer.TraceTree.from_node(
        model.ETMY.p2.o, model.FPY, symmetric=True, pre_node=model.ETMY.p1.i,
    )
    external_Ycav_back = ctracer.TraceTree.from_node(
        model.ITMY.p1.o, model.FPY, symmetric=True, pre_node=model.ITMY.p2.i,
    )
    branch_to_xarm_tree = ctracer.TraceTree.from_node(
        model.BS.p4.i, model.FPY, symmetric=True, exclude=[model.BS.p2.o],
    )

    forest = [
        internal_Ycav_tree,
        external_Ycav_out,
        external_Ycav_back,
        branch_to_xarm_tree,
    ]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


##### Linear coupled cavity (with no overlapping) tests #####


@pytest.fixture(scope="module")
def linear_coupled_cav_script():
    return """
    l L0 P=1

    s s0 L0.p1 ITM.p1

    m ITM R=0.99 T=0.01 Rc=-2
    s sc1 ITM.p2 CTM.p1 L=1
    m CTM R=0.99 T=0.01 Rc=2
    s sc2 CTM.p2 ETM.p1 L=2
    m ETM R=0.99 T=0.01 Rc=2.2
    """


def test_linear_coupled_cavity_implicit_ordering(model, linear_coupled_cav_script):
    """Test a linear coupled cavity forest structure for two sub-cavities defined with
    implicit trace ordering."""
    model.parse(linear_coupled_cav_script)
    model.parse(
        """
    cav SUB1 ITM.p2
    cav SUB2 CTM.p2
    """
    )
    model.beam_trace()

    internal_sub1_tree = ctracer.TraceTree.from_cavity(model.SUB1)
    internal_sub2_tree = ctracer.TraceTree.from_cavity(model.SUB2)

    external_sub1_back = ctracer.TraceTree.from_node(
        model.ITM.p1.o, model.SUB1, symmetric=True, pre_node=model.ITM.p2.i,
    )
    external_sub2_out = ctracer.TraceTree.from_node(
        model.ETM.p2.o, model.SUB2, symmetric=True, pre_node=model.ETM.p1.i,
    )

    forest = [
        internal_sub1_tree,
        internal_sub2_tree,
        external_sub1_back,
        external_sub2_out,
    ]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


def test_linear_coupled_cavity_explicit_ordering(model, linear_coupled_cav_script):
    """Test a linear coupled cavity forest structure for two sub-cavities defined with
    explicit trace ordering."""
    model.parse(linear_coupled_cav_script)
    model.parse(
        """
    cav SUB1 ITM.p2 priority=-1
    cav SUB2 CTM.p2
    """
    )
    model.beam_trace()

    internal_sub1_tree = ctracer.TraceTree.from_cavity(model.SUB1)
    internal_sub2_tree = ctracer.TraceTree.from_cavity(model.SUB2)

    external_sub1_back = ctracer.TraceTree.from_node(
        model.ITM.p1.o, model.SUB1, symmetric=True, pre_node=model.ITM.p2.i,
    )
    external_sub2_out = ctracer.TraceTree.from_node(
        model.ETM.p2.o, model.SUB2, symmetric=True, pre_node=model.ETM.p1.i,
    )

    forest = [
        internal_sub2_tree,
        internal_sub1_tree,
        external_sub2_out,
        external_sub1_back,
    ]

    assert len(forest) == len(model.trace_forest.forest)

    for tree, ttree in zip(forest, model.trace_forest.forest):
        assert_trace_trees_equal(tree, ttree)


# TODO (sjr) Overlapping cavities forest tests should be in a separate file as they
#            can get quite complicated, so need a whole suite of tests just for these

# TODO (sjr) Asymmetric tracing forest tests are a whole different ball game and also
#            need another file as these require another whole suite of tests


# TODO (sjr) More configurations for this file but main things to focus on are:
#
# - Different cavity types: i.e. triangular and bow-tie cavities
# - Configurations with AR + HR surfaces
# - Full Beamsplitter substrate
# - Telescopes / folded cavities
#
