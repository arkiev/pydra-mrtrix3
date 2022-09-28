from pathlib import Path
import pytest
from pydra.tasks.mrtrix3.utils import MRConvert
from medimages4tests.dicom.mri.dwi.siemens.skyra.syngo_d13c import (
    sample_image as sample_dwi_dicom,
)
from medimages4tests.nifti import sample_image as sample_nifti


@pytest.fixture
def dwi_dicom_dataset():
    return sample_dwi_dicom()


@pytest.fixture
def nifti_dataset(work_dir):
    return sample_nifti(work_dir / "nifti", compressed=True)


def test_mrconvert_default_out_file(nifti_dataset):

    task = MRConvert(in_file=nifti_dataset, axes=[0, 1, 2, -1])

    result = task()

    assert Path(result.output.out_file).exists()


@pytest.mark.skip(
    "Skip test of mrconvert with explicit out_file field provided until "
    "https://github.com/nipype/pydra/pull/585 (or equivalent) is merged "
    "into main branch"
)
def test_mrconvert_explicit_out_file(dwi_dicom_dataset):

    task = MRConvert(in_file=dwi_dicom_dataset, out_file="test.nii.gz")

    result = task()

    assert Path(result.output.out_file).exists()
