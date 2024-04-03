# Auto-generated test for dwi2adc

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import dwi2adc


def test_dwi2adc(tmp_path, cli_parse_only):
    task = dwi2adc(
        in_file=Nifti1.sample(),
        out_file=ImageFormat.sample(),
        grad=File.sample(),
        fslgrad=tuple([File.sample(), File.sample()]),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
