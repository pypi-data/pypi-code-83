import pytest
#import makeslug
import mkslug

class TestMakeSlug:
    def test_check_for_errors_regular_sentence(self):
        """
        Test check_for_errors function works successfully when a regular sentence provided.
        """

        error, error_text = mkslug.check_for_errors("Test SLUG vaLUEs 1")

        assert error == True
        assert error_text != None

    def test_check_for_errors_empty_sentence(self):
        """
        Test check_for_errors function raising an error when no sentence provided.
        """

        error, error_text = mkslug.check_for_errors("")

        assert error == True
        assert error_text == None

    def test_check_for_errors_special_characters_in_sentence(self):
        """
        Test check_for_errors function raising an error when special characters in a sentence provided.
        """

        error, error_text = mkslug.check_for_errors("%One slug ^* value  $  ")

        assert error == True
        assert error_text != None

    def test_generate_regular_sentence(self):
        """
        Test generate function works successfully when a regular sentence provided.
        """

        slug = mkslug.generate("Test SLUG vaLUEs 1")

        assert slug == "test-slug-values-1"

    def test_generate_outer_chars_are_blank(self):
        """
        Test generate function works successfully when the outer characters are blank provided.
        """

        slug = mkslug.generate("    Test SLUG vaLUEs 2  ")

        assert slug == "test-slug-values-2"
