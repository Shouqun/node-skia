{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'sfnt',
      'type': 'static_library',
      'dependencies': [
        'core.gyp:core',
      ],
      'include_dirs': [
        '../deps/skia/src/sfnt',
      ],
      'sources': [
        '../deps/skia/src/sfnt/SkIBMFamilyClass.h',
        '../deps/skia/src/sfnt/SkOTTableTypes.h',
        '../deps/skia/src/sfnt/SkOTTable_head.h',
        '../deps/skia/src/sfnt/SkOTTable_hhea.h',
        '../deps/skia/src/sfnt/SkOTTable_name.h',
        '../deps/skia/src/sfnt/SkOTTable_OS_2.h',
        '../deps/skia/src/sfnt/SkOTTable_OS_2_V0.h',
        '../deps/skia/src/sfnt/SkOTTable_OS_2_V1.h',
        '../deps/skia/src/sfnt/SkOTTable_OS_2_V2.h',
        '../deps/skia/src/sfnt/SkOTTable_OS_2_V3.h',
        '../deps/skia/src/sfnt/SkOTTable_OS_2_V4.h',
        '../deps/skia/src/sfnt/SkOTTable_OS_2_VA.h',
        '../deps/skia/src/sfnt/SkOTTable_post.h',
        '../deps/skia/src/sfnt/SkPanose.h',
        '../deps/skia/src/sfnt/SkOTUtils.h',
        '../deps/skia/src/sfnt/SkPreprocessorSeq.h',
        '../deps/skia/src/sfnt/SkSFNTHeader.h',
        '../deps/skia/src/sfnt/SkTypedEnum.h',

        '../deps/skia/src/sfnt/SkOTUtils.cpp',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../deps/skia/src/sfnt',
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
