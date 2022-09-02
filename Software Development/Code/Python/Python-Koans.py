# Python Koans Exercises

# First Impressions: I didn't really understand what the tests were asking me. The name of the tests seemed a bit confusing and the comments seem to give away the answer. I would input the answers but I didn't feel any closer to enlightenment.
 
 # About Strings
 def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b))
        
# This one took me a while to figure out. I thought that the test was asking me to rewrite the string using a different combination of single and double quotes, so I ended up spending a lot of time trying diffrent ways to do this.
# I eventually realised it was similar to the tests in about_asserts. If (a == b) is True, then "True" what I need to input in order to make the test pass since both items in Self.assertEqual must be equal to each other.

def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        self.assertEqual(52, len(string))
        
# I actually got the correct answer from this from inputting a random guess and the terminal spitting out:
# You have not yet reached enlightenment ...
  #AssertionError: __ != 52
# The error message basically gave me the answer. This made me think of one Python principle: "In the face of ambiguity, refuse the temptation to guess."
# Getting the answer from the error message didn't make me feel any more enlightened, but I made sure to go back and try to understand why 52 is the correct answer.
