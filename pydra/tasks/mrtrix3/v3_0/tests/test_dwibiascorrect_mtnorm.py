# Auto-generated test for dwibiascorrect_mtnorm

from fileformats.generic import File  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import dwibiascorrect_mtnorm


def test_dwibiascorrect_mtnorm(tmp_path):
    task = dwibiascorrect_mtnorm(
        input=File.sample(),
        output=FsObject.sample(),
        lmax=File.sample(),
        grad=File.sample(),
        fslgrad=File.sample(),
        mask=File.sample(),
        bias=File.sample(),
        nocleanup=True,
        scratch=File.sample(),
        cont=File.sample(),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
