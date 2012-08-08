{
  'includes': [
    'common.gypi'
  ],
  'targets': [
    # Due to an unfortunate intersection of lameness between gcc and gyp,
    # we have to build the *_SSE2.cpp files in a separate target.  The
    # gcc lameness is that, in order to compile SSE2 intrinsics code, it
    # must be passed the -msse2 flag.  However, with this flag, it may
    # emit SSE2 instructions even for scalar code, such as the CPUID
    # test used to test for the presence of SSE2.  So that, and all other
    # code must be compiled *without* -msse2.  The gyp lameness is that it
    # does not allow file-specific CFLAGS, so we must create this extra
    # target for those files to be compiled with -msse2.
    #
    # This is actually only a problem on 32-bit Linux (all Intel Macs have
    # SSE2, Linux x86_64 has SSE2 by definition, and MSC will happily emit
    # SSE2 from instrinsics, while generating plain ol' 386 for everything
    # else).  However, to keep the .gyp file simple and avoid platform-specific
    # build breakage, we do this on all platforms.

    # For about the same reason, we need to compile the ARM opts files
    # separately as well.
    {
      'target_name': 'opts',
      'type': 'static_library',
      'include_dirs': [
        '../deps/skia/include/config',
        '../deps/skia/include/core',
        '../deps/skia/src/core',
        '../deps/skia/src/opts',
      ],
      'conditions': [
        [ 'skia_arch_type == "x86"', {
          'conditions': [
            [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris"]', {
              'cflags': [
                '-msse2',
              ],
            }],
          ],
          'sources': [
            '../deps/skia/src/opts/opts_check_SSE2.cpp',
            '../deps/skia/src/opts/SkBitmapProcState_opts_SSE2.cpp',
            '../deps/skia/src/opts/SkBlitRow_opts_SSE2.cpp',
            '../deps/skia/src/opts/SkBlitRect_opts_SSE2.cpp',
            '../deps/skia/src/opts/SkUtils_opts_SSE2.cpp',
          ],
          'dependencies': [
            'opts_ssse3',
          ],
        }],
        [ 'skia_arch_type == "arm" and armv7 == 1', {
          # The assembly uses the frame pointer register (r7 in Thumb/r11 in
          # ARM), the compiler doesn't like that.
          'cflags!': [
            '-fno-omit-frame-pointer',
          ],
          'cflags': [
            '-fomit-frame-pointer',
          ],
          'variables': {
            'arm_neon_optional%': '<(arm_neon_optional>',
          },
          'sources': [
            '../deps/skia/src/opts/opts_check_arm.cpp',
            '../deps/skia/src/opts/memset.arm.S',
            '../deps/skia/src/opts/SkBitmapProcState_opts_arm.cpp',
            '../deps/skia/src/opts/SkBlitRow_opts_arm.cpp',
          ],
          'conditions': [
            [ 'arm_neon == 1 or arm_neon_optional == 1', {
              'dependencies': [
                'opts_neon',
              ]
            }]
          ],
        }],
        [ 'skia_arch_type == "arm" and armv7 != 1', {
          'sources': [
            '../deps/skia/src/opts/SkBitmapProcState_opts_none.cpp',
            '../deps/skia/src/opts/SkBlitRow_opts_none.cpp',
            '../deps/skia/src/opts/SkUtils_opts_none.cpp',
          ],
        }],
      ],
    },
    # For the same lame reasons as what is done for skia_opts, we have to
    # create another target specifically for SSSE3 code as we would not want
    # to compile the SSE2 code with -mssse3 which would potentially allow
    # gcc to generate SSSE3 code.
    {
      'target_name': 'opts_ssse3',
      'type': 'static_library',
      'include_dirs': [
        '../deps/skia/include/config',
        '../deps/skia/include/core',
        '../deps/skia/src/core',
      ],
      'conditions': [
        [ 'skia_os in ["linux", "freebsd", "openbsd", "solaris"]', {
          'cflags': [
            '-mssse3',
          ],
        }],
        # TODO(epoger): the following will enable SSSE3 on Macs, but it will
        # break once we set OTHER_CFLAGS anywhere else (the first setting will
        # be replaced, not added to)
        [ 'skia_os in ["mac"]', {
          'xcode_settings': {
            'OTHER_CFLAGS': ['-mssse3',],
          },
        }],
        [ 'skia_arch_type == "x86"', {
          'sources': [
            '../deps/skia/src/opts/SkBitmapProcState_opts_SSSE3.cpp',
          ],
        }],
      ],
    },
    # NEON code must be compiled with -mfpu=neon which also affects scalar
    # code. To support dynamic NEON code paths, we need to build all
    # NEON-specific sources in a separate static library. The situation
    # is very similar to the SSSE3 one.
    {
      'target_name': 'opts_neon',
      'type': 'static_library',
      'include_dirs': [
        '../deps/skia/include/config',
        '../deps/skia/include/core',
        '../deps/skia/src/core',
        '../deps/skia/src/opts',
      ],
      'cflags!': [
        '-fno-omit-frame-pointer',
        '-mfpu=vfp',  # remove them all, just in case.
        '-mfpu=vfpv3',
        '-mfpu=vfpv3-d16',
      ],
      'cflags': [
        '-mfpu=neon',
        '-fomit-frame-pointer',
      ],
      'sources': [
        '../deps/skia/src/opts/memset16_neon.S',
        '../deps/skia/src/opts/memset32_neon.S',
        '../deps/skia/src/opts/SkBitmapProcState_matrixProcs_neon.cpp',
        '../deps/skia/src/opts/SkBitmapProcState_matrix_clamp_neon.h',
        '../deps/skia/src/opts/SkBitmapProcState_matrix_repeat_neon.h',
      ],
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
