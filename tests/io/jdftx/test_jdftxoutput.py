from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from pymatgen.io.jdftx.outputs import JDFTXOutputs, implemented_store_vars

from .outputs_test_utils import (
    n2_ex_calc_dir,
    n2_ex_calc_dir_bandprojections_metadata,
    n2_ex_calc_dir_known_paths,
    nh3_ex_calc_dir,
    nh3_ex_calc_dir_bandprojections_metadata,
    nh3_ex_calc_dir_known_paths,
)
from .shared_test_utils import assert_same_value

if TYPE_CHECKING:
    from pathlib import Path


@pytest.mark.parametrize(
    ("calc_dir", "known_paths"),
    [(n2_ex_calc_dir, n2_ex_calc_dir_known_paths), (nh3_ex_calc_dir, nh3_ex_calc_dir_known_paths)],
)
def test_known_paths(calc_dir: Path, known_paths: dict):
    """Test that the known paths are correct."""
    jo = JDFTXOutputs.from_calc_dir(calc_dir)
    for path_type, path in known_paths.items():
        assert jo.paths[path_type] == path


@pytest.mark.parametrize(
    ("calc_dir", "store_vars"),
    [
        (n2_ex_calc_dir, ["bandProjections", "eigenvals"]),
        (n2_ex_calc_dir, ["bandProjections"]),
        (n2_ex_calc_dir, []),
    ],
)
def test_store_vars(calc_dir: Path, store_vars: list[str]):
    """Test that the stored variables are correct."""
    jo = JDFTXOutputs.from_calc_dir(calc_dir, store_vars=store_vars)
    for var in implemented_store_vars:
        assert hasattr(jo, var)
        if var in store_vars:
            assert getattr(jo, var) is not None
        else:
            assert getattr(jo, var) is None


@pytest.mark.parametrize(
    ("calc_dir", "known_metadata"),
    [
        (n2_ex_calc_dir, n2_ex_calc_dir_bandprojections_metadata),
        (nh3_ex_calc_dir, nh3_ex_calc_dir_bandprojections_metadata),
    ],
)
def test_store_bandprojections(calc_dir: Path, known_metadata: dict):
    """Test that the stored band projections are correct."""
    jo = JDFTXOutputs.from_calc_dir(calc_dir, store_vars=["bandProjections"])
    for var in known_metadata:
        assert hasattr(jo.bandProjections, var)
        assert_same_value(getattr(jo.bandProjections, var), known_metadata[var])
