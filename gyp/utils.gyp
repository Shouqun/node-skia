{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'utils',
      'type': 'static_library',
      'include_dirs': [
        '../deps/skia/include/config',
        '../deps/skia/include/core',
        '../deps/skia/include/effects',
        '../deps/skia/include/pipe',
        '../deps/skia/include/utils',
        '../deps/skia/include/utils/mac',
        '../deps/skia/include/utils/unix',
        '../deps/skia/include/utils/win',
        '../deps/skia/include/xml',
      ],
      'sources': [
        '../deps/skia/include/utils/SkBoundaryPatch.h',
        '../deps/skia/include/utils/SkCamera.h',
        '../deps/skia/include/utils/SkCubicInterval.h',
        '../deps/skia/include/utils/SkCullPoints.h',
        '../deps/skia/include/utils/SkDeferredCanvas.h',
        '../deps/skia/include/utils/SkDumpCanvas.h',
        '../deps/skia/include/utils/SkInterpolator.h',
        '../deps/skia/include/utils/SkLayer.h',
        '../deps/skia/include/utils/SkMatrix44.h',
        '../deps/skia/include/utils/SkMeshUtils.h',
        '../deps/skia/include/utils/SkNinePatch.h',
        '../deps/skia/include/utils/SkNWayCanvas.h',
        '../deps/skia/include/utils/SkNullCanvas.h',
        '../deps/skia/include/utils/SkParse.h',
        '../deps/skia/include/utils/SkParsePaint.h',
        '../deps/skia/include/utils/SkParsePath.h',
        '../deps/skia/include/utils/SkProxyCanvas.h',
        '../deps/skia/include/utils/SkUnitMappers.h',
        '../deps/skia/include/utils/SkWGL.h',

        '../deps/skia/src/utils/SkBase64.cpp',
        '../deps/skia/src/utils/SkBase64.h',
        '../deps/skia/src/utils/SkBitSet.cpp',
        '../deps/skia/src/utils/SkBitSet.h',
        '../deps/skia/src/utils/SkBoundaryPatch.cpp',
        '../deps/skia/src/utils/SkCamera.cpp',
        '../deps/skia/src/utils/SkCubicInterval.cpp',
        '../deps/skia/src/utils/SkCullPoints.cpp',
        '../deps/skia/src/utils/SkDeferredCanvas.cpp',
        '../deps/skia/src/utils/SkDumpCanvas.cpp',
        '../deps/skia/src/utils/SkInterpolator.cpp',
        '../deps/skia/src/utils/SkLayer.cpp',
        '../deps/skia/src/utils/SkMatrix44.cpp',
        '../deps/skia/src/utils/SkMeshUtils.cpp',
        '../deps/skia/src/utils/SkNinePatch.cpp',
        '../deps/skia/src/utils/SkNWayCanvas.cpp',
        '../deps/skia/src/utils/SkNullCanvas.cpp',
        '../deps/skia/src/utils/SkOSFile.cpp',
        '../deps/skia/src/utils/SkParse.cpp',
        '../deps/skia/src/utils/SkParseColor.cpp',
        '../deps/skia/src/utils/SkParsePath.cpp',
        '../deps/skia/src/utils/SkProxyCanvas.cpp',
        '../deps/skia/src/utils/SkThreadUtils.h',
        '../deps/skia/src/utils/SkThreadUtils_pthread.cpp',
        '../deps/skia/src/utils/SkThreadUtils_pthread.h',
        '../deps/skia/src/utils/SkThreadUtils_pthread_linux.cpp',
        '../deps/skia/src/utils/SkThreadUtils_pthread_mach.cpp',
        '../deps/skia/src/utils/SkThreadUtils_pthread_other.cpp',
        '../deps/skia/src/utils/SkThreadUtils_win.cpp',
        '../deps/skia/src/utils/SkThreadUtils_win.h',
        '../deps/skia/src/utils/SkUnitMappers.cpp',

        #mac
        '../deps/skia/include/utils/mac/SkCGUtils.h',
        '../deps/skia/src/utils/mac/SkCreateCGImageRef.cpp',
        
        #windows
        '../deps/skia/include/utils/win/SkAutoCoInitialize.h',
        '../deps/skia/include/utils/win/SkHRESULT.h',
        '../deps/skia/include/utils/win/SkIStream.h',
        '../deps/skia/include/utils/win/SkTScopedComPtr.h',
        '../deps/skia/src/utils/win/SkAutoCoInitialize.cpp',
        '../deps/skia/src/utils/win/SkHRESULT.cpp',
        '../deps/skia/src/utils/win/SkIStream.cpp',
        '../deps/skia/src/utils/win/SkWGL_win.cpp',
      ],
      'sources!': [
          '../deps/skia/src/utils/SDL/SkOSWindow_SDL.cpp',
      ],
      'conditions': [
        [ 'skia_os == "mac"', {
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/AGL.framework',
            ],
          },
          'direct_dependent_settings': {
            'include_dirs': [
              '../deps/skia/include/utils/mac',
            ],
          },
          'sources!': [
            '../deps/skia/src/utils/SkThreadUtils_pthread_other.cpp',
          ],
        },{ #else if 'skia_os != "mac"'
          'include_dirs!': [
            '../deps/skia/include/utils/mac',
          ],
          'sources!': [
            '../deps/skia/include/utils/mac/SkCGUtils.h',
            '../deps/skia/src/utils/mac/SkCreateCGImageRef.cpp',
            '../deps/skia/src/utils/SkThreadUtils_pthread_mach.cpp',
          ],
        }],
        [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris"]', {
          'link_settings': {
            'libraries': [
              '-lGL',
              '-lGLU',
            ],
          },
          'sources!': [
            '../deps/skia/src/utils/SkThreadUtils_pthread_other.cpp',
          ],
        },{ #else if 'skia_os not in ["linux", "freebsd", "openbsd", "solaris"]'
          'include_dirs!': [
            '../deps/skia/include/utils/unix',
          ],
          'sources!': [
            '../deps/skia/src/utils/SkThreadUtils_pthread_linux.cpp',
          ],
        }],
        [ 'skia_os == "win"', {
          'direct_dependent_settings': {
            'include_dirs': [
              '../deps/skia/include/utils/win',
            ],
          },
          'sources!': [
            '../deps/skia/src/utils/SkThreadUtils_pthread.cpp',
            '../deps/skia/src/utils/SkThreadUtils_pthread.h',
            '../deps/skia/src/utils/SkThreadUtils_pthread_other.cpp',
          ],
        },{ #else if 'skia_os != "win"'
          'include_dirs!': [
            '../deps/skia/include/utils/win',
          ],
          'sources/': [ ['exclude', '_win.(h|cpp)$'],],
          'sources!': [
            '../deps/skia/include/utils/win/SkAutoCoInitialize.h',
            '../deps/skia/include/utils/win/SkHRESULT.h',
            '../deps/skia/include/utils/win/SkIStream.h',
            '../deps/skia/include/utils/win/SkTScopedComPtr.h',
            '../deps/skia/src/utils/win/SkAutoCoInitialize.cpp',
            '../deps/skia/src/utils/win/SkHRESULT.cpp',
            '../deps/skia/src/utils/win/SkIStream.cpp',
          ],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../deps/skia/include/utils',
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
