# Auto-generated test for mrcat

from fileformats.generic import File  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import mrcat


def test_mrcat(tmp_path):
    task = mrcat(
        image1=Nifti1.sample(),
        image2=[Nifti1.sample()],
        output=ImageFormat.sample(),
        axis=1,
        datatype="float16",
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
