{
  'xcode_settings': {
    'SDKROOT': 'macosx10.6',
    'GCC_OPTIMIZATION_LEVEL': '0'
  },

  'targets' : [
    {
      'target_name' : 'skialib',
      'cflags': [ '-g', '-O0' ],
      'include_dirs' : [
        'deps/skia/include/animator',
        'deps/skia/include/config',
        'deps/skia/include/core/',
        'deps/skia/include/device/',
        'deps/skia/include/effects/',
        'deps/skia/include/gpu/',
        'deps/skia/include/images/',
        'deps/skia/include/pdf/',
        'deps/skia/include/pipe/',
      ],
      'sources' : [
        'src/init.cc',
        'src/skia.cc',
        'src/skia_canvas.cc',
        'src/skia_paint.cc',
        'src/skia_bitmap.cc',
        'src/skia_paint.cc',
      ],
      'dependencies' : [
        'gyp/animator.gyp:animator',
        'gyp/core.gyp:core',
        'gyp/effects.gyp:effects',
        'gyp/gpu.gyp:skgr',
        'gyp/gpu.gyp:gr',
        'gyp/images.gyp:images',
        'gyp/pdf.gyp:pdf',
        'gyp/svg.gyp:svg',
        'gyp/views.gyp:views',
        'gyp/xml.gyp:xml',
      ],
    },
  ],
}
