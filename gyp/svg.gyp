{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'svg',
      'type': 'static_library',
      'include_dirs': [
        '../deps/skia/include/config',
        '../deps/skia/include/core',
        '../deps/skia/include/xml',
        '../deps/skia/include/utils',
        '../deps/skia/include/svg',
      ],
      'sources': [
        '../deps/skia/include/svg/SkSVGAttribute.h',
        '../deps/skia/include/svg/SkSVGBase.h',
        '../deps/skia/include/svg/SkSVGPaintState.h',
        '../deps/skia/include/svg/SkSVGParser.h',
        '../deps/skia/include/svg/SkSVGTypes.h',

        '../deps/skia/src/svg/SkSVGCircle.cpp',
        '../deps/skia/src/svg/SkSVGCircle.h',
        '../deps/skia/src/svg/SkSVGClipPath.cpp',
        '../deps/skia/src/svg/SkSVGClipPath.h',
        '../deps/skia/src/svg/SkSVGDefs.cpp',
        '../deps/skia/src/svg/SkSVGDefs.h',
        '../deps/skia/src/svg/SkSVGElements.cpp',
        '../deps/skia/src/svg/SkSVGElements.h',
        '../deps/skia/src/svg/SkSVGEllipse.cpp',
        '../deps/skia/src/svg/SkSVGEllipse.h',
        '../deps/skia/src/svg/SkSVGFeColorMatrix.cpp',
        '../deps/skia/src/svg/SkSVGFeColorMatrix.h',
        '../deps/skia/src/svg/SkSVGFilter.cpp',
        '../deps/skia/src/svg/SkSVGFilter.h',
        '../deps/skia/src/svg/SkSVGG.cpp',
        '../deps/skia/src/svg/SkSVGG.h',
        '../deps/skia/src/svg/SkSVGGradient.cpp',
        '../deps/skia/src/svg/SkSVGGradient.h',
        '../deps/skia/src/svg/SkSVGGroup.cpp',
        '../deps/skia/src/svg/SkSVGGroup.h',
        '../deps/skia/src/svg/SkSVGImage.cpp',
        '../deps/skia/src/svg/SkSVGImage.h',
        '../deps/skia/src/svg/SkSVGLine.cpp',
        '../deps/skia/src/svg/SkSVGLine.h',
        '../deps/skia/src/svg/SkSVGLinearGradient.cpp',
        '../deps/skia/src/svg/SkSVGLinearGradient.h',
        '../deps/skia/src/svg/SkSVGMask.cpp',
        '../deps/skia/src/svg/SkSVGMask.h',
        '../deps/skia/src/svg/SkSVGMetadata.cpp',
        '../deps/skia/src/svg/SkSVGMetadata.h',
        '../deps/skia/src/svg/SkSVGPaintState.cpp',
        '../deps/skia/src/svg/SkSVGParser.cpp',
        '../deps/skia/src/svg/SkSVGPath.cpp',
        '../deps/skia/src/svg/SkSVGPath.h',
        '../deps/skia/src/svg/SkSVGPolygon.cpp',
        '../deps/skia/src/svg/SkSVGPolygon.h',
        '../deps/skia/src/svg/SkSVGPolyline.cpp',
        '../deps/skia/src/svg/SkSVGPolyline.h',
        '../deps/skia/src/svg/SkSVGRadialGradient.cpp',
        '../deps/skia/src/svg/SkSVGRadialGradient.h',
        '../deps/skia/src/svg/SkSVGRect.cpp',
        '../deps/skia/src/svg/SkSVGRect.h',
        '../deps/skia/src/svg/SkSVGStop.cpp',
        '../deps/skia/src/svg/SkSVGStop.h',
        '../deps/skia/src/svg/SkSVGSVG.cpp',
        '../deps/skia/src/svg/SkSVGSVG.h',
        '../deps/skia/src/svg/SkSVGSymbol.cpp',
        '../deps/skia/src/svg/SkSVGSymbol.h',
        '../deps/skia/src/svg/SkSVGText.cpp',
        '../deps/skia/src/svg/SkSVGText.h',
        '../deps/skia/src/svg/SkSVGUse.cpp',
      ],
      'sources!' : [
          '../deps/skia/src/svg/SkSVG.cpp', # doesn't compile, maybe this is test code?
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../deps/skia/include/svg',
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
