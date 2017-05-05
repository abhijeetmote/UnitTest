#!/usr/bin/python
# =============================================================================
# $Id: test_alias.py,v 1.1 2012/04/03 15:17:47 josht Exp $
# =============================================================================
# Copyright (C) 2011 Rhythm & Hues Studios
# An unpublished work by Rhythm & Hues Studios.  All rights reserved.
# =============================================================================
# Module: rh.mail.alias.tests.test_alias
# Contacts: PipelineDept
# =============================================================================
"""Unit tests for rh.mail.alias.Alias"""

import unittest

# =============================================================================
class AliasTestSuite(unittest.TestSuite):
    """A test suite for alias objects."""

    # =========================================================================
    def __init__(self):
        super(AliasTestSuite, self).__init__()

        # ---- add test cases

        self.addTest(AliasTestCase('test_category'))
        self.addTest(AliasTestCase('test_creationDate'))
        self.addTest(AliasTestCase('test_creator'))
        self.addTest(AliasTestCase('test_description'))
        self.addTest(AliasTestCase('test_emails'))
        self.addTest(AliasTestCase('test_expandedUsers'))
        self.addTest(AliasTestCase('test_expirationDate'))
        self.addTest(AliasTestCase('test_id'))
        self.addTest(AliasTestCase('test_isActive'))
        self.addTest(AliasTestCase('test_isPrecious'))
        self.addTest(AliasTestCase('test_job'))
        self.addTest(AliasTestCase('test_lastUsedDate'))
        self.addTest(AliasTestCase('test_lastUsedIndirectlyDate'))
        self.addTest(AliasTestCase('test_name'))
        self.addTest(AliasTestCase('test_users'))
        self.addTest(AliasTestCase('test_getAliasNamesForUser'))
        self.addTest(AliasTestCase('test_getAllAliasNames'))

# =============================================================================
class AliasTestCase(unittest.TestCase):
    """Validate the properties/methods of an Alias object."""    

    # =========================================================================
    def setUp(self):
        """Get an alias object for use in each test."""
        from rh.mail.alias import Alias 
        self._alias = Alias('randh')

    # =========================================================================
    def test_category(self):
        """rh.mail.alias.Alias().category:"""

        category = self._alias.category
        self.assertTrue(isinstance(category, str))

    # =========================================================================
    def test_creationDate(self):
        """rh.mail.alias.Alias().creationDate:"""

        import datetime

        created = self._alias.creationDate
        self.assertTrue(isinstance(created, datetime.datetime))

    # =========================================================================
    def test_creator(self):
        """rh.mail.alias.Alias().creator:"""

        creator = self._alias.creator
        self.assertTrue(isinstance(creator, str))

    # =========================================================================
    def test_description(self):
        """rh.mail.alias.Alias().description:"""

        desc = self._alias.description
        self.assertTrue(isinstance(desc, str))

    # =========================================================================
    def test_emails(self):
        """rh.mail.alias.Alias().emails:"""

        emails = self._alias.emails
        for email in emails:
            self.assertTrue(isinstance(email, str))

    # =========================================================================
    def test_expandedUsers(self):
        """rh.mail.alias.Alias().expandedUsers:"""

        users = self._alias.expandedUsers
        for user in users:
            self.assertTrue(isinstance(user, str))

    # =========================================================================
    def test_expirationDate(self):
        """rh.mail.alias.Alias().expirationDate:"""

        import datetime

        expiration = self._alias.expirationDate
        self.assertTrue(isinstance(expiration, datetime.date))

    # =========================================================================
    def test_id(self):
        """rh.mail.alias.Alias().id:"""

        id = self._alias.id
        self.assertTrue(isinstance(id, int))

    # =========================================================================
    def test_isActive(self):
        """rh.mail.alias.Alias().isActive():"""

        active = self._alias.isActive()
        self.assertTrue(isinstance(active, bool))
    
    # =========================================================================
    def test_isPrecious(self):
        """rh.mail.alias.Alias().isPrecious():"""

        precious = self._alias.isPrecious()
        self.assertTrue(isinstance(precious, bool))
    
    # =========================================================================
    def test_job(self):
        """rh.mail.alias.Alias().job:"""

        job = self._alias.job
        self.assertTrue(isinstance(job, str))

    # =========================================================================
    def test_lastUsedDate(self):
        """rh.mail.alias.Alias().lastUsedDate:"""

        import datetime

        lastUsed = self._alias.lastUsedDate
        self.assertTrue(isinstance(lastUsed, datetime.date))

    # =========================================================================
    def test_lastUsedIndirectlyDate(self):
        """rh.mail.alias.Alias().lastUsedIndirectlyDate:"""

        import datetime

        lastUsedIndirectly = self._alias.lastUsedIndirectlyDate
        self.assertTrue(isinstance(lastUsedIndirectly, datetime.date))
     
    # =========================================================================
    def test_name(self):
        """rh.mail.alias.Alias().name:"""

        name = self._alias.name
        self.assertTrue(isinstance(name, str))

    # =========================================================================
    def test_users(self):
        """rh.mail.alias.Alias().users:"""

        users = self._alias.users
        for user in users:
            self.assertTrue(isinstance(user, str))

    # =========================================================================
    def test_getAliasNamesForUser(self):
        """rh.mail.alias.Alias().getAliasNamesForUser():"""

        import rh.mail.alias
        aliasNames = rh.mail.alias.getAliasNamesForUser('huang')
        for aliasName in aliasNames:
            self.assertTrue(isinstance(aliasName, str))
        
    # =========================================================================
    def test_getAllAliasNames(self):
        """rh.mail.alias.Alias().getAllAliasNames():"""

        import rh.mail.alias
        aliasNames = rh.mail.alias.getAllAliasNames()
        for aliasName in aliasNames:
            self.assertTrue(isinstance(aliasName, str))

# =============================================================================
if __name__ == '__main__':

    # allow these tests to be run on the command line
    import rh.argument

    # pylint: disable=C0103
    parser = rh.argument.ArgumentParser()
    parser.add_argument(
        '-verbosity',
        help='Set the output verbosity',
        action='store',
        type=int,
        metavar='int',
        default=2
    )

    # pylint: disable=C0103
    args = parser.parse_args()
    unittest.TextTestRunner(verbosity=args.verbosity).run(AliasTestSuite())

