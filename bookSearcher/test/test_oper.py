import pytest
from pyparsing import Word, alphas, infixNotation, opAssoc
from bookSearcher.recurPar import evaluate_ast

variable = Word(alphas)
expr = infixNotation(variable, [
    ("NOT", 1, opAssoc.RIGHT),
    ("AND", 2, opAssoc.LEFT),
    ("OR",  2, opAssoc.LEFT),
])

def test_basic():
    UNIVERSE = set([1,2,3,4,5,6,7,8,9,10])
    values = {'azul': [1,2,3], 'rosa': [3,6,9], 'marron': [1,2,4]}
    expected_result = [3,5,6,7,8,9,10]
    parsed = expr.parseString("(azul AND rosa) OR (NOT marron)")
    result = evaluate_ast(parsed[0].asList(), values, UNIVERSE)
    assert expected_result == result

def test_and_simple():
    UNIVERSE = set([1,2,3])
    values = {'a': [1,2], 'b': [2,3]}
    expected_result = [2]
    parsed = expr.parseString("a AND b")
    result = evaluate_ast(parsed[0].asList(), values, UNIVERSE)
    assert expected_result == result

def test_or_simple():
    UNIVERSE = set([1,2,3,4])
    values = {'a': [1,2], 'b': [3,4]}
    expected_result = [1,2,3,4]
    parsed = expr.parseString("a OR b")
    result = evaluate_ast(parsed[0].asList(), values, UNIVERSE)
    assert expected_result == result

def test_not_simple():
    UNIVERSE = set([1,2,3,4])
    values = {'x': [1,2]}
    expected_result = [3,4]
    parsed = expr.parseString("NOT x")
    result = evaluate_ast(parsed[0].asList(), values, UNIVERSE)
    assert expected_result == result

def test_double_not():
    UNIVERSE = set([1,2,3])
    values = {'a': [1,2]}
    expected_result = [1,2]
    parsed = expr.parseString("NOT NOT a")
    result = evaluate_ast(parsed[0].asList(), values, UNIVERSE)
    assert expected_result == result

def test_nested_combination():
    UNIVERSE = set([1,2,3,4])
    values = {'a': [1,2], 'b': [2,3], 'c': [2]}
    # (a OR b) = [1,2,3]; NOT c = [1,3,4]; AND -> [1,3]
    expected_result = [1,3]
    parsed = expr.parseString("(a OR b) AND NOT c")
    result = evaluate_ast(parsed[0].asList(), values, UNIVERSE)
    assert expected_result == result

def test_precedence_without_parentheses():
    UNIVERSE = set([1,2])
    values = {'a': [1], 'b': [1,2], 'c': [2]}
    # b AND c = [2]; a OR [2] = [1,2]
    expected_result = [1,2]
    parsed = expr.parseString("a OR b AND c")
    result = evaluate_ast(parsed[0].asList(), values, UNIVERSE)
    assert expected_result == result

def test_chained_and_left_assoc():
    UNIVERSE = set([1,2,3,4])
    values = {'a': [1,2], 'b': [2,3], 'c': [2,4]}
    # a AND b = [2]; [2] AND c = [2]
    expected_result = [2]
    parsed = expr.parseString("(a AND b) AND c")
    result = evaluate_ast(parsed[0].asList(), values, UNIVERSE)
    assert expected_result == result

def test_chained_or():
    UNIVERSE = set([1,2,3])
    values = {'a': [1], 'b': [2], 'c': [3]}
    # a OR b OR c = [1,2,3]
    expected_result = [1,2,3]
    parsed = expr.parseString("(a OR b) OR c")
    result = evaluate_ast(parsed[0].asList(), values, UNIVERSE)
    assert expected_result == result

def test_complex_mixture():
    UNIVERSE = set([1,2,3,4,5,6])
    values = {
        'p': [1,2,3],
        'q': [2,4],
        'r': [3,5],
        's': [1,6]
    }
    # (p AND q) = [2]; NOT r = [1,2,4,6]; OR s = [1,2,4,6]
    expected_result = [1,2,4,6]
    parsed = expr.parseString("((p AND q) OR (NOT r)) OR s")
    result = evaluate_ast(parsed[0].asList(), values, UNIVERSE)
    assert expected_result == result
