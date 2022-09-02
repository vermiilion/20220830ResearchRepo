# Python Koans Exercises

# About Asserts

def test_that_sometimes_we_need_to_know_the_class_type(self):

        self.assertEqual(str, "navel".__class__)
   
 # This test 
 
 # About Strings
 
 def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b))
        
# This one took me a while to figure out. I thought that the test was asking me to rewrite the string using a different combination of single and double quotes
