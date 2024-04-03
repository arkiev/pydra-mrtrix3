# Auto-generated test for maskdump

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import maskdump


def test_maskdump(tmp_path, cli_parse_only):
    task = maskdump(
        in_file=Nifti1.sample(),
        out_file=File.sample(),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
