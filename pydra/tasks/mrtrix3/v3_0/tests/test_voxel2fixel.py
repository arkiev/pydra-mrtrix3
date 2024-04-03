# Auto-generated test for voxel2fixel

from fileformats.generic import File  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import voxel2fixel


def test_voxel2fixel(tmp_path):
    task = voxel2fixel(
        image_in=Nifti1.sample(),
        fixel_directory_in=File.sample(),
        fixel_directory_out="a-string",
        fixel_data_out="a-string",
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
