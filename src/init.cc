#include <node.h>
#include <v8.h>

#include "skia_bitmap.h"
#include "skia_canvas.h"
#include "skia_paint.h"

using namespace v8;

void init(Handle<Object> target) {
  HandleScope scope;

  NodeSkiaBitmap::Initialize(target);
  NodeSkiaCanvas::Initialize(target);
  NodeSkiaPaint::Initialize(target);
}

NODE_MODULE(skialib, init)
