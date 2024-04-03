# Auto-generated test for fixel2peaks

from fileformats.generic import File  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import fixel2peaks


def test_fixel2peaks(tmp_path):
    task = fixel2peaks(
        in_=File.sample(),
        out=ImageFormat.sample(),
        number=1,
        nan=True,
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
