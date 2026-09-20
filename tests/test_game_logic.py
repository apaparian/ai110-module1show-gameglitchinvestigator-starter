from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

def test_guess_high_when_secret_is_string():
    # Regression test for the high/low bug: when secret is passed as a
    # string (as app.py does on every other attempt), comparisons must
    # still be numeric, not lexicographic (e.g. "9" > "50" as strings).
    outcome, _ = check_guess(9, "50")
    assert outcome == "Too Low"

def test_guess_low_when_secret_is_string():
    outcome, _ = check_guess(100, "50")
    assert outcome == "Too High"

def test_too_high_message_says_go_lower():
    # Regression test: outcome "Too High" means the guess exceeded the
    # secret, so the hint must tell the player to go LOWER, not higher.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
