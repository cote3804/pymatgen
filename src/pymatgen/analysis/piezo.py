"""This module provides classes for the Piezoelectric tensor."""

from __future__ import annotations

import warnings
from typing import TYPE_CHECKING

import numpy as np

from pymatgen.core.tensors import Tensor

if TYPE_CHECKING:
    from numpy.typing import ArrayLike
    from typing_extensions import Self

__author__ = "Shyam Dwaraknath"
__copyright__ = "Copyright 2016, The Materials Project"
__version__ = "1.0"
__maintainer__ = "Shyam Dwaraknath"
__email__ = "shyamd@lbl.gov"
__status__ = "Development"
__date__ = "Feb, 2016"


class PiezoTensor(Tensor):
    """This class describes the 3x6 piezo tensor in Voigt notation."""

    def __new__(cls, input_array: ArrayLike, tol: float = 1e-3) -> Self:
        """
        Create an PiezoTensor object. The constructor throws an error if
        the shape of the input_matrix argument is not 3x3x3, i.e. in true
        tensor notation. Note that the constructor uses __new__ rather than
        __init__ according to the standard method of subclassing numpy
        ndarrays.

        Args:
            input_matrix (3x3x3 array-like): the 3x6 array-like
                representing the piezo tensor
        """
        obj = super().__new__(cls, input_array, check_rank=3)
        if not np.allclose(obj, np.transpose(obj, (0, 2, 1)), atol=tol, rtol=0):
            warnings.warn("Input piezo tensor does not satisfy standard symmetries", stacklevel=2)
        return obj.view(cls)

    @classmethod
    def from_vasp_voigt(cls, input_vasp_array: ArrayLike) -> Self:
        """
        Args:
            input_vasp_array (ArrayLike): Voigt form of tensor.

        Returns:
            PiezoTensor
        """
        voigt_map = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]
        input_vasp_array = np.array(input_vasp_array)
        rank = 3

        pt = np.zeros([rank, 3, 3])
        for dim in range(rank):
            for pos, val in enumerate(voigt_map):
                pt[dim][val] = input_vasp_array[dim][pos]
                pt[dim].T[val] = input_vasp_array[dim][pos]

        return cls(pt)
