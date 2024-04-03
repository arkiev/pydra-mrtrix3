# Auto-generated test for transformcalc

from fileformats.generic import File  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import transformcalc


def test_transformcalc(tmp_path):
    task = transformcalc(
        inputs=[File.sample()],
        operation="invert",
        output=File.sample(),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
