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
            "help_string": "The input T1-weighted image",
            "mandatory": True,
            "position": 0,
            "argstr": "",
        },
    ),
    (
        "output",
        Path,
        {
            "help_string": "The output 5TT image",
            "position": 1,
            "argstr": "",
            "output_file_template": "output_{input}",
        },
    ),
    (
        "t2",
        typing.Any,
        {
            "help_string": "Provide a T2-weighted image in addition to the default T1-weighted image; this will be used as a second input to FSL FAST",
            "argstr": "-t2",
        },
    ),
    (
        "mask",
        typing.Any,
        {
            "help_string": "Manually provide a brain mask, rather than deriving one in the script",
            "argstr": "-mask",
        },
    ),
    (
        "premasked",
        bool,
        {
            "help_string": "Indicate that brain masking has already been applied to the input image",
            "argstr": "-premasked",
        },
    ),
    (
        "nocrop",
        bool,
        {
            "help_string": "Do NOT crop the resulting 5TT image to reduce its size (keep the same dimensions as the input image)",
            "argstr": "-nocrop",
        },
    ),
    (
        "sgm_amyg_hipp",
        bool,
        {
            "help_string": "Represent the amygdalae and hippocampi as sub-cortical grey matter in the 5TT image",
            "argstr": "-sgm_amyg_hipp",
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
fivettgen_fsl_input_spec = specs.SpecInfo(
    name="fivettgen_fsl_input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [
    ("output", FsObject, {"help_string": "The output 5TT image", "mandatory": True})
]
fivettgen_fsl_output_spec = specs.SpecInfo(
    name="fivettgen_fsl_output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class fivettgen_fsl(ShellCommandTask):
    """
            References
        ----------

        * Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A. Anatomically-constrained tractography: Improved diffusion MRI streamlines tractography through effective use of anatomical information. NeuroImage, 2012, 62, 1924-1938

        * Smith, S. M. Fast robust automated brain extraction. Human Brain Mapping, 2002, 17, 143-155

        * Zhang, Y.; Brady, M. & Smith, S. Segmentation of brain MR images through a hidden Markov random field model and the expectation-maximization algorithm. IEEE Transactions on Medical Imaging, 2001, 20, 45-57

        * Patenaude, B.; Smith, S. M.; Kennedy, D. N. & Jenkinson, M. A Bayesian model of shape and appearance for subcortical brain segmentation. NeuroImage, 2011, 56, 907-922

        * Smith, S. M.; Jenkinson, M.; Woolrich, M. W.; Beckmann, C. F.; Behrens, T. E.; Johansen-Berg, H.; Bannister, P. R.; De Luca, M.; Drobnjak, I.; Flitney, D. E.; Niazy, R. K.; Saunders, J.; Vickers, J.; Zhang, Y.; De Stefano, N.; Brady, J. M. & Matthews, P. M. Advances in functional and structural MR image analysis and implementation as FSL. NeuroImage, 2004, 23, S208-S219

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

    input_spec = fivettgen_fsl_input_spec
    output_spec = fivettgen_fsl_output_spec
    executable = ("5ttgen", "fsl")
