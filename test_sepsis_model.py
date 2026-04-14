import pytest
from sepsis_model import check_sepsis_risk

def test_high_risk_patient_flagged():
    assert check_sepsis_risk(110, 39.1, 25)

def test_normal_patient_not_flagged():
    assert not check_sepsis_risk(75, 37.0, 16)

def test_boundary_conditions():
    assert check_sepsis_risk(91, 38.4, 21)

def test_invalid_heart_rate_raises_error():
    with pytest.raises(ValueError):
        check_sepsis_risk(0, 37.0, 16)

def test_invalid_temperature_raises_error():
    with pytest.raises(ValueError):
        check_sepsis_risk(75, 20.0, 16)
