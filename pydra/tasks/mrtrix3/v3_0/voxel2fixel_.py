import typing as ty
from pathlib import Path  # noqa: F401
from fileformats.generic import File, Directory  # noqa: F401
from fileformats.medimage_mrtrix3 import ImageIn, ImageOut, Tracks  # noqa: F401
from pydra.engine import specs, ShellCommandTask


input_fields = [
    # Arguments
    (
        "image_in",
        ImageIn,
        {
            "argstr": "",
            "position": 0,
            "help_string": """the input image.""",
            "mandatory": True,
        },
    ),
    (
        "fixel_directory_in",
        Directory,
        {
            "argstr": "",
            "position": 1,
            "help_string": """the input fixel directory. Used to define the fixels and their directions""",
            "mandatory": True,
        },
    ),
    (
        "fixel_directory_out",
        str,
        {
            "argstr": "",
            "position": 2,
            "help_string": """the fixel directory where the output will be written. This can be the same as the input directory if desired""",
            "mandatory": True,
        },
    ),
    (
        "fixel_data_out",
        str,
        {
            "argstr": "",
            "position": 3,
            "help_string": """the name of the fixel data image.""",
            "mandatory": True,
        },
    ),
    # Standard options
    (
        "info",
        bool,
        {
            "argstr": "-info",
            "help_string": """display information messages.""",
        },
    ),
    (
        "quiet",
        bool,
        {
            "argstr": "-quiet",
            "help_string": """do not display information messages or progress status; alternatively, this can be achieved by setting the MRTRIX_QUIET environment variable to a non-empty string.""",
        },
    ),
    (
        "debug",
        bool,
        {
            "argstr": "-debug",
            "help_string": """display debugging messages.""",
        },
    ),
    (
        "force",
        bool,
        {
            "argstr": "-force",
            "help_string": """force overwrite of output files (caution: using the same file as input and output might cause unexpected behaviour).""",
        },
    ),
    (
        "nthreads",
        int,
        {
            "argstr": "-nthreads",
            "help_string": """use this number of threads in multi-threaded applications (set to 0 to disable multi-threading).""",
        },
    ),
    (
        "config",
        specs.MultiInputObj[ty.Tuple[str, str]],
        {
            "argstr": "-config",
            "help_string": """temporarily set the value of an MRtrix config file entry.""",
        },
    ),
    (
        "help",
        bool,
        {
            "argstr": "-help",
            "help_string": """display this information page and exit.""",
        },
    ),
    (
        "version",
        bool,
        {
            "argstr": "-version",
            "help_string": """display version information and exit.""",
        },
    ),
]

voxel2fixel_input_spec = specs.SpecInfo(
    name="voxel2fixel_input", fields=input_fields, bases=(specs.ShellSpec,)
)


output_fields = []
voxel2fixel_output_spec = specs.SpecInfo(
    name="voxel2fixel_output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class voxel2fixel(ShellCommandTask):
    """This command is designed to enable CFE-based statistical analysis to be performed on voxel-wise measures.

        Fixel data are stored utilising the fixel directory format described in the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/fixel_based_analysis/fixel_directory_format.html


        References
        ----------

            Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137


        MRtrix
        ------

            Version:3.0.4-658-gded202e6-dirty, built Aug 28 2023

            Author: David Raffelt (david.raffelt@florey.edu.au)

            Copyright: Copyright (c) 2008-2023 the MRtrix3 contributors.

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

    Covered Software is provided under this License on an "as is"
    basis, without warranty of any kind, either expressed, implied, or
    statutory, including, without limitation, warranties that the
    Covered Software is free of defects, merchantable, fit for a
    particular purpose or non-infringing.
    See the Mozilla Public License v. 2.0 for more details.

    For more details, see http://www.mrtrix.org/.
    """

    executable = "voxel2fixel"
    input_spec = voxel2fixel_input_spec
    output_spec = voxel2fixel_output_spec
