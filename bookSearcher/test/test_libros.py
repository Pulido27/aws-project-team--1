import pytest
from bookSearcher.test.recurPar_Prueba import bookSearch

def test_OR():
    expected = ["Disordered Chronicles: A Nameless Prince's Journey in a Chaotic Kingdom", 'Labyrinth of Distorted Dreams: A Chaotic Narrative of Urban Illusions']

    assert set(bookSearch("vida OR suenoz")) == set(expected)
    
def test_AND():
    expected = ['Labyrinth of Distorted Dreams: A Chaotic Narrative of Urban Illusions']
    
    assert set(bookSearch("NOT pedro AND vida")) == set(expected)
    
def test_NOT():
    expected = ['Labyrinth of Distorted Dreams: A Chaotic Narrative of Urban Illusions', "Disordered Chronicles: A Nameless Prince's Journey in a Chaotic Kingdom", '', 'Erratic Sun: A Chaotic Portrait of a Nameless City']
    
    assert set(bookSearch("NOT computadora")) == set(expected)
    
def test_singleWord():
    expected = ['Labyrinth of Distorted Dreams: A Chaotic Narrative of Urban Illusions']
    
    assert set(bookSearch("vida")) == set(expected)
    
def test_OR_AND():
    expected = ["Disordered Chronicles: A Nameless Prince's Journey in a Chaotic Kingdom", 'Labyrinth of Distorted Dreams: A Chaotic Narrative of Urban Illusions']

    assert set(bookSearch("vida AND susurro OR todo")) == set(expected)