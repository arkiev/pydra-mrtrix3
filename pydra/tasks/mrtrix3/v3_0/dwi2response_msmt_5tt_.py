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
            "help_string": "The input DWI",
            "mandatory": True,
            "position": 0,
            "argstr": "",
        },
    ),
    (
        "in_5tt",
        typing.Any,
        {
            "help_string": "Input co-registered 5TT image",
            "mandatory": True,
            "position": 1,
            "argstr": "",
        },
    ),
    (
        "out_wm",
        typing.Any,
        {
            "help_string": "Output WM response text file",
            "mandatory": True,
            "position": 2,
            "argstr": "",
        },
    ),
    (
        "out_gm",
        typing.Any,
        {
            "help_string": "Output GM response text file",
            "mandatory": True,
            "position": 3,
            "argstr": "",
        },
    ),
    (
        "out_csf",
        typing.Any,
        {
            "help_string": "Output CSF response text file",
            "mandatory": True,
            "position": 4,
            "argstr": "",
        },
    ),
    (
        "dirs",
        typing.Any,
        {
            "help_string": "Manually provide the fibre direction in each voxel (a tensor fit will be used otherwise)",
            "argstr": "-dirs",
        },
    ),
    (
        "fa",
        float,
        {
            "help_string": "Upper fractional anisotropy threshold for GM and CSF voxel selection (default: 0.2)",
            "argstr": "-fa",
        },
    ),
    (
        "pvf",
        float,
        {
            "help_string": "Partial volume fraction threshold for tissue voxel selection (default: 0.95)",
            "argstr": "-pvf",
        },
    ),
    (
        "wm_algo",
        typing.Any,
        {
            "help_string": "dwi2response algorithm to use for WM single-fibre voxel selection (options: fa, tax, tournier; default: tournier)",
            "allowed_values": ["fa", "tax", "tournier"],
            "argstr": "-wm_algo",
        },
    ),
    (
        "sfwm_fa_threshold",
        float,
        {
            "help_string": "Sets -wm_algo to fa and allows to specify a hard FA threshold for single-fibre WM voxels, which is passed to the -threshold option of the fa algorithm (warning: overrides -wm_algo option)",
            "argstr": "-sfwm_fa_threshold",
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
            "help_string": "Provide an initial mask for response voxel selection",
            "argstr": "-mask",
        },
    ),
    (
        "voxels",
        typing.Any,
        {
            "help_string": "Output an image showing the final voxel selection(s)",
            "argstr": "-voxels",
        },
    ),
    (
        "shells",
        typing.Any,
        {
            "help_string": "The b-value(s) to use in response function estimation (comma-separated list in case of multiple b-values, b=0 must be included explicitly)",
            "argstr": "-shells",
        },
    ),
    (
        "lmax",
        typing.Any,
        {
            "help_string": "The maximum harmonic degree(s) for response function estimation (comma-separated list in case of multiple b-values)",
            "argstr": "-lmax",
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
]
dwi2response_msmt_5tt_input_spec = specs.SpecInfo(
    name="dwi2response_msmt_5tt_input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = []
dwi2response_msmt_5tt_output_spec = specs.SpecInfo(
    name="dwi2response_msmt_5tt_output",
    fields=output_fields,
    bases=(specs.ShellOutSpec,),
)


class dwi2response_msmt_5tt(ShellCommandTask):
    """
            References
        ----------

        * Jeurissen, B.; Tournier, J.-D.; Dhollander, T.; Connelly, A. & Sijbers, J. Multi-tissue constrained spherical deconvolution for improved analysis of multi-shell diffusion MRI data. NeuroImage, 2014, 103, 411-426

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

    input_spec = dwi2response_msmt_5tt_input_spec
    output_spec = dwi2response_msmt_5tt_output_spec
    executable = ("dwi2response", "msmt_5tt")
