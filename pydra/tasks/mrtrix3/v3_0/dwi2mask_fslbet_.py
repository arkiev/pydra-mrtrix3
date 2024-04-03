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
            "help_string": "The input DWI series",
            "mandatory": True,
            "position": 0,
            "argstr": "",
        },
    ),
    (
        "output",
        Path,
        {
            "help_string": "The output mask image",
            "position": 1,
            "argstr": "",
            "output_file_template": "output_{input}",
        },
    ),
    (
        "bet_f",
        float,
        {
            "help_string": "Fractional intensity threshold (0->1); smaller values give larger brain outline estimates",
            "argstr": "-bet_f",
        },
    ),
    (
        "bet_g",
        float,
        {
            "help_string": "Vertical gradient in fractional intensity threshold (-1->1); positive values give larger brain outline at bottom, smaller at top",
            "argstr": "-bet_g",
        },
    ),
    (
        "bet_c",
        typing.Any,
        {
            "help_string": "Centre-of-gravity (voxels not mm) of initial mesh surface",
            "argstr": "-bet_c",
        },
    ),
    (
        "bet_r",
        float,
        {
            "help_string": "Head radius (mm not voxels); initial surface sphere is set to half of this",
            "argstr": "-bet_r",
        },
    ),
    (
        "rescale",
        bool,
        {
            "help_string": "Rescale voxel size provided to BET to 1mm isotropic; can improve results for rodent data",
            "argstr": "-rescale",
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
dwi2mask_fslbet_input_spec = specs.SpecInfo(
    name="dwi2mask_fslbet_input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [
    ("output", FsObject, {"help_string": "The output mask image", "mandatory": True})
]
dwi2mask_fslbet_output_spec = specs.SpecInfo(
    name="dwi2mask_fslbet_output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class dwi2mask_fslbet(ShellCommandTask):
    """
            References
        ----------

        * Smith, S. M. Fast robust automated brain extraction. Human Brain Mapping, 2002, 17, 143-155

        Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137

        --------------



        **Author:** Warda Syeda (wtsyeda@unimelb.edu.au) and Robert E. Smith (robert.smith@florey.edu.au)

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

    input_spec = dwi2mask_fslbet_input_spec
    output_spec = dwi2mask_fslbet_output_spec
    executable = ("dwi2mask", "fslbet")
