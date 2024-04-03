# Auto-generated test for dwi2response_tax

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import dwi2response_tax


def test_dwi2response_tax(tmp_path, cli_parse_only):
    task = dwi2response_tax(
        in_file=Nifti1.sample(),
        out_file=File.sample(),
        peak_ratio=1.0,
        max_iters=1,
        convergence=1.0,
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
