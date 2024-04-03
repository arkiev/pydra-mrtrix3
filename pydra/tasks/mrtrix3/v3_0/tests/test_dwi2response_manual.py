# Auto-generated test for dwi2response_manual

from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.medimage_mrtrix3 import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_0 import dwi2response_manual


def test_dwi2response_manual(tmp_path, cli_parse_only):
    task = dwi2response_manual(
        in_file=Nifti1.sample(),
        in_voxels=Nifti1.sample(),
        out_file=File.sample(),
        dirs=Nifti1.sample(),
        grad=File.sample(),
        fslgrad=File.sample(),
        mask=Nifti1.sample(),
        voxels=False,
        shells=list([1.0]),
        lmax=list([1]),
        nocleanup=True,
        scratch=False,
        cont=File.sample(),
        debug=True,
        force=True,
    )
    result = task(plugin="serial")
    assert not result.errored
