
import DirectoryView

import FSImage
import FSPropertiesObject
import FSSTXMethod
import FSDTMLMethod
import FSPageTemplate
import FSZSQLMethod
import FSPythonScript
import FSExternalMethod

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

