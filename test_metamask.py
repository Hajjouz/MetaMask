# test_metamask.py
"""
Tests for MetaMask module.
"""

import unittest
from metamask import MetaMask

class TestMetaMask(unittest.TestCase):
    """Test cases for MetaMask class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaMask()
        self.assertIsInstance(instance, MetaMask)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaMask()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
