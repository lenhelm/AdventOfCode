from main import main

def test_main():
    expected_scores = (157, 70)
    assert main('test_input.txt') == expected_scores

