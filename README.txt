FileSystemSite

  This is a repackaging of the CMF's FileSystem Directory Views such
  that it is independent of the CMF.

  The major use of this is to develop view code on the file system
  such that it can be edited with normal development utilties and
  checked into a source control management system.

  The only additions are some minor modifications to the FSZSQLMethods
  for argument handling, some EditorUtils for setting syntax
  highlighting, the addition of FSExternalMethods, and some templates
  for common fs types.

  An example of how to use this can be found in the ExampleSite
  subdirectory. That directory should be moved into the Products
  directory and it will register its subdirectory as an
  FSDirectoryView which will make it accessible for addition from the
  ZMI screens.

 Packager

   kapil thangavelu (kvthan@wm.edu)

 Author

   Zope Corp.

 License

   ZPL 2.0


