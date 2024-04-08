# Auto-generated by mrtrix3/app.py:print_usage_pydra()

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
            "help_string": "Input directory containing all images of a given contrast",
            "mandatory": True,
            "position": 0,
            "argstr": "",
        },
    ),
    (
        "template",
        Path,
        {
            "help_string": "Output template image",
            "position": 1,
            "argstr": "",
            "output_file_template": "template.mif",
        },
    ),
    (
        "type",
        str,
        {
            "help_string": 'Specify the types of registration stages to perform. Options are: "rigid" (perform rigid registration only, which might be useful for intra-subject registration in longitudinal analysis), "affine" (perform affine registration), "nonlinear", as well as cominations of registration types: "rigid_affine", "rigid_nonlinear", "affine_nonlinear", "rigid_affine_nonlinear". Default: rigid_affine_nonlinear',
            "allowed_values": [
                "rigid",
                "affine",
                "nonlinear",
                "rigid_affine",
                "rigid_nonlinear",
                "affine_nonlinear",
                "rigid_affine_nonlinear",
            ],
            "argstr": "-type",
        },
    ),
    (
        "voxel_size",
        typing.List[float],
        {
            "help_string": "Define the template voxel size in mm. Use either a single value for isotropic voxels or 3 comma-separated values.",
            "argstr": "-voxel_size",
        },
    ),
    (
        "initial_alignment",
        str,
        {
            "help_string": 'Method of alignment to form the initial template. Options are: "mass" (default), "robust_mass" (requires masks), "geometric", "none".',
            "allowed_values": ["mass", "robust_mass", "geometric", "none"],
            "argstr": "-initial_alignment",
        },
    ),
    (
        "mask_dir",
        Directory,
        {
            "help_string": "Optionally input a set of masks inside a single directory, one per input image (with the same file name prefix). Using masks will speed up registration significantly. Note that masks are used for registration, not for aggregation. To exclude areas from aggregation, NaN-mask your input images.",
            "argstr": "-mask_dir",
        },
    ),
    (
        "warp_dir",
        Path,
        {
            "help_string": "Output a directory containing warps from each input to the template. If the folder does not exist it will be created",
            "argstr": "-warp_dir",
        },
    ),
    (
        "transformed_dir",
        Path,
        {
            "help_string": "Output a directory containing the input images transformed to the template. If the folder does not exist it will be created. For multi-contrast registration, this path will contain a sub-directory for the images per contrast.",
            "argstr": "-transformed_dir",
        },
    ),
    (
        "linear_transformations_dir",
        Path,
        {
            "help_string": "Output a directory containing the linear transformations used to generate the template. If the folder does not exist it will be created",
            "argstr": "-linear_transformations_dir",
        },
    ),
    (
        "template_mask",
        Path,
        {
            "help_string": "Output a template mask. Only works if -mask_dir has been input. The template mask is computed as the intersection of all subject masks in template space.",
            "argstr": "-template_mask",
        },
    ),
    (
        "noreorientation",
        bool,
        {
            "help_string": "Turn off FOD reorientation in mrregister. Reorientation is on by default if the number of volumes in the 4th dimension corresponds to the number of coefficients in an antipodally symmetric spherical harmonic series (i.e. 6, 15, 28, 45, 66 etc)",
            "argstr": "-noreorientation",
        },
    ),
    (
        "leave_one_out",
        str,
        {
            "help_string": "Register each input image to a template that does not contain that image. Valid choices: 0, 1, auto. (Default: auto (true if n_subjects larger than 2 and smaller than 15))",
            "allowed_values": ["0", "1", "auto"],
            "argstr": "-leave_one_out",
        },
    ),
    (
        "aggregate",
        str,
        {
            "help_string": "Measure used to aggregate information from transformed images to the template image. Valid choices: mean, median. Default: mean",
            "allowed_values": ["mean", "median"],
            "argstr": "-aggregate",
        },
    ),
    (
        "aggregation_weights",
        File,
        {
            "help_string": "Comma-separated file containing weights used for weighted image aggregation. Each row must contain the identifiers of the input image and its weight. Note that this weighs intensity values not transformations (shape).",
            "argstr": "-aggregation_weights",
        },
    ),
    (
        "nanmask",
        bool,
        {
            "help_string": "Optionally apply masks to (transformed) input images using NaN values to specify include areas for registration and aggregation. Only works if -mask_dir has been input.",
            "argstr": "-nanmask",
        },
    ),
    (
        "copy_input",
        bool,
        {
            "help_string": "Copy input images and masks into local scratch directory.",
            "argstr": "-copy_input",
        },
    ),
    (
        "delete_temporary_files",
        bool,
        {
            "help_string": "Delete temporary files from scratch directory during template creation.",
            "argstr": "-delete_temporary_files",
        },
    ),
    (
        "nl_scale",
        typing.List[float],
        {
            "help_string": "Specify the multi-resolution pyramid used to build the non-linear template, in the form of a list of scale factors (default: 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0). This implicitly defines the number of template levels",
            "argstr": "-nl_scale",
        },
    ),
    (
        "nl_lmax",
        typing.List[int],
        {
            "help_string": "Specify the lmax used for non-linear registration for each scale factor, in the form of a list of integers (default: 2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4). The list must be the same length as the nl_scale factor list",
            "argstr": "-nl_lmax",
        },
    ),
    (
        "nl_niter",
        typing.List[int],
        {
            "help_string": "Specify the number of registration iterations used within each level before updating the template, in the form of a list of integers (default: 5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5). The list must be the same length as the nl_scale factor list",
            "argstr": "-nl_niter",
        },
    ),
    (
        "nl_update_smooth",
        float,
        {
            "help_string": "Regularise the gradient update field with Gaussian smoothing (standard deviation in voxel units, Default 2.0 x voxel_size)",
            "argstr": "-nl_update_smooth",
        },
    ),
    (
        "nl_disp_smooth",
        float,
        {
            "help_string": "Regularise the displacement field with Gaussian smoothing (standard deviation in voxel units, Default 1.0 x voxel_size)",
            "argstr": "-nl_disp_smooth",
        },
    ),
    (
        "nl_grad_step",
        float,
        {
            "help_string": "The gradient step size for non-linear registration (Default: 0.5)",
            "argstr": "-nl_grad_step",
        },
    ),
    (
        "linear_no_pause",
        bool,
        {
            "help_string": "Do not pause the script if a linear registration seems implausible",
            "argstr": "-linear_no_pause",
        },
    ),
    (
        "linear_no_drift_correction",
        bool,
        {
            "help_string": "Deactivate correction of template appearance (scale and shear) over iterations",
            "argstr": "-linear_no_drift_correction",
        },
    ),
    (
        "linear_estimator",
        str,
        {
            "help_string": "Specify estimator for intensity difference metric. Valid choices are: l1 (least absolute: |x|), l2 (ordinary least squares), lp (least powers: |x|^1.2), none (no robust estimator). Default: none.",
            "allowed_values": ["l1", "l2", "lp", "none"],
            "argstr": "-linear_estimator",
        },
    ),
    (
        "rigid_scale",
        typing.List[float],
        {
            "help_string": "Specify the multi-resolution pyramid used to build the rigid template, in the form of a list of scale factors (default: 0.3,0.4,0.6,0.8,1.0,1.0). This and affine_scale implicitly define the number of template levels",
            "argstr": "-rigid_scale",
        },
    ),
    (
        "rigid_lmax",
        typing.List[int],
        {
            "help_string": "Specify the lmax used for rigid registration for each scale factor, in the form of a list of integers (default: 2,2,2,4,4,4). The list must be the same length as the linear_scale factor list",
            "argstr": "-rigid_lmax",
        },
    ),
    (
        "rigid_niter",
        typing.List[int],
        {
            "help_string": "Specify the number of registration iterations used within each level before updating the template, in the form of a list of integers (default: 50 for each scale). This must be a single number or a list of same length as the linear_scale factor list",
            "argstr": "-rigid_niter",
        },
    ),
    (
        "affine_scale",
        typing.List[float],
        {
            "help_string": "Specify the multi-resolution pyramid used to build the affine template, in the form of a list of scale factors (default: 0.3,0.4,0.6,0.8,1.0,1.0). This and rigid_scale implicitly define the number of template levels",
            "argstr": "-affine_scale",
        },
    ),
    (
        "affine_lmax",
        typing.List[int],
        {
            "help_string": "Specify the lmax used for affine registration for each scale factor, in the form of a list of integers (default: 2,2,2,4,4,4). The list must be the same length as the linear_scale factor list",
            "argstr": "-affine_lmax",
        },
    ),
    (
        "affine_niter",
        typing.List[int],
        {
            "help_string": "Specify the number of registration iterations used within each level before updating the template, in the form of a list of integers (default: 500 for each scale). This must be a single number or a list of same length as the linear_scale factor list",
            "argstr": "-affine_niter",
        },
    ),
    (
        "mc_weight_initial_alignment",
        typing.List[float],
        {
            "help_string": "Weight contribution of each contrast to the initial alignment. Comma separated, default: 1.0 for each contrast (ie. equal weighting).",
            "argstr": "-mc_weight_initial_alignment",
        },
    ),
    (
        "mc_weight_rigid",
        typing.List[float],
        {
            "help_string": "Weight contribution of each contrast to the objective of rigid registration. Comma separated, default: 1.0 for each contrast (ie. equal weighting)",
            "argstr": "-mc_weight_rigid",
        },
    ),
    (
        "mc_weight_affine",
        typing.List[float],
        {
            "help_string": "Weight contribution of each contrast to the objective of affine registration. Comma separated, default: 1.0 for each contrast (ie. equal weighting)",
            "argstr": "-mc_weight_affine",
        },
    ),
    (
        "mc_weight_nl",
        typing.List[float],
        {
            "help_string": "Weight contribution of each contrast to the objective of nonlinear registration. Comma separated, default: 1.0 for each contrast (ie. equal weighting)",
            "argstr": "-mc_weight_nl",
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
        Path,
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
    (
        "info",
        bool,
        {
            "help_string": "display information messages.",
            "argstr": "-info",
            "xor": ("info", "quiet", "debug"),
        },
    ),
    (
        "quiet",
        bool,
        {
            "help_string": "do not display information messages or progress status. Alternatively, this can be achieved by setting the MRTRIX_QUIET environment variable to a non-empty string.",
            "argstr": "-quiet",
            "xor": ("info", "quiet", "debug"),
        },
    ),
    (
        "debug",
        bool,
        {
            "help_string": "display debugging messages.",
            "argstr": "-debug",
            "xor": ("info", "quiet", "debug"),
        },
    ),
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
        specs.MultiInputObj[str],
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
PopulationTemplateInputSpec = specs.SpecInfo(
    name="PopulationTemplateInput", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = [
    ("template", ImageOut, {"help_string": "Output template image"}),
    (
        "warp_dir",
        Directory,
        {
            "help_string": "Output a directory containing warps from each input to the template. If the folder does not exist it will be created"
        },
    ),
    (
        "transformed_dir",
        Directory,
        {
            "help_string": "Output a directory containing the input images transformed to the template. If the folder does not exist it will be created. For multi-contrast registration, this path will contain a sub-directory for the images per contrast."
        },
    ),
    (
        "linear_transformations_dir",
        Directory,
        {
            "help_string": "Output a directory containing the linear transformations used to generate the template. If the folder does not exist it will be created"
        },
    ),
    (
        "template_mask",
        ImageOut,
        {
            "help_string": "Output a template mask. Only works if -mask_dir has been input. The template mask is computed as the intersection of all subject masks in template space."
        },
    ),
    (
        "scratch",
        Directory,
        {
            "help_string": "manually specify the path in which to generate the scratch directory."
        },
    ),
]
PopulationTemplateOutputSpec = specs.SpecInfo(
    name="PopulationTemplateOutput", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class PopulationTemplate(ShellCommandTask):
    """
            References
        ----------

        Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137

        --------------



        **Author:** David Raffelt (david.raffelt@florey.edu.au) & Max Pietsch (maximilian.pietsch@kcl.ac.uk) & Thijs Dhollander (thijs.dhollander@gmail.com)

        **Copyright:** Copyright (c) 2008-2024 the MRtrix3 contributors.

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

    input_spec = PopulationTemplateInputSpec
    output_spec = PopulationTemplateOutputSpec
    executable = "population_template"
