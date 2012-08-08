{
  'includes': [
    'common.gypi',
  ],
  'target_defaults': {
    'conditions': [
      ['skia_os != "win"', {
        'sources/': [ ['exclude', '_win.(h|cpp)$'],
        ],
      }],
      ['skia_os != "mac"', {
        'sources/': [ ['exclude', '_mac.(h|cpp)$'],
        ],
      }],
      ['skia_os != "linux"', {
        'sources/': [ ['exclude', '_unix.(h|cpp)$'],
        ],
      }],
      ['skia_os != "ios"', {
        'sources/': [ ['exclude', '_iOS.(h|cpp)$'],
        ],
      }],
      ['skia_os != "android"', {
        'sources/': [ ['exclude', '_android.(h|cpp)$'],
        ],
      }],
      [ 'skia_os == "android"', {
        'defines': [
          'GR_ANDROID_BUILD=1',
        ],
      }],
      [ 'skia_os == "mac"', {
        'defines': [
          'GR_MAC_BUILD=1',
        ],
      }],
      [ 'skia_os == "linux"', {
        'defines': [
          'GR_LINUX_BUILD=1',
        ],
      }],
      [ 'skia_os == "ios"', {
        'defines': [
          'GR_IOS_BUILD=1',
        ],
      }],
      [ 'skia_os == "win"', {
        'defines': [
          'GR_WIN32_BUILD=1',
        ],
      }],
      # nullify the targets in this gyp file if skia_gpu is 0
      [ 'skia_gpu == 0', {
        'sources/': [
          ['exclude', '.*'],
        ],
        'defines/': [
          ['exclude', '.*'],
        ],
        'include_dirs/': [
           ['exclude', '.*'],
        ],
        'link_settings': {
          'libraries/': [
            ['exclude', '.*'],
          ],
        },
        'direct_dependent_settings': {
          'defines/': [
            ['exclude', '.*'],
          ],
          'include_dirs/': [
            ['exclude', '.*'],
          ],
        },
      }],
    ],
    'direct_dependent_settings': {
      'conditions': [
        [ 'skia_os == "android"', {
          'defines': [
            'GR_ANDROID_BUILD=1',
          ],
        }],
        [ 'skia_os == "mac"', {
          'defines': [
            'GR_MAC_BUILD=1',
          ],
        }],
        [ 'skia_os == "linux"', {
          'defines': [
            'GR_LINUX_BUILD=1',
          ],
        }],
        [ 'skia_os == "ios"', {
          'defines': [
            'GR_IOS_BUILD=1',
          ],
        }],
        [ 'skia_os == "win"', {
          'defines': [
            'GR_WIN32_BUILD=1',
            'GR_GL_FUNCTION_TYPE=__stdcall',
          ],
        }],
      ],
      'include_dirs': [
        '../deps/skia/include/gpu',
      ],
    },
  },
  'targets': [
    {
      'target_name': 'skgr',
      'type': 'static_library',
      'include_dirs': [
        '../deps/skia/include/config',
        '../deps/skia/include/core',
        '../deps/skia/src/core',
        '../deps/skia/include/gpu',
        '../deps/skia/src/gpu',
      ],
      'dependencies': [
        'angle.gyp:*',
      ],
      'export_dependent_settings': [
        'angle.gyp:*',
      ],
      'sources': [
        '../deps/skia/include/gpu/SkGpuCanvas.h',
        '../deps/skia/include/gpu/SkGpuDevice.h',
        '../deps/skia/include/gpu/SkGr.h',
        '../deps/skia/include/gpu/SkGrPixelRef.h',
        '../deps/skia/include/gpu/SkGrTexturePixelRef.h',

        '../deps/skia/include/gpu/gl/SkGLContext.h',
        '../deps/skia/include/gpu/gl/SkMesaGLContext.h',
        '../deps/skia/include/gpu/gl/SkANGLEGLContext.h',
        '../deps/skia/include/gpu/gl/SkNativeGLContext.h',
        '../deps/skia/include/gpu/gl/SkNullGLContext.h',
        '../deps/skia/include/gpu/gl/SkDebugGLContext.h',

        '../deps/skia/src/gpu/SkGpuCanvas.cpp',
        '../deps/skia/src/gpu/SkGpuDevice.cpp',
        '../deps/skia/src/gpu/SkGr.cpp',
        '../deps/skia/src/gpu/SkGrFontScaler.cpp',
        '../deps/skia/src/gpu/SkGrPixelRef.cpp',
        '../deps/skia/src/gpu/SkGrTexturePixelRef.cpp',

        '../deps/skia/src/gpu/gl/SkGLContext.cpp',
        '../deps/skia/src/gpu/gl/SkNullGLContext.cpp',

        '../deps/skia/src/gpu/gl/debug/SkDebugGLContext.cpp',

        '../deps/skia/src/gpu/gl/mac/SkNativeGLContext_mac.cpp',

        '../deps/skia/src/gpu/gl/win/SkNativeGLContext_win.cpp',

        '../deps/skia/src/gpu/gl/unix/SkNativeGLContext_unix.cpp',

        '../deps/skia/src/gpu/gl/mesa/SkMesaGLContext.cpp',
        '../deps/skia/src/gpu/gl/angle/SkANGLEGLContext.cpp',
        '../deps/skia/src/gpu/gl/angle/GrGLCreateANGLEInterface.cpp',

        '../deps/skia/src/gpu/android/SkNativeGLContext_android.cpp',
      ],
      'conditions': [
        [ 'not skia_mesa', {
          'sources!': [
            '../deps/skia/src/gpu/gl/mesa/SkMesaGLContext.cpp',
          ],
        }],
        [ 'skia_mesa and skia_os == "mac"', {
          'include_dirs': [
             '$(SDKROOT)/usr/X11/include/',
          ],
        }],
        [ 'not skia_angle', {
          'sources!': [
            '../deps/skia/include/gpu/gl/SkANGLEGLContext.h',
            '../deps/skia/src/gpu/gl/angle/SkANGLEGLContext.cpp',
            '../deps/skia/src/gpu/gl/angle/GrGLCreateANGLEInterface.cpp',
          ],
        }],
      ],
    },
    {
      'target_name': 'gr',
      'type': 'static_library',
      'include_dirs': [
        '../deps/skia/include/core',
        '../deps/skia/include/config',
        '../deps/skia/include/gpu',
        '../deps/skia/src/core', # SkRasterClip.h
        '../deps/skia/src/gpu'
      ],
      'dependencies': [
        'angle.gyp:*',
      ],
      'export_dependent_settings': [
        'angle.gyp:*',
      ],
      'sources': [
        '../deps/skia/include/gpu/GrAARectRenderer.h',
        '../deps/skia/include/gpu/GrClipData.h',
        '../deps/skia/include/gpu/GrColor.h',
        '../deps/skia/include/gpu/GrConfig.h',
        '../deps/skia/include/gpu/GrContext.h',
        '../deps/skia/include/gpu/GrContextFactory.h',
        '../deps/skia/include/gpu/GrCustomStage.h',
        '../deps/skia/include/gpu/GrCustomStageUnitTest.h',
        '../deps/skia/include/gpu/GrFontScaler.h',
        '../deps/skia/include/gpu/GrGlyph.h',
        '../deps/skia/include/gpu/GrInstanceCounter.h',
        '../deps/skia/include/gpu/GrKey.h',
        '../deps/skia/include/gpu/GrMatrix.h',
        '../deps/skia/include/gpu/GrNoncopyable.h',
        '../deps/skia/include/gpu/GrPaint.h',
        '../deps/skia/include/gpu/GrPoint.h',
        '../deps/skia/include/gpu/GrProgramStageFactory.h',
        '../deps/skia/include/gpu/GrRect.h',
        '../deps/skia/include/gpu/GrRefCnt.h',
        '../deps/skia/include/gpu/GrRenderTarget.h',
        '../deps/skia/include/gpu/GrResource.h',
        '../deps/skia/include/gpu/GrSamplerState.h',
        '../deps/skia/include/gpu/GrScalar.h',
        '../deps/skia/include/gpu/GrSurface.h',
        '../deps/skia/include/gpu/GrTextContext.h',
        '../deps/skia/include/gpu/GrTexture.h',
        '../deps/skia/include/gpu/GrTypes.h',
        '../deps/skia/include/gpu/GrUserConfig.h',

        '../deps/skia/include/gpu/gl/GrGLConfig.h',
        '../deps/skia/include/gpu/gl/GrGLConfig_chrome.h',
        '../deps/skia/include/gpu/gl/GrGLFunctions.h',
        '../deps/skia/include/gpu/gl/GrGLInterface.h',

        '../deps/skia/src/gpu/GrAAHairLinePathRenderer.cpp',
        '../deps/skia/src/gpu/GrAAHairLinePathRenderer.h',
        '../deps/skia/src/gpu/GrAAConvexPathRenderer.cpp',
        '../deps/skia/src/gpu/GrAAConvexPathRenderer.h',
        '../deps/skia/src/gpu/GrAARectRenderer.cpp',
        '../deps/skia/src/gpu/GrAddPathRenderers_default.cpp',
        '../deps/skia/src/gpu/GrAllocator.h',
        '../deps/skia/src/gpu/GrAllocPool.h',
        '../deps/skia/src/gpu/GrAllocPool.cpp',
        '../deps/skia/src/gpu/GrAtlas.cpp',
        '../deps/skia/src/gpu/GrAtlas.h',
        '../deps/skia/src/gpu/GrBinHashKey.h',
        '../deps/skia/src/gpu/GrBufferAllocPool.cpp',
        '../deps/skia/src/gpu/GrBufferAllocPool.h',
        '../deps/skia/src/gpu/GrClipData.cpp',
        '../deps/skia/src/gpu/GrContext.cpp',
        '../deps/skia/src/gpu/GrCustomStage.cpp',
        '../deps/skia/src/gpu/GrDefaultPathRenderer.cpp',
        '../deps/skia/src/gpu/GrDefaultPathRenderer.h',
        '../deps/skia/src/gpu/GrDrawState.h',
        '../deps/skia/src/gpu/GrDrawTarget.cpp',
        '../deps/skia/src/gpu/GrDrawTarget.h',
        '../deps/skia/src/gpu/GrGeometryBuffer.h',
        '../deps/skia/src/gpu/GrClipMaskManager.h',
        '../deps/skia/src/gpu/GrClipMaskManager.cpp',
        '../deps/skia/src/gpu/GrGpu.cpp',
        '../deps/skia/src/gpu/GrGpu.h',
        '../deps/skia/src/gpu/GrGpuFactory.cpp',
        '../deps/skia/src/gpu/GrGpuVertex.h',
        '../deps/skia/src/gpu/GrIndexBuffer.h',
        '../deps/skia/src/gpu/GrInOrderDrawBuffer.cpp',
        '../deps/skia/src/gpu/GrInOrderDrawBuffer.h',
        '../deps/skia/src/gpu/GrMatrix.cpp',
        '../deps/skia/src/gpu/GrMemory.cpp',
        '../deps/skia/src/gpu/GrMemoryPool.cpp',
        '../deps/skia/src/gpu/GrMemoryPool.h',
        '../deps/skia/src/gpu/GrPath.h',
        '../deps/skia/src/gpu/GrPathRendererChain.cpp',
        '../deps/skia/src/gpu/GrPathRendererChain.h',
        '../deps/skia/src/gpu/GrPathRenderer.cpp',
        '../deps/skia/src/gpu/GrPathRenderer.h',
        '../deps/skia/src/gpu/GrPathUtils.cpp',
        '../deps/skia/src/gpu/GrPathUtils.h',
        '../deps/skia/src/gpu/GrPlotMgr.h',
        '../deps/skia/src/gpu/GrRandom.h',
        '../deps/skia/src/gpu/GrRectanizer.cpp',
        '../deps/skia/src/gpu/GrRectanizer.h',
        '../deps/skia/src/gpu/GrRedBlackTree.h',
        '../deps/skia/src/gpu/GrRenderTarget.cpp',
        '../deps/skia/src/gpu/GrResource.cpp',
        '../deps/skia/src/gpu/GrResourceCache.cpp',
        '../deps/skia/src/gpu/GrResourceCache.h',
        '../deps/skia/src/gpu/GrStencil.cpp',
        '../deps/skia/src/gpu/GrStencil.h',
        '../deps/skia/src/gpu/GrStencilAndCoverPathRenderer.cpp',
        '../deps/skia/src/gpu/GrStencilAndCoverPathRenderer.h',
        '../deps/skia/src/gpu/GrStencilBuffer.cpp',
        '../deps/skia/src/gpu/GrStencilBuffer.h',
        '../deps/skia/src/gpu/GrTBSearch.h',
        '../deps/skia/src/gpu/GrTDArray.h',
        '../deps/skia/src/gpu/GrSWMaskHelper.cpp',
        '../deps/skia/src/gpu/GrSWMaskHelper.h',
        '../deps/skia/src/gpu/GrSoftwarePathRenderer.cpp',
        '../deps/skia/src/gpu/GrSoftwarePathRenderer.h',
        '../deps/skia/src/gpu/GrSurface.cpp',
        '../deps/skia/src/gpu/GrTemplates.h',
        '../deps/skia/src/gpu/GrTextContext.cpp',
        '../deps/skia/src/gpu/GrTextStrike.cpp',
        '../deps/skia/src/gpu/GrTextStrike.h',
        '../deps/skia/src/gpu/GrTextStrike_impl.h',
        '../deps/skia/src/gpu/GrTexture.cpp',
        '../deps/skia/src/gpu/GrTHashCache.h',
        '../deps/skia/src/gpu/GrTLList.h',
        '../deps/skia/src/gpu/GrVertexBuffer.h',
        '../deps/skia/src/gpu/gr_unittests.cpp',

        '../deps/skia/src/gpu/effects/Gr1DKernelEffect.h',
        '../deps/skia/src/gpu/effects/GrColorTableEffect.cpp',
        '../deps/skia/src/gpu/effects/GrColorTableEffect.h',
        '../deps/skia/src/gpu/effects/GrConvolutionEffect.cpp',
        '../deps/skia/src/gpu/effects/GrConvolutionEffect.h',
        '../deps/skia/src/gpu/effects/GrMorphologyEffect.cpp',
        '../deps/skia/src/gpu/effects/GrMorphologyEffect.h',
        '../deps/skia/src/gpu/effects/GrSingleTextureEffect.cpp',
        '../deps/skia/src/gpu/effects/GrSingleTextureEffect.h',
        '../deps/skia/src/gpu/effects/GrTextureDomainEffect.cpp',
        '../deps/skia/src/gpu/effects/GrTextureDomainEffect.h',

        '../deps/skia/src/gpu/gl/GrGLCaps.cpp',
        '../deps/skia/src/gpu/gl/GrGLCaps.h',
        '../deps/skia/src/gpu/gl/GrGLContextInfo.cpp',
        '../deps/skia/src/gpu/gl/GrGLContextInfo.h',
        '../deps/skia/src/gpu/gl/GrGLCreateNativeInterface_none.cpp',
        '../deps/skia/src/gpu/gl/GrGLCreateNullInterface.cpp',
        '../deps/skia/src/gpu/gl/GrGLDefaultInterface_none.cpp',
        '../deps/skia/src/gpu/gl/GrGLDefaultInterface_native.cpp',
        '../deps/skia/src/gpu/gl/GrGLDefines.h',
        '../deps/skia/src/gpu/gl/GrGLIndexBuffer.cpp',
        '../deps/skia/src/gpu/gl/GrGLIndexBuffer.h',
        '../deps/skia/src/gpu/gl/GrGLInterface.cpp',
        '../deps/skia/src/gpu/gl/GrGLIRect.h',
        '../deps/skia/src/gpu/gl/GrGLPath.cpp',
        '../deps/skia/src/gpu/gl/GrGLPath.h',
        '../deps/skia/src/gpu/gl/GrGLProgram.cpp',
        '../deps/skia/src/gpu/gl/GrGLProgram.h',
        '../deps/skia/src/gpu/gl/GrGLProgramStage.cpp',
        '../deps/skia/src/gpu/gl/GrGLProgramStage.h',
        '../deps/skia/src/gpu/gl/GrGLRenderTarget.cpp',
        '../deps/skia/src/gpu/gl/GrGLRenderTarget.h',
        '../deps/skia/src/gpu/gl/GrGLShaderBuilder.cpp',
        '../deps/skia/src/gpu/gl/GrGLShaderBuilder.h',
        '../deps/skia/src/gpu/gl/GrGLShaderVar.h',
        '../deps/skia/src/gpu/gl/GrGLSL.cpp',
        '../deps/skia/src/gpu/gl/GrGLSL.h',
        '../deps/skia/src/gpu/gl/GrGLStencilBuffer.cpp',
        '../deps/skia/src/gpu/gl/GrGLStencilBuffer.h',
        '../deps/skia/src/gpu/gl/GrGLTexture.cpp',
        '../deps/skia/src/gpu/gl/GrGLTexture.h',
        '../deps/skia/src/gpu/gl/GrGLUtil.cpp',
        '../deps/skia/src/gpu/gl/GrGLUtil.h',
        '../deps/skia/src/gpu/gl/GrGLUniformManager.cpp',
        '../deps/skia/src/gpu/gl/GrGLUniformManager.h',
        '../deps/skia/src/gpu/gl/GrGLUniformHandle.h',
        '../deps/skia/src/gpu/gl/GrGLVertexBuffer.cpp',
        '../deps/skia/src/gpu/gl/GrGLVertexBuffer.h',
        '../deps/skia/src/gpu/gl/GrGpuGL.cpp',
        '../deps/skia/src/gpu/gl/GrGpuGL.h',
        '../deps/skia/src/gpu/gl/GrGpuGL_program.cpp',

        '../deps/skia/src/gpu/gl/debug/GrGLCreateDebugInterface.cpp',
        '../deps/skia/src/gpu/gl/debug/GrFakeRefObj.h',
        '../deps/skia/src/gpu/gl/debug/GrBufferObj.h',
        '../deps/skia/src/gpu/gl/debug/GrBufferObj.cpp',
        '../deps/skia/src/gpu/gl/debug/GrFBBindableObj.h',
        '../deps/skia/src/gpu/gl/debug/GrRenderBufferObj.h',
        '../deps/skia/src/gpu/gl/debug/GrTextureObj.h',
        '../deps/skia/src/gpu/gl/debug/GrTextureObj.cpp',
        '../deps/skia/src/gpu/gl/debug/GrTextureUnitObj.h',
        '../deps/skia/src/gpu/gl/debug/GrTextureUnitObj.cpp',
        '../deps/skia/src/gpu/gl/debug/GrFrameBufferObj.h',
        '../deps/skia/src/gpu/gl/debug/GrFrameBufferObj.cpp',
        '../deps/skia/src/gpu/gl/debug/GrShaderObj.h',
        '../deps/skia/src/gpu/gl/debug/GrShaderObj.cpp',
        '../deps/skia/src/gpu/gl/debug/GrProgramObj.h',
        '../deps/skia/src/gpu/gl/debug/GrProgramObj.cpp',
        '../deps/skia/src/gpu/gl/debug/GrDebugGL.h',
        '../deps/skia/src/gpu/gl/debug/GrDebugGL.cpp',

        '../deps/skia/src/gpu/gl/mac/GrGLCreateNativeInterface_mac.cpp',

        '../deps/skia/src/gpu/gl/win/GrGLCreateNativeInterface_win.cpp',

        '../deps/skia/src/gpu/gl/unix/GrGLCreateNativeInterface_unix.cpp',

        '../deps/skia/src/gpu/gl/mesa/GrGLCreateMesaInterface.cpp',
        '../deps/skia/src/gpu/gl/angle/GrGLCreateANGLEInterface.cpp',

        '../deps/skia/src/gpu/android/GrGLCreateNativeInterface_android.cpp',
      ],
      'defines': [
        'GR_IMPLEMENTATION=1',
      ],
      'conditions': [
        [ 'skia_nv_path_rendering', {
          'defines': [
            'GR_GL_USE_NV_PATH_RENDERING=1',
          ],
        }],
        [ 'skia_os == "linux"', {
          'sources!': [
            '../deps/skia/src/gpu/gl/GrGLDefaultInterface_none.cpp',
            '../deps/skia/src/gpu/gl/GrGLCreateNativeInterface_none.cpp',
          ],
          'link_settings': {
            'libraries': [
              '-lGL',
              '-lX11',
            ],
          },
        }],
        [ 'skia_mesa and skia_os == "linux"', {
          'link_settings': {
            'libraries': [
              '-lOSMesa',
            ],
          },
        }],
        [ 'skia_os == "mac"', {
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/OpenGL.framework',
            ],
          },
          'sources!': [
            '../deps/skia/src/gpu/gl/GrGLDefaultInterface_none.cpp',
            '../deps/skia/src/gpu/gl/GrGLCreateNativeInterface_none.cpp',
          ],
        }],
        [ 'skia_mesa and skia_os == "mac"', {
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/usr/X11/lib/libOSMesa.dylib',
            ],
          },
          'include_dirs': [
             '$(SDKROOT)/usr/X11/include/',
          ],
        }],
        [ 'not skia_mesa', {
          'sources!': [
            '../deps/skia/src/gpu/gl/mesa/GrGLCreateMesaInterface.cpp',
          ],
        }],
        [ 'skia_os == "win"', {
          'sources!': [
            '../deps/skia/src/gpu/gl/GrGLDefaultInterface_none.cpp',
            '../deps/skia/src/gpu/gl/GrGLCreateNativeInterface_none.cpp',
          ],
        }],
        [ 'not skia_angle', {
          'sources!': [
            '../deps/skia/include/gpu/gl/SkANGLEGLContext.h',

            '../deps/skia/src/gpu/gl/angle/GrGLCreateANGLEInterface.cpp',
            '../deps/skia/src/gpu/gl/angle/SkANGLEGLContext.cpp',
          ],
        }],
        [ 'skia_os == "android"', {
          'sources!': [
            '../deps/skia/src/gpu/gl/GrGLDefaultInterface_none.cpp',
            '../deps/skia/src/gpu/gl/GrGLCreateNativeInterface_none.cpp',
          ],
          'link_settings': {
            'libraries': [
              '-lGLESv2',
              '-lEGL',
            ],
          },
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
