# Auto-generated test for warpinvert

from fileformats.generic import File  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import warpinvert


def test_warpinvert(tmp_path):
    task = warpinvert(
        in_=Nifti1.sample(),
        out=ImageFormat.sample(),
        template=Nifti1.sample(),
        displacement=True,
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
