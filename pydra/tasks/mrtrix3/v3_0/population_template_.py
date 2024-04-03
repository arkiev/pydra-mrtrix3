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
            "help_string": "Directory containing all input images of a given contrast",
            "mandatory": True,
            "position": 0,
            "argstr": "",
        },
    ),
    (
        "template",
        typing.Any,
        {
            "help_string": "Output template image",
            "mandatory": True,
            "position": 1,
            "argstr": "",
        },
    ),
    (
        "type",
        typing.Any,
        {
            "help_string": 'Specify the types of registration stages to perform. Options are "rigid" (perform rigid registration only which might be useful for intra-subject registration in longitudinal analysis), "affine" (perform affine registration) and "nonlinear" as well as cominations of registration types: "rigid_affine", "rigid_nonlinear", "affine_nonlinear", "rigid_affine_nonlinear". Default: rigid_affine_nonlinear',
            "argstr": "-type",
        },
    ),
    (
        "voxel_size",
        typing.Any,
        {
            "help_string": "Define the template voxel size in mm. Use either a single value for isotropic voxels or 3 comma separated values.",
            "argstr": "-voxel_size",
        },
    ),
    (
        "initial_alignment",
        typing.Any,
        {
            "help_string": 'Method of alignment to form the initial template. Options are "mass" (default), "robust_mass" (requires masks), "geometric" and "none".',
            "argstr": "-initial_alignment",
        },
    ),
    (
        "mask_dir",
        typing.Any,
        {
            "help_string": "Optionally input a set of masks inside a single directory, one per input image (with the same file name prefix). Using masks will speed up registration significantly. Note that masks are used for registration, not for aggregation. To exclude areas from aggregation, NaN-mask your input images.",
            "argstr": "-mask_dir",
        },
    ),
    (
        "warp_dir",
        typing.Any,
        {
            "help_string": "Output a directory containing warps from each input to the template. If the folder does not exist it will be created",
            "argstr": "-warp_dir",
        },
    ),
    (
        "transformed_dir",
        typing.Any,
        {
            "help_string": "Output a directory containing the input images transformed to the template. If the folder does not exist it will be created. For multi-contrast registration, provide comma separated list of directories.",
            "argstr": "-transformed_dir",
        },
    ),
    (
        "linear_transformations_dir",
        typing.Any,
        {
            "help_string": "Output a directory containing the linear transformations used to generate the template. If the folder does not exist it will be created",
            "argstr": "-linear_transformations_dir",
        },
    ),
    (
        "template_mask",
        typing.Any,
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
        typing.Any,
        {
            "help_string": "Register each input image to a template that does not contain that image. Valid choices: 0, 1, auto. (Default: auto (true if n_subjects larger than 2 and smaller than 15)) ",
            "argstr": "-leave_one_out",
        },
    ),
    (
        "aggregate",
        typing.Any,
        {
            "help_string": "Measure used to aggregate information from transformed images to the template image. Valid choices: mean, median. Default: mean",
            "argstr": "-aggregate",
        },
    ),
    (
        "aggregation_weights",
        typing.Any,
        {
            "help_string": "Comma separated file containing weights used for weighted image aggregation. Each row must contain the identifiers of the input image and its weight. Note that this weighs intensity values not transformations (shape).",
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
        typing.Any,
        {
            "help_string": "Specify the multi-resolution pyramid used to build the non-linear template, in the form of a list of scale factors (default: 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0). This implicitly defines the number of template levels",
            "argstr": "-nl_scale",
        },
    ),
    (
        "nl_lmax",
        typing.Any,
        {
            "help_string": "Specify the lmax used for non-linear registration for each scale factor, in the form of a list of integers (default: 2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4). The list must be the same length as the nl_scale factor list",
            "argstr": "-nl_lmax",
        },
    ),
    (
        "nl_niter",
        typing.Any,
        {
            "help_string": "Specify the number of registration iterations used within each level before updating the template, in the form of a list of integers (default: 5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5). The list must be the same length as the nl_scale factor list",
            "argstr": "-nl_niter",
        },
    ),
    (
        "nl_update_smooth",
        typing.Any,
        {
            "help_string": "Regularise the gradient update field with Gaussian smoothing (standard deviation in voxel units, Default 2.0 x voxel_size)",
            "argstr": "-nl_update_smooth",
        },
    ),
    (
        "nl_disp_smooth",
        typing.Any,
        {
            "help_string": "Regularise the displacement field with Gaussian smoothing (standard deviation in voxel units, Default 1.0 x voxel_size)",
            "argstr": "-nl_disp_smooth",
        },
    ),
    (
        "nl_grad_step",
        typing.Any,
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
        typing.Any,
        {
            "help_string": "Specify estimator for intensity difference metric. Valid choices are: l1 (least absolute: |x|), l2 (ordinary least squares), lp (least powers: |x|^1.2), Default: None (no robust estimator used)",
            "argstr": "-linear_estimator",
        },
    ),
    (
        "rigid_scale",
        typing.Any,
        {
            "help_string": "Specify the multi-resolution pyramid used to build the rigid template, in the form of a list of scale factors (default: 0.3,0.4,0.6,0.8,1.0,1.0). This and affine_scale implicitly  define the number of template levels",
            "argstr": "-rigid_scale",
        },
    ),
    (
        "rigid_lmax",
        typing.Any,
        {
            "help_string": "Specify the lmax used for rigid registration for each scale factor, in the form of a list of integers (default: 2,2,2,4,4,4). The list must be the same length as the linear_scale factor list",
            "argstr": "-rigid_lmax",
        },
    ),
    (
        "rigid_niter",
        typing.Any,
        {
            "help_string": "Specify the number of registration iterations used within each level before updating the template, in the form of a list of integers (default:50 for each scale). This must be a single number or a list of same length as the linear_scale factor list",
            "argstr": "-rigid_niter",
        },
    ),
    (
        "affine_scale",
        typing.Any,
        {
            "help_string": "Specify the multi-resolution pyramid used to build the affine template, in the form of a list of scale factors (default: 0.3,0.4,0.6,0.8,1.0,1.0). This and rigid_scale implicitly define the number of template levels",
            "argstr": "-affine_scale",
        },
    ),
    (
        "affine_lmax",
        typing.Any,
        {
            "help_string": "Specify the lmax used for affine registration for each scale factor, in the form of a list of integers (default: 2,2,2,4,4,4). The list must be the same length as the linear_scale factor list",
            "argstr": "-affine_lmax",
        },
    ),
    (
        "affine_niter",
        typing.Any,
        {
            "help_string": "Specify the number of registration iterations used within each level before updating the template, in the form of a list of integers (default:500 for each scale). This must be a single number or a list of same length as the linear_scale factor list",
            "argstr": "-affine_niter",
        },
    ),
    (
        "mc_weight_initial_alignment",
        typing.Any,
        {
            "help_string": "Weight contribution of each contrast to the initial alignment. Comma separated, default: 1.0",
            "argstr": "-mc_weight_initial_alignment",
        },
    ),
    (
        "mc_weight_rigid",
        typing.Any,
        {
            "help_string": "Weight contribution of each contrast to the objective of rigid registration. Comma separated, default: 1.0",
            "argstr": "-mc_weight_rigid",
        },
    ),
    (
        "mc_weight_affine",
        typing.Any,
        {
            "help_string": "Weight contribution of each contrast to the objective of affine registration. Comma separated, default: 1.0",
            "argstr": "-mc_weight_affine",
        },
    ),
    (
        "mc_weight_nl",
        typing.Any,
        {
            "help_string": "Weight contribution of each contrast to the objective of nonlinear registration. Comma separated, default: 1.0",
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
population_template_input_spec = specs.SpecInfo(
    name="population_template_input", fields=input_fields, bases=(specs.ShellSpec,)
)

output_fields = []
population_template_output_spec = specs.SpecInfo(
    name="population_template_output", fields=output_fields, bases=(specs.ShellOutSpec,)
)


class population_template(ShellCommandTask):
    """
            References
        ----------

        Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137

        --------------



        **Author:** David Raffelt (david.raffelt@florey.edu.au) & Max Pietsch (maximilian.pietsch@kcl.ac.uk) & Thijs Dhollander (thijs.dhollander@gmail.com)

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

    input_spec = population_template_input_spec
    output_spec = population_template_output_spec
    executable = "population_template"
