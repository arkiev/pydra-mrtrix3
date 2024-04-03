# Auto-generated test for fivettgen_hsvs

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import fivettgen_hsvs


def test_fivettgen_hsvs(tmp_path, cli_parse_only):
    task = fivettgen_hsvs(
        in_file=File.sample(),
        out_file=ImageFormat.sample(),
        nocrop=True,
        sgm_amyg_hipp=True,
        nocleanup=True,
        scratch=False,
        cont=File.sample(),
        debug=True,
        force=True,
        template=Nifti1.sample(),
        hippocampi="subfields",
        thalami="nuclei",
        white_stem=True,
    )
    result = task(plugin="serial")
    assert not result.errored
