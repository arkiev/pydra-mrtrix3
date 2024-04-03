# Auto-generated test for fixelcrop

from fileformats.generic import File  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import fixelcrop


def test_fixelcrop(tmp_path):
    task = fixelcrop(
        input_fixel_directory=File.sample(),
        input_fixel_mask=Nifti1.sample(),
        output_fixel_directory=Directory.sample(),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
