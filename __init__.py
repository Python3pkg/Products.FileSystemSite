
import DirectoryView

import FSImage
import FSFile
import FSPropertiesObject
import FSSTXMethod
import FSDTMLMethod
import FSPageTemplate
import FSZSQLMethod
import FSPythonScript
import FSExternalMethod
import TrustedFSPythonScript

def initialize(context):

    context.registerClass(
            DirectoryView.DirectoryViewSurrogate,
            constructors=(('manage_addDirectoryViewForm',
                           DirectoryView.manage_addDirectoryViewForm),
                          DirectoryView.manage_addDirectoryView,
                          DirectoryView.manage_listAvailableDirectories,
                          ),
            icon='images/dirview.gif'            
    )

    utils.registerIcon(FSPageTemplate.FSPageTemplate,
                       'images/fspt.gif', globals())
    utils.registerIcon(FSDTMLMethod.FSDTMLMethod,
                       'images/fsdtml.gif', globals())
    utils.registerIcon(FSPythonScript.FSPythonScript,
                       'images/fspy.gif', globals())
    utils.registerIcon(TrustedFSPythonScript.TrustedFSPythonScript,
                       'images/fspy.gif', globals())
    utils.registerIcon(FSImage.FSImage,
                       'images/fsimage.gif', globals())
    utils.registerIcon(FSFile.FSFile,
                       'images/fsfile.gif', globals())
    utils.registerIcon(FSPropertiesObject.FSPropertiesObject,
                       'images/fsprops.gif', globals())
    utils.registerIcon(FSZSQLMethod.FSZSQLMethod,
                       'images/fssqlmethod.gif', globals())
