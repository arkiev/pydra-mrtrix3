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
            "help_string": "The input DWI series to be corrected",
            "mandatory": True,
            "position": 0,
            "argstr": "",
        },
    ),
    (
        "output_dwi",
        str,
        {
            "help_string": "The output corrected DWI series",
            "mandatory": True,
            "position": 1,
            "argstr": "",
        },
    ),
    (
        "output_mask",
        str,
        {
            "help_string": "The output DWI mask",
            "mandatory": True,
            "position": 2,
            "argstr": "",
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
        "dice",
        float,
        {
            "help_string": "Set the Dice coefficient threshold for similarity of masks between sequential iterations that will result in termination due to convergence; default = 0.999",
            "argstr": "-dice",
        },
    ),
    (
        "init_mask",
        typing.Any,
        {
            "help_string": "Provide an initial mask for the first iteration of the algorithm (if not provided, the default dwi2mask algorithm will be used)",
            "argstr": "-init_mask",
        },
    ),
    (
        "max_iters",
        int,
        {
            "help_string": "The maximum number of iterations (see Description); default is 2; set to 0 to proceed until convergence",
            "argstr": "-max_iters",
        },
    ),
    (
        "mask_algo",
        typing.Any,
        {
            "help_string": "The algorithm to use for mask estimation, potentially based on the ODF sum image (see Description); default: threshold",
            "allowed_values": [
                "dwi2mask",
                "fslbet",
                "hdbet",
                "mrthreshold",
                "synthstrip",
                "threshold",
            ],
            "argstr": "-mask_algo",
        },
    ),
    (
        "lmax",
        typing.Any,
        {
            "help_string": 'The maximum spherical harmonic degree for the estimated FODs (see Description); defaults are "4,0,0" for multi-shell and "4,0" for single-shell data)',
            "argstr": "-lmax",
        },
    ),
    (
        "output_bias",
        str,
        {
            "help_string": "Export the final estimated bias field to an image",
            "argstr": "-output_bias",
        },
    ),
    (
        "output_scale",
        typing.Any,
        {
            "help_string": "Write the scaling factor applied to the DWI series to a text file",
            "argstr": "-output_scale",
        },
    ),
    (
        "output_tissuesum",
        str,
        {
            "help_string": "Export the tissue sum image that was used to generate the final mask",
            "argstr": "-output_tissuesum",
        },
    ),
    (
        "reference",
        float,
        {
            "help_string": "Set the target CSF b=0 intensity in the output DWI series (default: 1000.0)",
            "argstr": "-reference",
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
dwibiasnormmask_input_spec = specs.SpecInfo(
    name="dwibiasnormmask_input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [
    (
        "output_dwi",
        str,
        {
            "help_string": "The output corrected DWI series",
            "mandatory": True,
            "position": 1,
            "argstr": "",
        },
    ),
    (
        "output_mask",
        str,
        {
            "help_string": "The output DWI mask",
            "mandatory": True,
            "position": 2,
            "argstr": "",
        },
    ),
    (
        "output_bias",
        str,
        {
            "help_string": "Export the final estimated bias field to an image",
            "argstr": "-output_bias",
        },
    ),
    (
        "output_tissuesum",
        str,
        {
            "help_string": "Export the tissue sum image that was used to generate the final mask",
            "argstr": "-output_tissuesum",
        },
    ),

]
dwibiasnormmask_output_spec = specs.SpecInfo(
    name="dwibiasnormmask_output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class dwibiasnormmask(ShellCommandTask):
    """
            References
        ----------

        * Jeurissen, B; Tournier, J-D; Dhollander, T; Connelly, A & Sijbers, J. Multi-tissue constrained spherical deconvolution for improved analysis of multi-shell diffusion MRI data. NeuroImage, 2014, 103, 411-426

        * Raffelt, D.; Dhollander, T.; Tournier, J.-D.; Tabbara, R.; Smith, R. E.; Pierre, E. & Connelly, A. Bias Field Correction and Intensity Normalisation for Quantitative Analysis of Apparent Fibre Density. In Proc. ISMRM, 2017, 26, 3541

        * Dhollander, T.; Raffelt, D. & Connelly, A. Unsupervised 3-tissue response function estimation from single-shell or multi-shell diffusion MR data without a co-registered T1 image. ISMRM Workshop on Breaking the Barriers of Diffusion MRI, 2016, 5

        * Dhollander, T.; Tabbara, R.; Rosnarho-Tornstrand, J.; Tournier, J.-D.; Raffelt, D. & Connelly, A. Multi-tissue log-domain intensity and inhomogeneity normalisation for quantitative apparent fibre density. In Proc. ISMRM, 2021, 29, 2472

        Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137

        --------------



        **Author:** Robert E. Smith (robert.smith@florey.edu.au) and Arshiya Sangchooli (asangchooli@student.unimelb.edu.au)

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

    input_spec = dwibiasnormmask_input_spec
    output_spec = dwibiasnormmask_output_spec
    executable = "dwibiasnormmask"
