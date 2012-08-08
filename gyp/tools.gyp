# GYP file to build various tools.
#
# To build on Linux:
#  ./gyp_skia tools.gyp && make tools
#
# Building on other platforms not tested yet.
#
{
  'includes': [
    'apptype_console.gypi',
  ],
  'targets': [
    {
      # Build all executable targets defined below.
      'target_name': 'tools',
      'type': 'none',
      'dependencies': [
        'skdiff',
        'skhello',
        'skimage',
        'render_pictures',
        'bench_pictures',
        'pinspect',
      ],
    },
    {
      'target_name': 'skdiff',
      'type': 'executable',
      'sources': [
        '../tools/skdiff_main.cpp',
      ],
      'dependencies': [
        'core.gyp:core',
        'effects.gyp:effects',
        'images.gyp:images',
        'ports.gyp:ports',
        'utils.gyp:utils',
      ],
    },
    {
      'target_name': 'skhello',
      'type': 'executable',
      'sources': [
        '../tools/skhello.cpp',
      ],
      'dependencies': [
        'core.gyp:core',
        'effects.gyp:effects',
        'images.gyp:images',
        'ports.gyp:ports',
        'utils.gyp:utils',
      ],
    },
    {
      'target_name': 'skimage',
      'type': 'executable',
      'sources': [
        '../tools/skimage_main.cpp',
      ],
      'dependencies': [
        'core.gyp:core',
        'effects.gyp:effects',
        'images.gyp:images',
        'ports.gyp:ports',
        'utils.gyp:utils',
      ],
    },
    {
      'target_name': 'render_pictures',
      'type': 'executable',
      'sources': [
        '../tools/render_pictures_main.cpp',
      ],
      'include_dirs': [
        '../src/pipe/utils/',
      ],
      'dependencies': [
        'core.gyp:core',
        'images.gyp:images',
        'ports.gyp:ports',
        'tools.gyp:picture_renderer',
        'tools.gyp:picture_utils',
      ],
    },
    {
      'target_name': 'bench_pictures',
      'type': 'executable',
      'sources': [
        '../tools/bench_pictures_main.cpp',
      ],
      'include_dirs': [
        '../bench',
      ],
      'dependencies': [
        'core.gyp:core',
        'ports.gyp:ports',
        'images.gyp:images',
        'tools.gyp:picture_utils',
        'tools.gyp:picture_benchmark',
        'bench.gyp:bench_timer',
      ],
    },
    {
     'target_name': 'picture_benchmark',
     'type': 'static_library',
     'sources': [
        '../tools/PictureBenchmark.cpp',
     ],
     'include_dirs': [
        '../bench',
     ],
     'dependencies': [
        'core.gyp:core',
        'tools.gyp:picture_utils',
        'tools.gyp:picture_renderer',
        'bench.gyp:bench_timer',
     ],
    },
    {
     'target_name': 'picture_renderer',
     'type': 'static_library',
     'sources': [
        '../tools/PictureRenderer.cpp',
        '../src/pipe/utils/SamplePipeControllers.h',
        '../src/pipe/utils/SamplePipeControllers.cpp',
     ],
      'include_dirs': [
        '../src/pipe/utils/',
      ],
     'dependencies': [
        'core.gyp:core',
        'tools.gyp:picture_utils',
     ],
    },
    {
      'target_name': 'picture_utils',
      'type': 'static_library',
      'sources': [
        '../tools/picture_utils.cpp',
      ],
      'dependencies': [
        'core.gyp:core',
      ],
    },
    {
      'target_name': 'pinspect',
      'type': 'executable',
      'sources': [
        '../tools/pinspect.cpp',
      ],
      'dependencies': [
        'core.gyp:core',
        'effects.gyp:effects',
        'images.gyp:images',
        'ports.gyp:ports',
        'utils.gyp:utils',
      ],
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
