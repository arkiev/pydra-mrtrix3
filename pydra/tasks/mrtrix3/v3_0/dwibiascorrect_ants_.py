import typing
from pathlib import Path  # noqa: F401
from fileformats.generic import FsObject, File, Directory  # noqa: F401
from fileformats.medimage_mrtrix3 import Tracks, ImageIn, ImageOut  # noqa: F401
from pydra.engine.task import ShellCommandTask
from pydra.engine import specs

input_fields = [
    (
        "input",
        FsObject,
        {
            "help_string": "The input image series to be corrected",
            "mandatory": True,
            "position": 0,
            "argstr": "",
        },
    ),
    (
        "output",
        Path,
        {
            "help_string": "The output corrected image series",
            "position": 1,
            "argstr": "",
            "output_file_template": "output_{input}",
        },
    ),
    (
        "ants_b",
        typing.Any,
        {
            "help_string": "N4BiasFieldCorrection option -b. [initial mesh resolution in mm, spline order] This value is optimised for human adult data and needs to be adjusted for rodent data.",
            "argstr": "-ants.b",
        },
    ),
    (
        "ants_c",
        typing.Any,
        {
            "help_string": "N4BiasFieldCorrection option -c. [numberOfIterations,convergenceThreshold]",
            "argstr": "-ants.c",
        },
    ),
    (
        "ants_s",
        typing.Any,
        {
            "help_string": "N4BiasFieldCorrection option -s. shrink-factor applied to spatial dimensions",
            "argstr": "-ants.s",
        },
    ),
    (
        "grad",
        typing.Any,
        {
            "help_string": "Provide the diffusion gradient table in MRtrix format",
            "argstr": "-grad",
        },
    ),
    (
        "fslgrad",
        typing.Any,
        {
            "help_string": "Provide the diffusion gradient table in FSL bvecs/bvals format",
            "argstr": "-fslgrad",
        },
    ),
    (
        "mask",
        typing.Any,
        {
            "help_string": "Manually provide a mask image for bias field estimation",
            "argstr": "-mask",
        },
    ),
    (
        "bias",
        typing.Any,
        {"help_string": "Output the estimated bias field", "argstr": "-bias"},
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
]
dwibiascorrect_ants_input_spec = specs.SpecInfo(
    name="dwibiascorrect_ants_input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [
    (
        "output",
        FsObject,
        {"help_string": "The output corrected image series", "mandatory": True},
    )
]
dwibiascorrect_ants_output_spec = specs.SpecInfo(
    name="dwibiascorrect_ants_output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class dwibiascorrect_ants(ShellCommandTask):
    """
            References
        ----------

        * Tustison, N.; Avants, B.; Cook, P.; Zheng, Y.; Egan, A.; Yushkevich, P. & Gee, J. N4ITK: Improved N3 Bias Correction. IEEE Transactions on Medical Imaging, 2010, 29, 1310-1320

        Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137

        --------------



        **Author:** Robert E. Smith (robert.smith@florey.edu.au)

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

    input_spec = dwibiascorrect_ants_input_spec
    output_spec = dwibiascorrect_ants_output_spec
    executable = ("dwibiascorrect", "ants")
