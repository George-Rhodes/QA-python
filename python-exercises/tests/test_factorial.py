import pytest
from applications import factorial



def test_count_fact():
    assert factorial.fact(6) == 720

def test_fact_teen_number():
    assert factorial.fact(17) == 355687428096000

def test_fact_teen_number():
    assert factorial.fact(0) == 1 
