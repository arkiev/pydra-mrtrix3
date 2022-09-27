from pathlib import Path
import pytest
from pydra.tasks.mrtrix3.utils import MRConvert
from medimages4tests.dicom.mri.dwi.siemens.skyra.syngo_d13c import sample_image


@pytest.fixture
def dicom_dataset():
    return sample_image()


def test_mrconvert_default_out_file(dicom_dataset):

    task = MRConvert(in_file=dicom_dataset, coord=(3, 0))

    result = task()

    assert Path(result.output.out_file).exists()


def test_mrconvert_explicit_out_file(dicom_dataset):

    task = MRConvert(in_file=dicom_dataset, out_file="test.nii.gz")

    result = task()

    assert Path(result.output.out_file).exists()
