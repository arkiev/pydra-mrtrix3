# Auto-generated test for fivettgen_fsl

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import fivettgen_fsl


def test_fivettgen_fsl(tmp_path, cli_parse_only):
    task = fivettgen_fsl(
        in_file=Nifti1.sample(),
        out_file=ImageFormat.sample(),
        t2=Nifti1.sample(),
        mask=Nifti1.sample(),
        premasked=True,
        nocrop=True,
        sgm_amyg_hipp=True,
        nocleanup=True,
        scratch=False,
        cont=File.sample(),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
