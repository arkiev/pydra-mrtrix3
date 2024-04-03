# Auto-generated test for dwi2response_msmt_5tt

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import dwi2response_msmt_5tt


def test_dwi2response_msmt_5tt(tmp_path, cli_parse_only):
    task = dwi2response_msmt_5tt(
        in_file=Nifti1.sample(),
        in_5tt=Nifti1.sample(),
        out_wm=File.sample(),
        out_gm=File.sample(),
        out_csf=File.sample(),
        dirs=Nifti1.sample(),
        fa=1.0,
        pvf=1.0,
        wm_algo="fa",
        sfwm_fa_threshold=1.0,
        grad=File.sample(),
        fslgrad=File.sample(),
        mask=Nifti1.sample(),
        voxels=False,
        shells=list([1.0]),
        lmax=list([1]),
        nocleanup=True,
        scratch=False,
        cont=File.sample(),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
