import typing as ty
from pathlib import Path  # noqa: F401
from fileformats.generic import File, Directory  # noqa: F401
from fileformats.medimage_mrtrix3 import ImageIn, ImageOut, Tracks  # noqa: F401
from pydra.engine import specs, ShellCommandTask


input_fields = [
    # Arguments
    (
        "fod",
        ImageIn,
        {
            "argstr": "",
            "position": 0,
            "help_string": """the input fod image.""",
            "mandatory": True,
        },
    ),
    (
        "fixel_directory",
        Path,
        {
            "argstr": "",
            "position": 1,
            "output_file_template": "fixel_directory",
            "help_string": """the output fixel directory""",
        },
    ),
    # Metric values for fixel-based sparse output images Option Group
    (
        "afd",
        ty.Union[Path, bool],
        False,
        {
            "argstr": "-afd",
            "output_file_template": "afd.mif",
            "help_string": """output the total Apparent Fibre Density per fixel (integral of FOD lobe)""",
        },
    ),
    (
        "peak_amp",
        ty.Union[Path, bool],
        False,
        {
            "argstr": "-peak_amp",
            "output_file_template": "peak_amp.mif",
            "help_string": """output the amplitude of the FOD at the maximal peak per fixel""",
        },
    ),
    (
        "disp",
        ty.Union[Path, bool],
        False,
        {
            "argstr": "-disp",
            "output_file_template": "disp.mif",
            "help_string": """output a measure of dispersion per fixel as the ratio between FOD lobe integral and maximal peak amplitude""",
        },
    ),
    # FOD FMLS segmenter options Option Group
    (
        "fmls_integral",
        float,
        {
            "argstr": "-fmls_integral",
            "help_string": """threshold absolute numerical integral of positive FOD lobes. Any lobe for which the integral is smaller than this threshold will be discarded. Default: 0.""",
        },
    ),
    (
        "fmls_peak_value",
        float,
        {
            "argstr": "-fmls_peak_value",
            "help_string": """threshold peak amplitude of positive FOD lobes. Any lobe for which the maximal peak amplitude is smaller than this threshold will be discarded. Default: 0.1.""",
        },
    ),
    (
        "fmls_no_thresholds",
        bool,
        {
            "argstr": "-fmls_no_thresholds",
            "help_string": """disable all FOD lobe thresholding; every lobe where the FOD is positive will be retained.""",
        },
    ),
    (
        "fmls_lobe_merge_ratio",
        float,
        {
            "argstr": "-fmls_lobe_merge_ratio",
            "help_string": """Specify the ratio between a given FOD amplitude sample between two lobes, and the smallest peak amplitude of the adjacent lobes, above which those lobes will be merged. This is the amplitude of the FOD at the 'bridge' point between the two lobes, divided by the peak amplitude of the smaller of the two adjoining lobes. A value of 1.0 will never merge two lobes into one; a value of 0.0 will always merge lobes unless they are bisected by a zero-valued crossing. Default: 1.""",
        },
    ),
    # Other options for fod2fixel Option Group
    (
        "mask",
        ImageIn,
        {
            "argstr": "-mask",
            "help_string": """only perform computation within the specified binary brain mask image.""",
        },
    ),
    (
        "maxnum",
        int,
        {
            "argstr": "-maxnum",
            "help_string": """maximum number of fixels to output for any particular voxel (default: no limit)""",
        },
    ),
    (
        "nii",
        bool,
        {
            "argstr": "-nii",
            "help_string": """output the directions and index file in nii format (instead of the default mif)""",
        },
    ),
    (
        "dirpeak",
        bool,
        {
            "argstr": "-dirpeak",
            "help_string": """define the fixel direction as that of the lobe's maximal peak as opposed to its weighted mean direction (the default)""",
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

fod2fixel_input_spec = specs.SpecInfo(
    name="fod2fixel_input", fields=input_fields, bases=(specs.ShellSpec,)
)


output_fields = [
    (
        "fixel_directory",
        Directory,
        {
            "help_string": """the output fixel directory""",
        },
    ),
    (
        "afd",
        ImageOut,
        {
            "help_string": """output the total Apparent Fibre Density per fixel (integral of FOD lobe)""",
        },
    ),
    (
        "peak_amp",
        ImageOut,
        {
            "help_string": """output the amplitude of the FOD at the maximal peak per fixel""",
        },
    ),
    (
        "disp",
        ImageOut,
        {
            "help_string": """output a measure of dispersion per fixel as the ratio between FOD lobe integral and maximal peak amplitude""",
        },
    ),
]
fod2fixel_output_spec = specs.SpecInfo(
    name="fod2fixel_output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class fod2fixel(ShellCommandTask):
    """Fixel data are stored utilising the fixel directory format described in the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/fixel_based_analysis/fixel_directory_format.html


        References
        ----------

            * Reference for the FOD segmentation method:
    Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A. SIFT: Spherical-deconvolution informed filtering of tractograms. NeuroImage, 2013, 67, 298-312 (Appendix 2)

            * Reference for Apparent Fibre Density (AFD):
    Raffelt, D.; Tournier, J.-D.; Rose, S.; Ridgway, G.R.; Henderson, R.; Crozier, S.; Salvado, O.; Connelly, A. Apparent Fibre Density: a novel measure for the analysis of diffusion-weighted magnetic resonance images.Neuroimage, 2012, 15;59(4), 3976-94

            Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137


        MRtrix
        ------

            Version:3.0.4-658-gded202e6-dirty, built Aug 28 2023

            Author: Robert E. Smith (robert.smith@florey.edu.au)

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

    executable = "fod2fixel"
    input_spec = fod2fixel_input_spec
    output_spec = fod2fixel_output_spec
