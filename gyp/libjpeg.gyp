# Copyright 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This is a copy of ../deps/skia/third_party/externals/libjpeg/libjpeg.gyp , modified
# such that all source paths point into that directory.
# See http://code.google.com/p/skia/issues/detail?id=543 ('wrap libjpeg.gyp
# from Chrome's libjpeg port, rather than making our own copy') for a better
# long-term solution.

{
  'includes': [
    'common.gypi',
  ],
  'variables': {
    'use_system_libjpeg%': 0,
  },
  'conditions': [
    ['use_system_libjpeg==0', {
      'targets': [
        {
          'target_name': 'libjpeg',
          'type': 'static_library',
          'sources': [
            '../deps/skia/third_party/externals/libjpeg/jcapimin.c',
            '../deps/skia/third_party/externals/libjpeg/jcapistd.c',
            '../deps/skia/third_party/externals/libjpeg/jccoefct.c',
            '../deps/skia/third_party/externals/libjpeg/jccolor.c',
            '../deps/skia/third_party/externals/libjpeg/jcdctmgr.c',
            '../deps/skia/third_party/externals/libjpeg/jchuff.c',
            '../deps/skia/third_party/externals/libjpeg/jchuff.h',
            '../deps/skia/third_party/externals/libjpeg/jcinit.c',
            '../deps/skia/third_party/externals/libjpeg/jcmainct.c',
            '../deps/skia/third_party/externals/libjpeg/jcmarker.c',
            '../deps/skia/third_party/externals/libjpeg/jcmaster.c',
            '../deps/skia/third_party/externals/libjpeg/jcomapi.c',
            '../deps/skia/third_party/externals/libjpeg/jconfig.h',
            '../deps/skia/third_party/externals/libjpeg/jcparam.c',
            '../deps/skia/third_party/externals/libjpeg/jcphuff.c',
            '../deps/skia/third_party/externals/libjpeg/jcprepct.c',
            '../deps/skia/third_party/externals/libjpeg/jcsample.c',
            '../deps/skia/third_party/externals/libjpeg/jdapimin.c',
            '../deps/skia/third_party/externals/libjpeg/jdapistd.c',
            '../deps/skia/third_party/externals/libjpeg/jdatadst.c',
            '../deps/skia/third_party/externals/libjpeg/jdatasrc.c',
            '../deps/skia/third_party/externals/libjpeg/jdcoefct.c',
            '../deps/skia/third_party/externals/libjpeg/jdcolor.c',
            '../deps/skia/third_party/externals/libjpeg/jdct.h',
            '../deps/skia/third_party/externals/libjpeg/jddctmgr.c',
            '../deps/skia/third_party/externals/libjpeg/jdhuff.c',
            '../deps/skia/third_party/externals/libjpeg/jdhuff.h',
            '../deps/skia/third_party/externals/libjpeg/jdinput.c',
            '../deps/skia/third_party/externals/libjpeg/jdmainct.c',
            '../deps/skia/third_party/externals/libjpeg/jdmarker.c',
            '../deps/skia/third_party/externals/libjpeg/jdmaster.c',
            '../deps/skia/third_party/externals/libjpeg/jdmerge.c',
            '../deps/skia/third_party/externals/libjpeg/jdphuff.c',
            '../deps/skia/third_party/externals/libjpeg/jdpostct.c',
            '../deps/skia/third_party/externals/libjpeg/jdsample.c',
            '../deps/skia/third_party/externals/libjpeg/jerror.c',
            '../deps/skia/third_party/externals/libjpeg/jerror.h',
            '../deps/skia/third_party/externals/libjpeg/jfdctflt.c',
            '../deps/skia/third_party/externals/libjpeg/jfdctfst.c',
            '../deps/skia/third_party/externals/libjpeg/jfdctint.c',
            '../deps/skia/third_party/externals/libjpeg/jidctflt.c',
            '../deps/skia/third_party/externals/libjpeg/jidctfst.c',
            '../deps/skia/third_party/externals/libjpeg/jidctint.c',
            '../deps/skia/third_party/externals/libjpeg/jinclude.h',
            '../deps/skia/third_party/externals/libjpeg/jmemmgr.c',
            '../deps/skia/third_party/externals/libjpeg/jmemnobs.c',
            '../deps/skia/third_party/externals/libjpeg/jmemsys.h',
            '../deps/skia/third_party/externals/libjpeg/jmorecfg.h',
            '../deps/skia/third_party/externals/libjpeg/jpegint.h',
            '../deps/skia/third_party/externals/libjpeg/jpeglib.h',
            '../deps/skia/third_party/externals/libjpeg/jquant1.c',
            '../deps/skia/third_party/externals/libjpeg/jquant2.c',
            '../deps/skia/third_party/externals/libjpeg/jutils.c',
            '../deps/skia/third_party/externals/libjpeg/jversion.h',
          ],
          'direct_dependent_settings': {
            'include_dirs': [
              '../deps/skia/third_party/externals/libjpeg',
            ],
          },
          'conditions': [
            ['OS!="win"', {'product_name': 'jpeg'}],
            ['OS=="android"', {
              'cflags!': [
               '-fno-rtti', # supresses warnings about invalid option of non-C++ code
              ],
            }],
          ],
        },
      ],
    }, {
      'targets': [
        {
          'target_name': 'libjpeg',
          'type': 'none',
          'direct_dependent_settings': {
            'defines': [
              'USE_SYSTEM_LIBJPEG',
            ],
          },
          'link_settings': {
            'libraries': [
              '-ljpeg',
            ],
          },
        }
      ],
    }],
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
