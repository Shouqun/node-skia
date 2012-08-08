{
  'includes' : [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'xml',
      'type': 'static_library',
      'include_dirs': [
        '../deps/skia/include/config',
        '../deps/skia/include/core',
        '../deps/skia/include/xml',
        '../deps/skia/include/utils',
      ],
      'sources': [
        '../deps/skia/include/xml/SkBML_WXMLParser.h',
        '../deps/skia/include/xml/SkBML_XMLParser.h',
        '../deps/skia/include/xml/SkDOM.h',
        '../deps/skia/include/xml/SkJS.h',
        '../deps/skia/include/xml/SkXMLParser.h',
        '../deps/skia/include/xml/SkXMLWriter.h',

        '../deps/skia/src/xml/SkBML_Verbs.h',
        '../deps/skia/src/xml/SkBML_XMLParser.cpp',
        '../deps/skia/src/xml/SkDOM.cpp',
        '../deps/skia/src/xml/SkJS.cpp',
        '../deps/skia/src/xml/SkJSDisplayable.cpp',
        '../deps/skia/src/xml/SkXMLParser.cpp',
        '../deps/skia/src/xml/SkXMLPullParser.cpp',
        '../deps/skia/src/xml/SkXMLWriter.cpp',
      ],
      'sources!': [
          '../deps/skia/src/xml/SkXMLPullParser.cpp', #if 0 around class decl in header
      ],
      'conditions': [
        [ 'skia_os in ["win", "mac", "linux", "freebsd", "openbsd", "solaris", "android"]', {
          'sources!': [
            # no jsapi.h by default on system
            '../deps/skia/include/xml/SkJS.h',
            '../deps/skia/src/xml/SkJS.cpp',
            '../deps/skia/src/xml/SkJSDisplayable.cpp',
          ],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../deps/skia/include/xml',
        ],
      },
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
