# Auto-generated test for dwinormalise_group

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import dwinormalise_group


def test_dwinormalise_group(tmp_path, cli_parse_only):
    task = dwinormalise_group(
        input_dir=File.sample(),
        mask_dir=File.sample(),
        output_dir=Directory.sample(),
        fa_template=ImageFormat.sample(),
        wm_mask=ImageFormat.sample(),
        nocleanup=True,
        scratch=False,
        cont=File.sample(),
        debug=True,
        force=True,
        fa_threshold=1.0,
    )
    result = task(plugin="serial")
    assert not result.errored
