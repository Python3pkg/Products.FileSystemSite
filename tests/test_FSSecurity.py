import Zope

from unittest import TestSuite, makeSuite, main
from types import ListType
from os import remove
from os.path import join
from time import sleep

from AccessControl.Permission import Permission
from Products.CMFCore.tests.base.testcase import RequestTest
from test_DirectoryView import _registerDirectory, _prefix
from Globals import DevelopmentMode

class FSSecurityBase( RequestTest ):

    def _checkSettings(self,object,permissionname,acquire=0,roles=[]):
        # check the roles and acquire settings for a permission on an
        # object are as expected
        happy=0
        for pstuff in object.ac_inherited_permissions(1):
            name,value = pstuff[:2]
            if name==permissionname:
                p = Permission(name,value,object)
                groles=p.getRoles(default=[])
                acquired=isinstance(groles,ListType)
                expected={}
                for role in roles:
                    expected[role]=1
                got={}
                for role in groles:
                    got[role]=1
                self.assertEqual((acquire,expected),(acquired,got))
                happy=1
        if not happy:
            raise ValueError,"'%s' not found in permissions: %s" % (permissionname,all_names)
            
    _path = join(_prefix,'fake_skins','fake_skin')
    
    def _writeFile(self, filename, stuff):
        # write some stuff to a file on disk
        thePath = join(self._path,filename)
        f = open(thePath,'w')
        f.write(stuff)
        f.close()
        
    def _deleteFile(self,filename):
        # nuke it
        remove(join(self._path,filename))
        
    def setUp( self ):
        # initialise skins
        _registerDirectory(self)
        # set up ZODB
        RequestTest.setUp(self)
        # put object in ZODB
        root=self.root
        try: root._delObject('fake_skin')
        except AttributeError: pass
        root._setObject( 'fake_skin', self.ob.fake_skin )

    def tearDown( self ):
        try:
            self._deleteFile('test5.py.security')
        except:
            pass
        RequestTest.tearDown(self)
        
class FSSecurityTests( FSSecurityBase ):

    def test_basicPermissions( self ):
        """ Test basic FS permissions """
        # check a normal method is as we'd expect
        self._checkSettings(self.ob.fake_skin.test1,'View',1,[])
        # now do some checks on the method with FS permissions
        self._checkSettings(self.ob.fake_skin.test4,'View',1,['Manager','Owner'])
        self._checkSettings(self.ob.fake_skin.test4,'Access contents information',0,[])

    def test_invalidPermissionNames( self ):
        """ Test for an invalid permission name """
        # baseline
        self._checkSettings(self.ob.fake_skin.test5,'View',1,[])
        # add .rpm with dodgy permission name
        self._writeFile('test5.py.security','Access stoopid contents::')
        # check baseline
        self._checkSettings(self.ob.fake_skin.test5,'View',1,[])
        
    def test_invalidAcquireNames( self ):
        """ Test for an invalid spelling of acquire """
        # baseline
        self._checkSettings(self.ob.fake_skin.test5,'View',1,[])
        # add dodgy .rpm
        self._writeFile('test5.py.security','View:aquire:')
        # check baseline
        self._checkSettings(self.ob.fake_skin.test5,'View',1,[])

if DevelopmentMode:

    class DebugModeTests( FSSecurityBase ):
        
        def test_addPRM( self ):
            """ Test adding of a .security """
            # baseline
            self._checkSettings(self.ob.fake_skin.test5,'View',1,[])
            # add
            self._writeFile('test5.py.security','View:acquire:Manager')
            # test            
            self._checkSettings(self.ob.fake_skin.test5,'View',1,['Manager'])

        def test_delPRM( self ):
            """ Test deleting of a .security """
            # baseline
            self._checkSettings(self.ob.fake_skin.test5,'View',1,[])
            self._writeFile('test5.py.security','View:acquire:Manager')
            self._checkSettings(self.ob.fake_skin.test5,'View',1,['Manager'])
            # delete
            self._deleteFile('test5.py.security')
            # test
            self._checkSettings(self.ob.fake_skin.test5,'View',1,[])

        def test_editPRM( self ):
            """ Test editing a .security """
            # we need to wait a second here or the mtime will actually
            # have the same value as set in the last test.
            # Maybe someone brainier than me can figure out a way to make this
            # suck less :-(            
            sleep(1)
            
            # baseline
            self._writeFile('test5.py.security','View::Manager,Anonymous')
            self._checkSettings(self.ob.fake_skin.test5,'View',0,['Manager','Anonymous'])
            
            

            # edit
            self._writeFile('test5.py.security','View:acquire:Manager')
            # test
            self._checkSettings(self.ob.fake_skin.test5,'View',1,['Manager'])


        def test_DelAddEditPRM( self ):
            """ Test deleting, then adding, then editing a .security file """
            # baseline
            self._writeFile('test5.py.security','View::Manager')

            # delete
            self._deleteFile('test5.py.security')
            self._checkSettings(self.ob.fake_skin.test5,'View',1,[])

            # we need to wait a second here or the mtime will actually
            # have the same value, no human makes two edits in less
            # than a second ;-)
            sleep(1)
            
            # add back
            self._writeFile('test5.py.security','View::Manager,Anonymous')
            self._checkSettings(self.ob.fake_skin.test5,'View',0,['Manager','Anonymous'])

            # edit
            self._writeFile('test5.py.security','View:acquire:Manager')

            # test
            self._checkSettings(self.ob.fake_skin.test5,'View',1,['Manager'])

else:

    class DebugModeTests( FSSecurityBase ):
        pass

def test_suite():
    return TestSuite((
        makeSuite(FSSecurityTests),
        makeSuite(DebugModeTests),        
        ))

if __name__ == '__main__':
    main(defaultTest='test_suite')



