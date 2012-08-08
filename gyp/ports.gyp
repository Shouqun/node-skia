# Port-specific Skia library code.
{
  'includes':[
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'ports',
      'type': 'static_library',
      'dependencies': [
        'core.gyp:core',
        'sfnt.gyp:sfnt',
        'utils.gyp:utils',
      ],
      'include_dirs': [
        '../deps/skia/include/images',
        '../deps/skia/include/effects',
        '../deps/skia/include/ports',
        '../deps/skia/include/xml',
        '../deps/skia/src/core',
        '../deps/skia/src/utils',
      ],
      'sources': [
        '../deps/skia/src/ports/SkDebug_stdio.cpp',
        '../deps/skia/src/ports/SkDebug_win.cpp',
        '../deps/skia/src/ports/SkFontDescriptor.h',
        '../deps/skia/src/ports/SkFontDescriptor.cpp',
        '../deps/skia/src/ports/SkFontHost_sandbox_none.cpp',
        '../deps/skia/src/ports/SkFontHost_win.cpp',
        '../deps/skia/src/ports/SkGlobalInitialization_default.cpp',
        '../deps/skia/src/ports/SkThread_win.cpp',

        '../deps/skia/src/ports/SkFontHost_tables.cpp',
        '../deps/skia/src/ports/SkMemory_malloc.cpp',
        '../deps/skia/src/ports/SkOSFile_stdio.cpp',
        '../deps/skia/src/ports/SkTime_Unix.cpp',
        '../deps/skia/src/ports/SkTime_win.cpp',
        '../deps/skia/src/ports/SkXMLParser_empty.cpp',
      ],
      'conditions': [
        [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris"]', {
          'sources': [
            '../deps/skia/src/ports/SkThread_pthread.cpp',
            '../deps/skia/src/ports/SkFontHost_FreeType.cpp',
            '../deps/skia/src/ports/SkFontHost_linux.cpp',
          ],
        }],
        [ 'skia_os == "mac"', {
          'include_dirs': [
            '../deps/skia/include/utils/mac',
            '../deps/skia/third_party/freetype/include/**',
          ],
          'sources': [
            '../deps/skia/src/ports/SkFontHost_mac_coretext.cpp',
            '../deps/skia/src/utils/mac/SkStream_mac.cpp',
#            '../deps/skia/src/ports/SkFontHost_FreeType.cpp',
#            '../deps/skia/src/ports/SkFontHost_freetype_mac.cpp',
            '../deps/skia/src/ports/SkThread_pthread.cpp',
          ],
          'sources!': [
            '../deps/skia/src/ports/SkFontHost_tables.cpp',
          ],
        }],
        [ 'skia_os == "ios"', {
          'include_dirs': [
            '../deps/skia/include/utils/ios',
          ],
          'sources': [
            '../deps/skia/src/ports/SkFontHost_mac_coretext.cpp',
            '../deps/skia/src/ports/SkThread_pthread.cpp',
          ],
        }],
        [ 'skia_os == "win"', {
          'include_dirs': [
            'config/win',
          ],
          'sources!': [ # these are used everywhere but windows
            '../deps/skia/src/ports/SkDebug_stdio.cpp',
            '../deps/skia/src/ports/SkTime_Unix.cpp',
          ],
        }, { # else !win
          'sources!': [
            '../deps/skia/src/ports/SkDebug_win.cpp',
            '../deps/skia/src/ports/SkFontHost_win.cpp',
            '../deps/skia/src/ports/SkThread_win.cpp',
            '../deps/skia/src/ports/SkTime_win.cpp',
          ],
        }],
        [ 'skia_os == "android"', {
          'sources!': [
            '../deps/skia/src/ports/SkDebug_stdio.cpp',
          ],
          'sources': [
            '../deps/skia/src/ports/SkDebug_android.cpp',
            '../deps/skia/src/ports/SkThread_pthread.cpp',
            '../deps/skia/src/ports/SkFontHost_android.cpp',
            '../deps/skia/src/ports/SkFontHost_FreeType.cpp',
            '../deps/skia/src/ports/FontHostConfiguration_android.cpp',
            #TODO: include the ports/SkImageRef_ashmem.cpp for non-NDK builds
          ],
          'dependencies': [
             'android_system.gyp:ft2',
             'android_system.gyp:expat',
          ],
        }],        
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../deps/skia/include/ports',
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
