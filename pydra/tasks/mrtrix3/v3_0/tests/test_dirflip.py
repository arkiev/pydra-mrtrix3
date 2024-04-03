# Auto-generated test for dirflip

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import dirflip


def test_dirflip(tmp_path, cli_parse_only):
    task = dirflip(
        in_=File.sample(),
        out=File.sample(),
        permutations=1,
        cartesian=True,
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
