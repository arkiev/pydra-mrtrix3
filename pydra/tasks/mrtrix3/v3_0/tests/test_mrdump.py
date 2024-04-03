# Auto-generated test for mrdump

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import mrdump


def test_mrdump(tmp_path, cli_parse_only):
    task = mrdump(
        in_file=Nifti1.sample(),
        out_file=File.sample(),
        mask=Nifti1.sample(),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
