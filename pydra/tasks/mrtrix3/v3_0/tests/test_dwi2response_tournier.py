# Auto-generated test for dwi2response_tournier

from fileformats.generic import File  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import dwi2response_tournier


def test_dwi2response_tournier(tmp_path):
    task = dwi2response_tournier(
        input=File.sample(),
        output=FsObject.sample(),
        number=1,
        iter_voxels=1,
        dilate=1,
        max_iters=1,
        grad=File.sample(),
        fslgrad=File.sample(),
        mask=File.sample(),
        voxels=File.sample(),
        shells=File.sample(),
        lmax=File.sample(),
        nocleanup=True,
        scratch=File.sample(),
        cont=File.sample(),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
