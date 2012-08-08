{ 
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'pdf',
      'type': 'static_library',
      'dependencies': [
        'core.gyp:core',
        'ports.gyp:ports',
        'utils.gyp:utils',
        'zlib.gyp:zlib',
      ],
      'include_dirs': [
        '../deps/skia/include/config',
        '../deps/skia/include/core',
        '../deps/skia/include/pdf',
        '../deps/skia/src/core', # needed to get SkGlyphCache.h and SkTextFormatParams.h
        '../deps/skia/src/utils', # needed to get SkBitSet.h
      ],
      'sources': [
        '../deps/skia/include/pdf/SkPDFDevice.h',
        '../deps/skia/include/pdf/SkPDFDocument.h',

        '../deps/skia/src/pdf/SkPDFCatalog.cpp',
        '../deps/skia/src/pdf/SkPDFCatalog.h',
        '../deps/skia/src/pdf/SkPDFDevice.cpp',
        '../deps/skia/src/pdf/SkPDFDocument.cpp',
        '../deps/skia/src/pdf/SkPDFFont.cpp',
        '../deps/skia/src/pdf/SkPDFFont.h',
        '../deps/skia/src/pdf/SkPDFFontImpl.h',
        '../deps/skia/src/pdf/SkPDFFormXObject.cpp',
        '../deps/skia/src/pdf/SkPDFFormXObject.h',
        '../deps/skia/src/pdf/SkPDFGraphicState.cpp',
        '../deps/skia/src/pdf/SkPDFGraphicState.h',
        '../deps/skia/src/pdf/SkPDFImage.cpp',
        '../deps/skia/src/pdf/SkPDFImage.h',
        '../deps/skia/src/pdf/SkPDFPage.cpp',
        '../deps/skia/src/pdf/SkPDFPage.h',
        '../deps/skia/src/pdf/SkPDFShader.cpp',
        '../deps/skia/src/pdf/SkPDFShader.h',
        '../deps/skia/src/pdf/SkPDFStream.cpp',
        '../deps/skia/src/pdf/SkPDFStream.h',
        '../deps/skia/src/pdf/SkPDFTypes.cpp',
        '../deps/skia/src/pdf/SkPDFTypes.h',
        '../deps/skia/src/pdf/SkPDFUtils.cpp',
        '../deps/skia/src/pdf/SkPDFUtils.h',
      ],
      # This section makes all targets that depend on this target
      # #define SK_SUPPORT_PDF and have access to the pdf header files.
      'direct_dependent_settings': {
        'defines': [
          'SK_SUPPORT_PDF',
        ],
        'include_dirs': [
          '../deps/skia/include/pdf',
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
