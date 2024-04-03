import typing
from pathlib import Path  # noqa: F401
from fileformats.generic import FsObject, File, Directory  # noqa: F401
from fileformats.medimage_mrtrix3 import Tracks, ImageIn, ImageOut  # noqa: F401
from pydra.engine.task import ShellCommandTask
from pydra.engine import specs

input_fields = [
    (
        "input_dir",
        typing.Any,
        {
            "help_string": "The input directory containing all DWI images",
            "mandatory": True,
            "position": 0,
            "argstr": "",
        },
    ),
    (
        "mask_dir",
        typing.Any,
        {
            "help_string": "Input directory containing brain masks, corresponding to one per input image (with the same file name prefix)",
            "mandatory": True,
            "position": 1,
            "argstr": "",
        },
    ),
    (
        "output_dir",
        typing.Any,
        {
            "help_string": "The output directory containing all of the intensity normalised DWI images",
            "mandatory": True,
            "position": 2,
            "argstr": "",
        },
    ),
    (
        "fa_template",
        typing.Any,
        {
            "help_string": "The output population specific FA template, which is threshold to estimate a white matter mask",
            "mandatory": True,
            "position": 3,
            "argstr": "",
        },
    ),
    (
        "wm_mask",
        typing.Any,
        {
            "help_string": "The output white matter mask (in template space), used to estimate the median b=0 white matter value for normalisation",
            "mandatory": True,
            "position": 4,
            "argstr": "",
        },
    ),
    (
        "nocleanup",
        bool,
        {
            "help_string": "do not delete intermediate files during script execution, and do not delete scratch directory at script completion.",
            "argstr": "-nocleanup",
        },
    ),
    (
        "scratch",
        typing.Any,
        {
            "help_string": "manually specify the path in which to generate the scratch directory.",
            "argstr": "-scratch",
        },
    ),
    (
        "cont",
        typing.Any,
        {
            "help_string": "continue the script from a previous execution; must provide the scratch directory path, and the name of the last successfully-generated file.",
            "argstr": "-cont",
        },
    ),
    ("info", bool, {"help_string": "display information messages.", "argstr": "-info"}),
    (
        "quiet",
        bool,
        {
            "help_string": "do not display information messages or progress status. Alternatively, this can be achieved by setting the MRTRIX_QUIET environment variable to a non-empty string.",
            "argstr": "-quiet",
        },
    ),
    ("debug", bool, {"help_string": "display debugging messages.", "argstr": "-debug"}),
    (
        "force",
        bool,
        {"help_string": "force overwrite of output files.", "argstr": "-force"},
    ),
    (
        "nthreads",
        int,
        {
            "help_string": "use this number of threads in multi-threaded applications (set to 0 to disable multi-threading).",
            "argstr": "-nthreads",
        },
    ),
    (
        "config",
        specs.MultiInputObj[typing.Any],
        {
            "help_string": "temporarily set the value of an MRtrix config file entry.",
            "argstr": "-config",
        },
    ),
    (
        "help",
        bool,
        {"help_string": "display this information page and exit.", "argstr": "-help"},
    ),
    (
        "version",
        bool,
        {"help_string": "display version information and exit.", "argstr": "-version"},
    ),
    (
        "fa_threshold",
        typing.Any,
        {
            "help_string": "The threshold applied to the Fractional Anisotropy group template used to derive an approximate white matter mask (default: 0.4)",
            "argstr": "-fa_threshold",
        },
    ),
]
dwinormalise_group_input_spec = specs.SpecInfo(
    name="dwinormalise_group_input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = []
dwinormalise_group_output_spec = specs.SpecInfo(
    name="dwinormalise_group_output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class dwinormalise_group(ShellCommandTask):
    """
            References
        ----------

        Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137

        --------------



        **Author:** David Raffelt (david.raffelt@florey.edu.au)

        **Copyright:** Copyright (c) 2008-2023 the MRtrix3 contributors.

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

    input_spec = dwinormalise_group_input_spec
    output_spec = dwinormalise_group_output_spec
    executable = ("dwinormalise", "group")
