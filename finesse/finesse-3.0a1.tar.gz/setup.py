"""Setup file."""
from setuptools import setup, find_packages
import os
import sys
import platform
from Cython.Build import build_ext, cythonize
from Cython.Distutils import Extension

SYS_NAME = platform.system()


def get_conda_paths():
    try:
        library = sys.prefix
        # library = os.environ["CONDA_PREFIX"]
        if sys.platform == "win32":
            library = os.path.join(library, "Library")
        return (os.path.join(library, "include"), os.path.join(library, "lib"))
    except KeyError:
        return (None, None)


def make_extension(relpath, **kwargs):
    import numpy as np

    root_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "src")
    finesse_dir = os.path.join(root_dir, "finesse")

    def construct_ext_name(rp):
        names = []
        leading, trailing = os.path.split(rp)

        while trailing != "":
            names.append(trailing)

            leading, trailing = os.path.split(leading)

        names.reverse()
        if names[-1].endswith(".pyx"):
            names[-1] = names[-1].split(".")[0]

        return ".".join(names)

    # The optional arguments consisting of various directories,
    # macros, compilation args, etc. that will be passed to
    # Extension object constructor
    ext_args = {
        "include_dirs": [],
        "define_macros": [],
        "undef_macros": [],
        "library_dirs": [],
        "libraries": [],
        "runtime_library_dirs": [],
        "extra_objects": [],
        "extra_compile_args": [],
        "extra_link_args": [],
        "export_symbols": [],
        "cython_include_dirs": [],
        "cython_directives": [],
    }
    ### Setting up some global options that need to be passed ###
    ###                   to all extensions                   ###

    include_dirs = ext_args.get("include_dirs")
    # Include the src/finesse and NumPy header file directories
    include_dirs.extend([finesse_dir, np.get_include()])

    # Now ensure suitesparse headers get included
    USR_SUITESPARSE_PATH = "/usr/include/suitesparse"
    if os.path.exists(USR_SUITESPARSE_PATH):
        include_dirs.append(USR_SUITESPARSE_PATH)

    # Grab the paths to suitesparse from conda if using this
    conda_include, conda_lib = get_conda_paths()
    if conda_include is not None:
        CONDA_SUITESPARSE_PATH = os.path.join(conda_include, "suitesparse")
        if os.path.exists(CONDA_SUITESPARSE_PATH):
            include_dirs.append(CONDA_SUITESPARSE_PATH)

        include_dirs.append(conda_include)
        ext_args.get("library_dirs").append(conda_lib)

    # define_macros = ext_args.get("define_macros")
    # define_macros.extend(
    #     [
    #         # Stops numpy version warning, cython uses an older API on purpose
    #         ("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION"),
    #     ]
    # )

    extra_compile_args = ext_args.get("extra_compile_args")
    extra_compile_args.extend(
        [
            "-O3",
            # Inlined cpdef functions in finesse.cymath extensions complain
            # about not being used (they are used outside of these extensions)
            # so we suppress these warnings for the moment
            "-Wno-unused-function",
            "-Wno-unused-variable",
            # "-DCYTHON_WITHOUT_ASSERTIONS",
        ]
    )

    ### Now adding the optional extra args needed for this specific extension ###

    for arg_opt, arg_list in ext_args.items():
        extra_args = kwargs.get(arg_opt)
        if extra_args:
            if isinstance(extra_args, str):
                extra_args = [extra_args]

            arg_list += extra_args

    ext_name = "finesse." + construct_ext_name(relpath)
    sources = [os.path.join(finesse_dir, relpath)]

    return Extension(ext_name, sources, language="c", **ext_args,)


def ext_modules():
    # Argument pattern for extensions requiring OpenMP
    if SYS_NAME == "Darwin":
        open_mp_args = {
            "extra_compile_args": ["-Xpreprocessor", "-fopenmp"],
            "extra_link_args": ["-liomp5"],
        }
    else:
        open_mp_args = {"extra_compile_args": "-fopenmp", "extra_link_args": "-fopenmp"}

    # Argument pattern for extensions using KLU
    cmatrix_args = {"libraries": "klu"}

    # The argument patterns that get passed to all extensions
    default_ext_args = {}

    COVERAGE_MODE = "--coverage" in sys.argv
    if COVERAGE_MODE:
        # If we're in coverage report mode, then add the trace
        # macros to all extensions so that proper line tracing
        # is performed
        default_ext_args["define_macros"] = [
            ("CYTHON_TRACE", "1"),
            ("CYTHON_TRACE_NOGIL", "1"),
        ]

    # NOTE (sjr) Pass any extra arguments that a specific extension needs via a
    #            dict of the arg names: values here. See ext_args in make_extension
    #            function above for the options.
    ext_args = [
        ("enums.pyx", default_ext_args),
        ("cymath/complex.pyx", default_ext_args),
        ("cymath/math.pyx", default_ext_args),
        ("cymath/gaussbeam.pyx", default_ext_args),
        ("cymath/homs.pyx", {**default_ext_args, **open_mp_args}),
        ("tree.pyx", default_ext_args),
        ("constants.pyx", default_ext_args),
        ("frequency.pyx", default_ext_args),
        ("symbols.pyx", default_ext_args),
        ("parameter.pyx", default_ext_args),
        ("cyexpr.pyx", default_ext_args),
        ("element.pyx", default_ext_args),
        ("cmatrix.pyx", {**default_ext_args, **cmatrix_args}),
        ("knm/matrix.pyx", default_ext_args),
        ("knm/bayerhelms.pyx", {**default_ext_args, **open_mp_args}),
        ("simulations/base.pyx", default_ext_args),
        ("simulations/basematrix.pyx", default_ext_args),
        ("simulations/KLU.pyx", default_ext_args),
        ("components/workspace.pyx", default_ext_args),
        ("components/mechanical.pyx", default_ext_args),
        ("components/modal/*.pyx", default_ext_args),
        ("detectors/workspace.pyx", default_ext_args),
        ("detectors/compute/amplitude.pyx", default_ext_args),
        ("detectors/compute/camera.pyx", {**default_ext_args, **open_mp_args}),
        ("detectors/compute/power.pyx", {**default_ext_args, **open_mp_args}),
        ("detectors/compute/quantum.pyx", default_ext_args),
        ("detectors/compute/gaussian.pyx", default_ext_args),
        ("tracing/ctracer.pyx", default_ext_args),
        ("tracing/cytools.pyx", default_ext_args),
        ("analysis/runners.pyx", default_ext_args),
        ("solutions/base.pyx", default_ext_args),
        ("solutions/array.pyx", default_ext_args),
        ("utilities/cyomp.pyx", {**default_ext_args, **open_mp_args}),
    ]

    exts = []
    for ext_rel_path, args in ext_args:
        exts.append(make_extension(os.path.normpath(ext_rel_path), **args))

    if (SYS_NAME == "Windows") or (SYS_NAME == "Darwin"):
        num_jobs = 0
    else:
        num_jobs = os.cpu_count()

    # See https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#compiler-directives
    # for in-depth details on the options for compiler directives
    compiler_directives = {
        # Embeds call signature in docstring of Python visible functions
        "embedsignature": True,
        # No checks are performed on division by zero (for big perfomance boost)
        "cdivision": True,
    }

    # If coverage mode is set the ensure line tracing
    # is switched on for all extensions
    if COVERAGE_MODE:
        compiler_directives["linetrace"] = True
        sys.argv.remove("--coverage")

    # If debug mode is set then ensure profiling
    # is switched on for all extensions
    DEBUG_MODE = "--debug" in sys.argv
    if DEBUG_MODE:
        compiler_directives["profile"] = True
        sys.argv.remove("--debug")

    return cythonize(
        exts,
        # Produces HTML files showing level of CPython interaction
        # per-line of each Cython extension (.pyx) file
        annotate=True,
        language_level=3,
        nthreads=num_jobs,
        compiler_directives=compiler_directives,
        gdb_debug=True,
    )


### NOTE See https://finesse.readthedocs.io/en/latest/developer/codeguide/requirements.html

REQUIRES = [
    "numpy",
    "scipy",
    "matplotlib",
    "cython",
    "sympy",
    "networkx",
    "sly",
    "h5py",
    "click",
    "click-default-group",
    "tabulate",
    "deprecated",
]

EXTRAS = {
    "dev": [
        "sphinx",
        "sphinx_rtd_theme",
        # Can't use latest sphinxcontrib-bibtex version due to a dependency incompatibility as of
        # 2020-12-14 (https://github.com/executablebooks/jupyter-book/issues/1137). The version
        # pinning can be removed once Jupyter Book > 0.8.3 is released.
        "sphinxcontrib-bibtex < 2.0.0",
        "sphinxcontrib-katex",
        "sphinxcontrib-svg2pdfconverter",
        "sphinxcontrib-programoutput",
        "jupyter-sphinx",
        "numpydoc",
        "pytest",
        "pytest-cov",
        # Can't use latest coverage version due to Cython bug as of 2020-11-26
        # (https://github.com/cython/cython/issues/3515).
        "coverage == 4.5.4",
        "pycobertura",
        "Faker",
        "black",
        "pre-commit",
        "pylint",
        "flake8",
        "flake8-bugbear",
        "doc8",
        "hypothesis",
        "reslate",
    ],
    "graphviz": ["pygraphviz",],
}

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Topic :: Scientific/Engineering :: Physics",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Operating System :: MacOS",
]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def parallelise_build():
    import warnings
    from concurrent.futures import ProcessPoolExecutor
    from concurrent.futures.process import BrokenProcessPool

    def build_extensions(self):
        """Function to monkey-patch Cython.Build.build_ext.build_extensions to build
        extensions in parallel."""
        self.check_extensions_list(self.extensions)
        num_jobs = os.cpu_count()
        try:
            with ProcessPoolExecutor(max_workers=num_jobs) as pool:
                # results = pool.map(self.build_extension, self.extensions)
                pool.map(self.build_extension, self.extensions)
        # TODO [adf] check which exception could be used to start sequential build
        except BrokenProcessPool:
            for ex in self.extensions:
                self.build_extension(ex)
        # TODO [adf] this does not raise an error when the build fails, so
        # it still looks like everything works with pip install
        # else:
        #    try:
        #        print(list(results))
        #    except (Exception, BrokenProcessPool):
        #        raise RuntimeError("Could not compile extension, maybe missing a dependency")

    warnings.warn(
        "Cython is monkey-patched to parallelise the build. If you encounter any issues, this "
        "behaviour can be disabled in setup.py."
    )
    build_ext.build_extensions = build_extensions


# Parallel build behaves strangely on Windows and Mac OSX so enable it only for Linux.
# See #272.
if __name__ == "__main__" and SYS_NAME == "Linux":
    parallelise_build()


setup(
    # package descriptions
    name="finesse",
    description=("A simulation tool for modelling laser interferometers"),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://www.gwoptics.org/finesse",
    author_email="finesse-support@nikhef.nl",
    project_urls={
        "Bug Tracker": "https://git.ligo.org/finesse/finesse3/issues",
        "Documentation": "https://finesse.docs.ligo.org/finesse3",
        "Source Code": "https://git.ligo.org/finesse/finesse3",
    },
    # packages and extensions
    packages=find_packages("src"),
    package_dir={"": "src"},
    ext_modules=ext_modules(),
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    package_data={
        "finesse": [
            "plotting/style/*.mplstyle",
            "finesse.ini",  # Base config file.
            "usr.ini.dist",  # Barebone user config file.
        ]
    },
    # requirements
    python_requires=">=3.8",
    install_requires=REQUIRES,
    setup_requires=["setuptools_scm", "numpy"],
    extras_require=EXTRAS,
    # other
    license="GPL",
    classifiers=CLASSIFIERS,
    # CLI
    entry_points={
        "console_scripts": ["kat3 = finesse.__main__:cli"],
        "pygments.lexers": [
            "KatScript = finesse.script.highlighter:KatScriptPygmentsLexer",
            "KatScriptInPython = finesse.script.highlighter:KatScriptSubstringPygmentsLexer",
        ],
    },
)
