# Auto-generated test for shview

from fileformats.generic import File  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import shview


def test_shview(tmp_path):
    task = shview(
        coefs=File.sample(),
        response=True,
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
