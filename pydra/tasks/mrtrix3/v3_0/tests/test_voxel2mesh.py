# Auto-generated test for voxel2mesh

from fileformats.generic import File  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import voxel2mesh


def test_voxel2mesh(tmp_path):
    task = voxel2mesh(
        input=Nifti1.sample(),
        output=File.sample(),
        blocky=True,
        threshold=1.0,
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
