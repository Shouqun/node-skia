{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'effects',
      'type': 'static_library',
      'include_dirs': [
        '../deps/skia/include/effects',
      ],
      'sources': [
        '../deps/skia/include/effects/Sk1DPathEffect.h',
        '../deps/skia/include/effects/Sk2DPathEffect.h',
        '../deps/skia/include/effects/SkAvoidXfermode.h',
        '../deps/skia/include/effects/SkArithmeticMode.h',
        '../deps/skia/include/effects/SkBlurDrawLooper.h',
        '../deps/skia/include/effects/SkBlurImageFilter.h',
        '../deps/skia/include/effects/SkBlurMaskFilter.h',
        '../deps/skia/include/effects/SkColorMatrix.h',
        '../deps/skia/include/effects/SkColorMatrixFilter.h',
        '../deps/skia/include/effects/SkCornerPathEffect.h',
        '../deps/skia/include/effects/SkDashPathEffect.h',
        '../deps/skia/include/effects/SkDiscretePathEffect.h',
        '../deps/skia/include/effects/SkDrawExtraPathEffect.h',
        '../deps/skia/include/effects/SkEmbossMaskFilter.h',
        '../deps/skia/include/effects/SkGradientShader.h',
        '../deps/skia/include/effects/SkGroupShape.h',
        '../deps/skia/include/effects/SkKernel33MaskFilter.h',
        '../deps/skia/include/effects/SkLayerDrawLooper.h',
        '../deps/skia/include/effects/SkLayerRasterizer.h',
        '../deps/skia/include/effects/SkLightingImageFilter.h',
        '../deps/skia/include/effects/SkMorphologyImageFilter.h',
        '../deps/skia/include/effects/SkPaintFlagsDrawFilter.h',
        '../deps/skia/include/effects/SkPixelXorXfermode.h',
        '../deps/skia/include/effects/SkPorterDuff.h',
        '../deps/skia/include/effects/SkRectShape.h',
        '../deps/skia/include/effects/SkStippleMaskFilter.h',
        '../deps/skia/include/effects/SkTableColorFilter.h',
        '../deps/skia/include/effects/SkTableMaskFilter.h',
        '../deps/skia/include/effects/SkTransparentShader.h',

        '../deps/skia/src/effects/Sk1DPathEffect.cpp',
        '../deps/skia/src/effects/Sk2DPathEffect.cpp',
        '../deps/skia/src/effects/SkAvoidXfermode.cpp',
        '../deps/skia/src/effects/SkArithmeticMode.cpp',
        '../deps/skia/src/effects/SkBlurDrawLooper.cpp',
        '../deps/skia/src/effects/SkBlurMask.cpp',
        '../deps/skia/src/effects/SkBlurMask.h',
        '../deps/skia/src/effects/SkBlurImageFilter.cpp',
        '../deps/skia/src/effects/SkBlurMaskFilter.cpp',
        '../deps/skia/src/effects/SkColorFilters.cpp',
        '../deps/skia/src/effects/SkColorMatrix.cpp',
        '../deps/skia/src/effects/SkColorMatrixFilter.cpp',
        '../deps/skia/src/effects/SkCornerPathEffect.cpp',
        '../deps/skia/src/effects/SkDashPathEffect.cpp',
        '../deps/skia/src/effects/SkDiscretePathEffect.cpp',
        '../deps/skia/src/effects/SkEmbossMask.cpp',
        '../deps/skia/src/effects/SkEmbossMask.h',
        '../deps/skia/src/effects/SkEmbossMask_Table.h',
        '../deps/skia/src/effects/SkEmbossMaskFilter.cpp',
        '../deps/skia/src/effects/SkGroupShape.cpp',
        '../deps/skia/src/effects/SkKernel33MaskFilter.cpp',
        '../deps/skia/src/effects/SkLayerDrawLooper.cpp',
        '../deps/skia/src/effects/SkLayerRasterizer.cpp',
        '../deps/skia/src/effects/SkLightingImageFilter.cpp',
        '../deps/skia/src/effects/SkMorphologyImageFilter.cpp',
        '../deps/skia/src/effects/SkPaintFlagsDrawFilter.cpp',
        '../deps/skia/src/effects/SkPixelXorXfermode.cpp',
        '../deps/skia/src/effects/SkPorterDuff.cpp',
        '../deps/skia/src/effects/SkRectShape.cpp',
        '../deps/skia/src/effects/SkStippleMaskFilter.cpp',
        '../deps/skia/src/effects/SkTableColorFilter.cpp',
        '../deps/skia/src/effects/SkTableMaskFilter.cpp',
        '../deps/skia/src/effects/SkTestImageFilters.cpp',
        '../deps/skia/src/effects/SkTransparentShader.cpp',

        '../deps/skia/src/effects/gradients/SkBitmapCache.cpp',
        '../deps/skia/src/effects/gradients/SkBitmapCache.h',
        '../deps/skia/src/effects/gradients/SkClampRange.cpp',
        '../deps/skia/src/effects/gradients/SkClampRange.h',
        '../deps/skia/src/effects/gradients/SkRadialGradient_Table.h',
        '../deps/skia/src/effects/gradients/SkGradientShader.cpp',
        '../deps/skia/src/effects/gradients/SkGradientShaderPriv.h',
        '../deps/skia/src/effects/gradients/SkLinearGradient.cpp',
        '../deps/skia/src/effects/gradients/SkLinearGradient.h',
        '../deps/skia/src/effects/gradients/SkRadialGradient.cpp',
        '../deps/skia/src/effects/gradients/SkRadialGradient.h',
        '../deps/skia/src/effects/gradients/SkTwoPointRadialGradient.cpp',
        '../deps/skia/src/effects/gradients/SkTwoPointRadialGradient.h',
        '../deps/skia/src/effects/gradients/SkTwoPointConicalGradient.cpp',
        '../deps/skia/src/effects/gradients/SkTwoPointConicalGradient.h',
        '../deps/skia/src/effects/gradients/SkSweepGradient.cpp',
        '../deps/skia/src/effects/gradients/SkSweepGradient.h',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../deps/skia/include/effects',
        ],
      },
      'dependencies': [
        'core.gyp:core',
      ],
      'conditions': [
        ['skia_gpu == 1', {
          'include_dirs': [
            '../deps/skia/src/gpu',
          ],
          'dependencies': [
            'gpu.gyp:gr',
          ],
        }],
      ],
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
