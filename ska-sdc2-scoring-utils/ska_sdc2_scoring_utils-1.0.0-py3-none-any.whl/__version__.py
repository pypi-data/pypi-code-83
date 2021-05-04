"""The current package version.

This follows the Semantic Versioning (https://semver.org/) standard.

Standard version numbers look like `X.Y.Z` and this translates to:

* `X` major release: adds changes incompatible with prior major releases.
* `Y` minor release: adds new functionality and bug fixes in a backwards
   compatible manner.
* `Z` is a patch release: adds backwards compatible bug fixes.

Exception: version < 1.0 may introduce backwards-incompatible changes in
a minor release.

In addition to the standard version, pre-releases are identified by a
segment (suffix) following the release version, which consists of an
alphabetical identifier followed by with a non-negative integer value.

* `X.Y.ZaN` indicates an **alpha** release.
* `X.Y.ZbN` indicates an **beta** release.
* `X.Y.ZrcN` indicates a **release candidate**.

Pre-releases are ordered by phase (alpha, beta, release candidate)
and then by numerical component.

"""
__version__ = "1.0.0"
