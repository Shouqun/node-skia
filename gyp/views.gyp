#Views is the Skia windowing toolkit.
#It provides
#  * a portable means of creating native windows
#  * events
#  * basic widgets and controls

{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'views',
      'type': 'static_library',
      'include_dirs': [
        '../deps/skia/include/config',
        '../deps/skia/include/core',
        '../deps/skia/include/views',
        '../deps/skia/include/xml',
        '../deps/skia/include/utils',
        '../deps/skia/include/images',
        '../deps/skia/include/effects',
        '../deps/skia/include/views/unix',
      ],
      'dependencies': [
        'angle.gyp:*',
      ],
      'sources': [
        '../deps/skia/include/views/SkApplication.h',
        '../deps/skia/include/views/SkBGViewArtist.h',
        '../deps/skia/include/views/SkEvent.h',
        '../deps/skia/include/views/SkEventSink.h',
        '../deps/skia/include/views/SkKey.h',
        '../deps/skia/include/views/SkOSMenu.h',
        '../deps/skia/include/views/SkOSWindow_Mac.h',
        '../deps/skia/include/views/SkOSWindow_SDL.h',
        '../deps/skia/include/views/SkOSWindow_Unix.h',
        '../deps/skia/include/views/SkOSWindow_Win.h',
        #'../deps/skia/include/views/SkOSWindow_wxwidgets.h',
        '../deps/skia/include/views/SkStackViewLayout.h',
        '../deps/skia/include/views/SkSystemEventTypes.h',
        '../deps/skia/include/views/SkTextBox.h',
        '../deps/skia/include/views/SkTouchGesture.h',
        '../deps/skia/include/views/SkView.h',
        '../deps/skia/include/views/SkViewInflate.h',
        '../deps/skia/include/views/SkWidget.h',
        '../deps/skia/include/views/SkWindow.h',

        '../deps/skia/src/views/SkBGViewArtist.cpp',
        '../deps/skia/src/views/SkEvent.cpp',
        '../deps/skia/src/views/SkEventSink.cpp',
        '../deps/skia/src/views/SkOSMenu.cpp',
        '../deps/skia/src/views/SkParsePaint.cpp',
        '../deps/skia/src/views/SkProgressView.cpp',
        '../deps/skia/src/views/SkStackViewLayout.cpp',
        '../deps/skia/src/views/SkTagList.cpp',
        '../deps/skia/src/views/SkTagList.h',
        '../deps/skia/src/views/SkTextBox.cpp',
        '../deps/skia/src/views/SkTouchGesture.cpp',
        '../deps/skia/src/views/SkView.cpp',
        '../deps/skia/src/views/SkViewInflate.cpp',
        '../deps/skia/src/views/SkViewPriv.cpp',
        '../deps/skia/src/views/SkViewPriv.h',
        '../deps/skia/src/views/SkWidget.cpp',
        '../deps/skia/src/views/SkWidgets.cpp',
        '../deps/skia/src/views/SkWindow.cpp',

        #mac
        '../deps/skia/src/views/mac/SkOSWindow_Mac.mm',
        '../deps/skia/src/views/mac/skia_mac.mm',

        #sdl
        '../deps/skia/src/views/SDL/SkOSWindow_SDL.cpp',

        #*nix
        '../deps/skia/src/views/unix/SkOSWindow_Unix.cpp',
        '../deps/skia/src/views/unix/keysym2ucs.c',
        '../deps/skia/src/views/unix/skia_unix.cpp',

        #windows
        '../deps/skia/src/views/win/SkOSWindow_win.cpp',
        '../deps/skia/src/views/win/skia_win.cpp',

      ],
      'sources!' : [
        '../deps/skia/src/views/SDL/SkOSWindow_SDL.cpp',
      ],
      'conditions': [
        [ 'skia_os == "mac"', {
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/Cocoa.framework',
              '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
            ],
          },
        },{
          'sources!': [
            '../deps/skia/src/views/mac/SkOSWindow_Mac.mm',
            '../deps/skia/src/views/mac/skia_mac.mm',
          ],
        }],
        [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris"]', {
        },{
          'sources!': [
            '../deps/skia/src/views/unix/SkOSWindow_Unix.cpp',
            '../deps/skia/src/views/unix/keysym2ucs.c',
            '../deps/skia/src/views/unix/skia_unix.cpp',
          ],
        }],
        [ 'skia_os == "win"', {
        },{
          'sources!': [
            '../deps/skia/src/views/win/SkOSWindow_win.cpp',
            '../deps/skia/src/views/win/skia_win.cpp',
          ],
        }],
        [ 'skia_gpu == 1', {
          'include_dirs': [
            '../deps/skia/include/gpu',
          ],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../deps/skia/include/views',
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
