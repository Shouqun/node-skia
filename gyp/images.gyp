{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'images',
      'type': 'static_library',
      'dependencies': [
        'libjpeg.gyp:*',
        'utils.gyp:utils',
      ],
      'export_dependent_settings': [
        'libjpeg.gyp:*',
      ],
      'include_dirs': [
        '../deps/skia/include/config',
        '../deps/skia/include/core',
        '../deps/skia/include/images',
      ],
      'sources': [
        '../deps/skia/include/images/SkFlipPixelRef.h',
        '../deps/skia/include/images/SkImageDecoder.h',
        '../deps/skia/include/images/SkImageEncoder.h',
        '../deps/skia/include/images/SkImageRef.h',
        '../deps/skia/include/images/SkImageRef_GlobalPool.h',
        '../deps/skia/include/images/SkJpegUtility.h',
        '../deps/skia/include/images/SkMovie.h',
        '../deps/skia/include/images/SkPageFlipper.h',

        '../deps/skia/src/images/bmpdecoderhelper.cpp',
        '../deps/skia/src/images/bmpdecoderhelper.h',
        '../deps/skia/src/images/SkFDStream.cpp',
        '../deps/skia/src/images/SkFlipPixelRef.cpp',
        '../deps/skia/src/images/SkImageDecoder.cpp',
        '../deps/skia/src/images/SkImageDecoder_Factory.cpp',
        '../deps/skia/src/images/SkImageDecoder_libjpeg.cpp',
        '../deps/skia/src/images/SkImageDecoder_libbmp.cpp',
        '../deps/skia/src/images/SkImageDecoder_libgif.cpp',
        '../deps/skia/src/images/SkImageDecoder_libico.cpp',
        '../deps/skia/src/images/SkImageDecoder_libpng.cpp',
        '../deps/skia/src/images/SkImageDecoder_wbmp.cpp',
        '../deps/skia/src/images/SkImageEncoder.cpp',
        '../deps/skia/src/images/SkImageEncoder_Factory.cpp',
        '../deps/skia/src/images/SkImageRef.cpp',
        '../deps/skia/src/images/SkImageRefPool.cpp',
        '../deps/skia/src/images/SkImageRefPool.h',
        '../deps/skia/src/images/SkImageRef_GlobalPool.cpp',
        '../deps/skia/src/images/SkJpegUtility.cpp',
        '../deps/skia/src/images/SkMovie.cpp',
        '../deps/skia/src/images/SkMovie_gif.cpp',
        '../deps/skia/src/images/SkPageFlipper.cpp',
        '../deps/skia/src/images/SkScaledBitmapSampler.cpp',
        '../deps/skia/src/images/SkScaledBitmapSampler.h',

        '../deps/skia/src/ports/SkImageDecoder_CG.cpp',
        '../deps/skia/src/ports/SkImageDecoder_WIC.cpp',
      ],
      'conditions': [
        [ 'skia_os == "win"', {
          'sources!': [
            '../deps/skia/src/images/SkFDStream.cpp',
            '../deps/skia/src/images/SkImageDecoder_Factory.cpp',
            '../deps/skia/src/images/SkImageDecoder_libgif.cpp',
            '../deps/skia/src/images/SkImageDecoder_libpng.cpp',
            '../deps/skia/src/images/SkImageEncoder_Factory.cpp',
            '../deps/skia/src/images/SkMovie_gif.cpp',
          ],
          'link_settings': {
            'libraries': [
              'windowscodecs.lib',
            ],
          },
        },{ #else if skia_os != win
          'sources!': [
            '../deps/skia/src/ports/SkImageDecoder_WIC.cpp',
          ],
        }],
        [ 'skia_os == "mac"', {
          'sources!': [
            '../deps/skia/src/images/SkImageDecoder_Factory.cpp',
            '../deps/skia/src/images/SkImageDecoder_libpng.cpp',
            '../deps/skia/src/images/SkImageDecoder_libgif.cpp',
            '../deps/skia/src/images/SkImageEncoder_Factory.cpp',
            '../deps/skia/src/images/SkMovie_gif.cpp',
          ],
        },{ #else if skia_os != mac
          'sources!': [
            '../deps/skia/src/ports/SkImageDecoder_CG.cpp',
          ],
        }],
        [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris"]', {
          'sources!': [
            '../deps/skia/src/images/SkImageDecoder_libgif.cpp',
            '../deps/skia/src/images/SkMovie_gif.cpp',
          ],
          # libpng stuff:
          # Any targets that depend on this target should link in libpng and
          # our code that calls it.
          # See http://code.google.com/p/gyp/wiki/InputFormatReference#Dependent_Settings
          'link_settings': {
            'sources': [
              '../deps/skia/src/images/SkImageDecoder_libpng.cpp',
            ],
            'libraries': [
              '-lpng',
            ],
          },
          # end libpng stuff
        }],
        [ 'skia_os == "android"', {
          'sources!': [
          ],
          'dependencies': [
             'android_system.gyp:gif',
             'android_system.gyp:png',
          ],
          'defines': [
            'SK_ENABLE_LIBPNG',
          ],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../deps/skia/include/images',
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
