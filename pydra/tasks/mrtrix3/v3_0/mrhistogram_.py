# Auto-generated from MRtrix C++ command with '__print_usage_pydra__' secret option

import typing as ty
from pathlib import Path  # noqa: F401
from fileformats.generic import File, Directory  # noqa: F401
from fileformats.medimage_mrtrix3 import ImageIn, ImageOut, Tracks  # noqa: F401
from pydra.engine import specs, ShellCommandTask


input_fields = [
    # Arguments
    (
        "image_",
        ImageIn,
        {
            "argstr": "",
            "position": 0,
            "help_string": """the input image from which the histogram will be computed""",
            "mandatory": True,
        },
    ),
    (
        "hist",
        Path,
        {
            "argstr": "",
            "position": 1,
            "output_file_template": "hist.txt",
            "help_string": """the output histogram file""",
        },
    ),
    # Histogram generation options Option Group
    (
        "bins",
        int,
        {
            "argstr": "-bins",
            "help_string": """Manually set the number of bins to use to generate the histogram.""",
        },
    ),
    (
        "template",
        File,
        {
            "argstr": "-template",
            "help_string": """Use an existing histogram file as the template for histogram formation""",
        },
    ),
    (
        "mask",
        ImageIn,
        {
            "argstr": "-mask",
            "help_string": """Calculate the histogram only within a mask image.""",
        },
    ),
    (
        "ignorezero",
        bool,
        {
            "argstr": "-ignorezero",
            "help_string": """ignore zero-valued data during histogram construction.""",
        },
    ),
    # Additional options for mrhistogram Option Group
    (
        "allvolumes",
        bool,
        {
            "argstr": "-allvolumes",
            "help_string": """generate one histogram across all image volumes, rather than one per image volume""",
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

MrHistogramInputSpec = specs.SpecInfo(
    name="MrHistogramInput", fields=input_fields, bases=(specs.ShellSpec,)
)


output_fields = [
    (
        "hist",
        File,
        {
            "help_string": """the output histogram file""",
        },
    ),
]
MrHistogramOutputSpec = specs.SpecInfo(
    name="MrHistogramOutput", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class MrHistogram(ShellCommandTask):
    """
        References
        ----------

            Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137


        MRtrix
        ------

            Version:3.0.4-699-g04cb84da, built Apr  3 2024

            Author: Robert E. Smith (robert.smith@florey.edu.au)

            Copyright: Copyright (c) 2008-2024 the MRtrix3 contributors.

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

    executable = "mrhistogram"
    input_spec = MrHistogramInputSpec
    output_spec = MrHistogramOutputSpec
